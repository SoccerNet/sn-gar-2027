"""Train the OpenSportsLib GAR tracking baseline and export a submission ZIP.

Run from an OpenSportsLib checkout with a configured GPU and Hugging Face access.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

import yaml


TRACKING_REVISION = "589eba2aaa71da6c3fda7c2e6396e9fd6610a369"


def convert(predictions: dict, manifest: dict) -> dict:
    if not isinstance(predictions, dict) or not isinstance(predictions.get("data"), list):
        raise ValueError("OpenSportsLib inference did not return a data list")
    classes = set(manifest["labels"]["action"]["labels"])
    expected = {item["id"] for item in manifest["data"]}
    by_id = {}
    for item in predictions["data"]:
        sample_id = item["id"]
        label = item["labels"]["action"]["label"]
        if sample_id in by_id or label not in classes:
            raise ValueError(f"Duplicate ID or unknown class: {sample_id}")
        action = {"label": label}
        confidence = item["labels"]["action"].get("confidence")
        if isinstance(confidence, (int, float)):
            action["confidence"] = confidence
        by_id[sample_id] = {"id": sample_id, "labels": {"action": action}}
    if set(by_id) != expected:
        raise ValueError(f"Predictions cover {len(by_id)} IDs; expected {len(expected)}")
    return {
        "version": "2.0",
        "date": date.today().isoformat(),
        "task": "action_classification",
        "dataset_name": "soccernet_gar_2027_predictions",
        "metadata": {"type": "predictions"},
        "data": [by_id[item["id"]] for item in manifest["data"]],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path,
                        default=Path("examples/sngar/sngar_tracking_hf.yaml"))
    parser.add_argument("--manifest", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data/annotations_test.json")
    parser.add_argument("--cache-dir", type=Path,
                        default=Path("~/.cache/opensportslib/sngar"))
    parser.add_argument("--output-dir", type=Path, default=Path("gar-baseline-output"))
    parser.add_argument("--checkpoint", type=Path,
                        help="Use an existing validation-selected checkpoint instead of training")
    args = parser.parse_args()

    from opensportslib.apis import ClassificationModel

    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if config["DATA"]["inputs"]["tracking"]["source"]["format"] != "hf_webdataset":
        raise ValueError("The supplied config must use OpenSportsLib's HF tracking source")
    cache_dir = args.cache_dir.expanduser().resolve()
    output_dir = args.output_dir.expanduser().resolve()
    cache_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    config["DATA"]["common"]["data_root"] = str(cache_dir)
    config["DATA"]["inputs"]["tracking"]["source"]["cache_dir"] = str(cache_dir)
    config["DATA"]["inputs"]["tracking"]["source"]["revision"] = TRACKING_REVISION
    config["SYSTEM"]["paths"]["save_dir"] = str(output_dir / "checkpoints")
    config["SYSTEM"]["paths"]["work_dir"] = str(output_dir / "checkpoints")
    config["SYSTEM"]["paths"]["log_dir"] = str(output_dir / "logs")
    config["SYSTEM"]["gpu"]["count"] = 1

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    if manifest["metadata"]["hf_sources"]["tracking"]["commit"] != TRACKING_REVISION:
        raise ValueError("Baseline and challenge manifest tracking revisions differ")
    with tempfile.TemporaryDirectory(prefix="gar-baseline-config-") as temp_dir:
        config_path = Path(temp_dir) / "config.yaml"
        config_path.write_text(yaml.safe_dump(config), encoding="utf-8")
        model = ClassificationModel(config=str(config_path))
        checkpoint = str(args.checkpoint.expanduser().resolve()) if args.checkpoint else model.train(
            use_ddp=False, use_wandb=False
        )
        predictions = model.infer(weights=checkpoint, use_ddp=False, use_wandb=False)
    prediction_file = convert(predictions, manifest)
    submission = output_dir / "predictions.json"
    submission.write_text(json.dumps(prediction_file, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with ZipFile(output_dir / "gar-submission.zip", "w", ZIP_DEFLATED) as archive:
        archive.write(submission, "predictions.json")
    (output_dir / "run.json").write_text(
        json.dumps({"checkpoint": checkpoint, "tracking_revision": TRACKING_REVISION,
                    "config": str(args.config.resolve()), "sample_count": len(prediction_file["data"])}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Checkpoint: {checkpoint}")
    print(f"Submission: {output_dir / 'gar-submission.zip'}")


if __name__ == "__main__":
    main()
