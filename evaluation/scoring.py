"""Score OpenSportsLib JSON predictions against OpenSportsLib JSON ground truth."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON key")
        result[key] = value
    return result


def load_json(path: Path):
    if path.stat().st_size > 50_000_000:
        raise ValueError("JSON file exceeds 50 MB")
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=unique_object,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON value")),
    )


def osl_labels(document, *, require_schema: bool):
    if not isinstance(document, dict) or document.get("version") != "2.0":
        raise ValueError("Expected an OpenSportsLib JSON object with version '2.0'")
    if document.get("task") != "action_classification":
        raise ValueError("Expected task 'action_classification'")
    rows = document.get("data")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected a nonempty OSL data list")

    classes = None
    if require_schema:
        action_schema = (document.get("labels") or {}).get("action")
        if not isinstance(action_schema, dict) or action_schema.get("type") != "single_label":
            raise ValueError("Ground truth must define a single-label action schema")
        classes = action_schema.get("labels")
        if (
            not isinstance(classes, list)
            or not classes
            or any(not isinstance(label, str) or not label for label in classes)
            or len(set(classes)) != len(classes)
        ):
            raise ValueError("Ground truth requires unique action class names")

    indexed = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Each OSL data item must be an object")
        sample_id = row.get("id")
        action = (row.get("labels") or {}).get("action")
        label = action.get("label") if isinstance(action, dict) else None
        if not isinstance(sample_id, str) or not sample_id or sample_id in indexed:
            raise ValueError("Sample IDs must be nonempty unique strings")
        if not isinstance(label, str) or not label:
            raise ValueError(f"Missing OSL labels.action.label for {sample_id}")
        indexed[sample_id] = label
    return classes, indexed


def score(ground_truth, predictions):
    """Return percentage metrics, delegating computation to OpenSportsLib."""
    classes, truth = osl_labels(ground_truth, require_schema=True)
    _, pred = osl_labels(predictions, require_schema=False)
    if set(pred) != set(truth):
        raise ValueError("Prediction IDs must cover every ground-truth ID exactly once")
    if set(truth.values()) != set(classes):
        raise ValueError("Ground truth must contain every configured action class")
    if not set(pred.values()) <= set(classes):
        raise ValueError("Prediction contains an unknown action class")

    from opensportslib.metrics.classification_metric import compute_classification_metrics

    class_to_index = {name: index for index, name in enumerate(classes)}
    ids = list(truth)
    labels = [class_to_index[truth[sample_id]] for sample_id in ids]
    predicted = [class_to_index[pred[sample_id]] for sample_id in ids]
    metrics = compute_classification_metrics((predicted, labels), mode="labels")
    return {
        "balanced_accuracy": 100.0 * float(metrics["balanced_accuracy"]),
        "macro_f1": 100.0 * float(metrics["f1"]),
        "accuracy": 100.0 * float(metrics["accuracy"]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ground-truth", type=Path,
                        help="OSL ground-truth JSON; use this with --predictions for local scoring")
    parser.add_argument("--predictions", type=Path,
                        help="OSL prediction JSON; use this with --ground-truth for local scoring")
    parser.add_argument("--input", type=Path, default=Path("/app/input"),
                        help="CodaBench input directory (default: /app/input)")
    parser.add_argument("--output", type=Path,
                        help="Optional directory for scores.json; CodaBench passes /app/output")
    args = parser.parse_args()

    if bool(args.ground_truth) != bool(args.predictions):
        parser.error("Supply both --ground-truth and --predictions, or neither")
    if args.ground_truth:
        ground_truth_path, predictions_path = args.ground_truth, args.predictions
    else:
        ground_truth_path = args.input / "ref" / "reference.json"
        predictions_path = args.input / "res" / "predictions.json"

    try:
        scores = score(load_json(ground_truth_path), load_json(predictions_path))
        serialized = json.dumps(scores, allow_nan=False)
        if args.output:
            args.output.mkdir(parents=True, exist_ok=True)
            (args.output / "scores.json").write_text(serialized, encoding="utf-8")
        print(serialized)
    except (ValueError, KeyError, TypeError, OSError, ImportError) as exc:
        print(f"Scoring failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
