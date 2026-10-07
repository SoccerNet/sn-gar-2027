# GAR evaluation

The [scorer](scoring.py) calls OpenSportsLib's `compute_classification_metrics(..., mode="labels")`. It reports balanced accuracy, macro F1, and accuracy as percentages. **Balanced accuracy** determines the single leaderboard. The scoring environment pins OpenSportsLib commit `dc96cbfd0128fa77cb3bf1b3319e5fdf8c53b5a7` in the [Dockerfile](Dockerfile).

## Prediction format

Submit a ZIP containing `predictions.json` at its root. This JSON file is a list of records such as `{"id":"test_000000","label":"PASS"}`. IDs must be unique and cover all **13,689 IDs** in the [test manifest](../data/test_manifest.json), with no extras. Records may appear in any order. Labels must match one of the ten class names in that manifest, including capitalization and spaces. The scorer's reference JSON uses `{"task":"gar","classes":[...],"records":[{"id":"...","label":"..."}]}`.

## Local scoring

Place `reference.json` at `input/ref/reference.json` and the participant's `predictions.json` at `input/res/predictions.json`. Install the dependencies from the [Dockerfile](Dockerfile), then run from the repository root:

```bash
python evaluation/scoring.py --input input --output output
```

The script writes `output/scores.json`. The reference file contains labels; only the evaluation environment needs it. Submitted code supports reproducibility review under the [rules](../RULES.md).

The [reference builder](build_reference.py) validates matching test IDs and labels across the pinned tracking and frames revisions, writes the public ID manifest, and produces the scorer reference under the ignored `private/` directory. It requires `pyarrow` and `huggingface_hub` in addition to access to the gated dataset.
