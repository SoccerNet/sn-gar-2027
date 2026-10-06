# GAR evaluation

The [scorer](scoring.py) calls OpenSportsLib's `compute_classification_metrics(..., mode="labels")`. It reports balanced accuracy, macro F1, and accuracy as percentages. **Balanced accuracy** determines the single leaderboard. The scoring environment pins OpenSportsLib commit `dc96cbfd0128fa77cb3bf1b3319e5fdf8c53b5a7` in the [Dockerfile](Dockerfile).

## Prediction format

Submit a ZIP containing `predictions.json` at its root. This JSON file is a list of records such as `{"id":"clip-id","label":"class-name"}`. IDs must be unique and match the reference IDs exactly. Labels must belong to its ten-class vocabulary. The reference JSON uses `{"task":"gar","classes":[...],"records":[{"id":"...","label":"..."}]}`.

## Local scoring

Place `reference.json` at `input/ref/reference.json` and the participant's `predictions.json` at `input/res/predictions.json`. Install the dependencies from the [Dockerfile](Dockerfile), then run from the repository root:

```bash
python evaluation/scoring.py --input input --output output
```

The script writes `output/scores.json`. The reference file contains labels; only the evaluation environment needs it. Predictions alone cannot establish which input modality a method used, so submitted code supplies that evidence under the [rules](../RULES.md).
