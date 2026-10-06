# Evaluation — OpenSportsLib adapter, draft 2027 protocol

The scorer delegates classification metrics to OpenSportsLib's `compute_classification_metrics(..., mode="labels")`. Its reference schema and 2027 leaderboard policy still need organizer approval. The image pins OpenSportsLib commit `dc96cbfd0128fa77cb3bf1b3319e5fdf8c53b5a7`; review and re-pin before launch.

## Metrics

The scorer returns OpenSportsLib balanced accuracy, macro F1 and accuracy as percentages. **Balanced accuracy is the selected ranking metric on one leaderboard.** Classes are read from the reference's `classes` array, and every configured class must occur in the evaluated reference. Tie handling and modality eligibility remain open.

## Submission and reference contract

Submit a ZIP containing `predictions.json` at its root. The file is a JSON list of `{ "id": "...", "label": "..." }` records. IDs must be unique and match the reference exactly. Labels must belong to the frozen `classes` vocabulary. The private reference uses `{"task":"gar","classes":[...],"records":[{"id":"...","label":"..."}]}`. The real 2027 test-ID manifest is still pending.

## Local check and CodaBench

Use Python 3.12 and install OpenSportsLib at the pinned commit with the dependencies in [Dockerfile](Dockerfile), or build that image. From this repository root:

```bash
python evaluation/scoring.py --input /path/to/input --output /path/to/output
```

CodaBench runs `evaluation/scoring.py` with `/app/input/ref/reference.json` and `/app/input/res/predictions.json`, writing `/app/output/scores.json`. The scoring package must use an image that has the pinned OpenSportsLib and scikit-learn installed. Put real reference labels only in the organizer package. Do not publish them in this repository or the participant bundle. The task is not live on CodaBench yet.

The scorer checks submission syntax and labels. Pixel-only versus position-only restrictions require separate track configuration and, if needed, a finalist method audit; predictions alone cannot prove which modality was used.
