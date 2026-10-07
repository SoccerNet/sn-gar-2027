"""CodaBench adapter for SoccerNet-GAR using OpenSportsLib classification metrics."""
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


def indexed(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected a nonempty list of records")
    result = {}
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"id", "label"}:
            raise ValueError("Each record must contain exactly id and label")
        key, value = row["id"], row["label"]
        if not isinstance(key, str) or not key or key in result:
            raise ValueError("IDs must be nonempty unique strings")
        if not isinstance(value, str) or not value:
            raise ValueError("Labels must be nonempty strings")
        result[key] = value
    return result


def score(reference, predictions):
    """Return percentage metrics; computation delegates to OpenSportsLib."""
    if not isinstance(reference, dict) or reference.get("task") != "gar":
        raise ValueError("Unsupported reference task")
    classes = reference.get("classes")
    if (
        not isinstance(classes, list)
        or not classes
        or any(not isinstance(c, str) or not c for c in classes)
        or len(set(classes)) != len(classes)
    ):
        raise ValueError("Reference requires unique class names")
    truth = indexed(reference["records"])
    pred = indexed(predictions)
    if set(pred) != set(truth):
        raise ValueError("Submission must cover every expected ID exactly once, with no extras")
    if set(truth.values()) != set(classes):
        raise ValueError("Reference must contain every configured class")
    if not set(pred.values()) <= set(classes):
        raise ValueError("Unknown predicted class")

    from opensportslib.metrics.classification_metric import compute_classification_metrics

    class_to_index = {name: i for i, name in enumerate(classes)}
    ids = list(truth)
    labels = [class_to_index[truth[key]] for key in ids]
    predictions = [class_to_index[pred[key]] for key in ids]
    osl = compute_classification_metrics((predictions, labels), mode="labels")
    return {
        "balanced_accuracy": 100.0 * float(osl["balanced_accuracy"]),
        "macro_f1": 100.0 * float(osl["f1"]),
        "accuracy": 100.0 * float(osl["accuracy"]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("/app/input"))
    parser.add_argument("--output", type=Path, default=Path("/app/output"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    output = args.output / "scores.json"
    output.unlink(missing_ok=True)
    try:
        scores = score(
            load_json(args.input / "ref" / "reference.json"),
            load_json(args.input / "res" / "predictions.json"),
        )
        output.write_text(json.dumps(scores, allow_nan=False), encoding="utf-8")
        print("Scoring completed successfully.")
    except (ValueError, KeyError, TypeError, OSError, ImportError):
        print("Scoring failed: check format, IDs, labels, and OpenSportsLib installation.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
