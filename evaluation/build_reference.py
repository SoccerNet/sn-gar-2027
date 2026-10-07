"""Build the GAR test-ID manifest and scoring reference from pinned HF metadata.

The manifest contains IDs and class names only. The reference contains labels
and is written under private/ by default, which this repository ignores.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ID = "OpenSportsLab/SoccerNet-GAR"
REVISIONS = {
    "tracking": "589eba2aaa71da6c3fda7c2e6396e9fd6610a369",
    "frames": "629043a5f3fe74e53095c7b8d3c0b489ff0d0269",
}


def read_metadata(path: Path):
    import pyarrow.parquet as pq

    table = pq.read_table(path, columns=["sample_id", "sample_payload", "header"])
    ids = table["sample_id"].to_pylist()
    payloads = [json.loads(value) for value in table["sample_payload"].to_pylist()]
    headers = [json.loads(value) for value in table["header"].to_pylist()]
    if not ids or len(ids) != len(set(ids)) or any(not isinstance(i, str) or not i for i in ids):
        raise ValueError(f"Empty or duplicate sample IDs in {path}")
    classes = headers[0]["labels"]["action"]["labels"]
    if len(classes) != 10 or len(set(classes)) != 10:
        raise ValueError(f"Expected ten unique GAR classes in {path}")
    if any(h["labels"]["action"]["labels"] != classes for h in headers):
        raise ValueError(f"Inconsistent class order in {path}")
    records = {}
    for sample_id, payload in zip(ids, payloads):
        label = payload["labels"]["action"]["label"]
        if payload["id"] != sample_id or label not in classes:
            raise ValueError(f"Invalid payload for {sample_id}")
        records[sample_id] = label
    return ids, classes, records


def build(tracking_path: Path, frames_path: Path):
    tracking_ids, tracking_classes, tracking_labels = read_metadata(tracking_path)
    frames_ids, frames_classes, frames_labels = read_metadata(frames_path)
    if tracking_classes != frames_classes:
        raise ValueError("Tracking and frame class orders differ")
    if set(tracking_ids) != set(frames_ids) or tracking_labels != frames_labels:
        raise ValueError("Tracking and frame IDs or labels differ")
    manifest = {
        "dataset": REPO_ID,
        "split": "test",
        "revisions": REVISIONS,
        "classes": tracking_classes,
        "ids": tracking_ids,
    }
    reference = {
        "task": "gar",
        "classes": tracking_classes,
        "records": [{"id": sample_id, "label": tracking_labels[sample_id]}
                    for sample_id in tracking_ids],
    }
    return manifest, reference


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tracking-metadata", type=Path)
    parser.add_argument("--frames-metadata", type=Path)
    parser.add_argument("--manifest-out", type=Path, default=Path("data/test_manifest.json"))
    parser.add_argument("--reference-out", type=Path, default=Path("private/reference.json"))
    args = parser.parse_args()
    if bool(args.tracking_metadata) != bool(args.frames_metadata):
        parser.error("Supply both metadata paths or neither")
    if args.tracking_metadata:
        tracking_path, frames_path = args.tracking_metadata, args.frames_metadata
    else:
        from huggingface_hub import hf_hub_download

        tracking_path, frames_path = (
            Path(hf_hub_download(REPO_ID, "test/metadata.parquet", repo_type="dataset",
                                 revision=REVISIONS[modality]))
            for modality in ("tracking", "frames")
        )
    if args.manifest_out.resolve() == args.reference_out.resolve():
        parser.error("Manifest and reference output paths must differ")
    manifest, reference = build(tracking_path, frames_path)
    for path, value in ((args.manifest_out, manifest), (args.reference_out, reference)):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n",
                        encoding="utf-8")
    print(f"Validated {len(manifest['ids'])} aligned GAR test IDs across both modalities.")
    print(f"Public ID manifest: {args.manifest_out}")
    print(f"Scoring reference: {args.reference_out}")


if __name__ == "__main__":
    main()
