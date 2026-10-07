# GAR evaluation

The [CodaBench evaluation server](https://www.codabench.org/competitions/18326/) accepts result submissions. Every submission must be an OpenSportsLib JSON prediction file. The scorer reads the OpenSportsLib ground-truth JSON and the submitted OpenSportsLib prediction JSON, matches records by sample ID, and calls OpenSportsLib's `compute_classification_metrics(..., mode="labels")`. It reports balanced accuracy, macro F1, and accuracy as percentages. **Balanced accuracy** determines the single leaderboard. The CodaBench scoring image pins OpenSportsLib in the [Dockerfile](Dockerfile).

## Prediction format

Submit a ZIP containing `predictions.json` at its root. The JSON must be an OSL object with version `2.0`, task `action_classification`, and a `data` array. Each sample must include its unique test `id` and an action label at `labels.action.label`. The example below shows the required structure; optional OSL fields such as prediction confidence may also be included.

```json
{
  "version": "2.0",
  "task": "action_classification",
  "dataset_name": "soccernet_gar_2027_predictions",
  "metadata": { "type": "predictions" },
  "data": [
    {
      "id": "test_000000",
      "labels": { "action": { "label": "PASS" } }
    }
  ]
}
```

The prediction IDs must cover every sample in the [OSL test ground truth](../data/annotations_test.json) exactly once, with no extra IDs. Labels must match one of the ten class names in that file, including capitalization and spaces. The scorer compares the two JSON files by ID, so record order does not affect the score.

## Local scoring

Install the dependencies listed in the [Dockerfile](Dockerfile), then score an OSL prediction file against the OSL test ground truth:

```bash
python evaluation/scoring.py \
  --ground-truth data/annotations_test.json \
  --predictions baselines/predictions_test_epoch_final.json
```

The script prints the three metrics as JSON. To also write `scores.json`, pass `--output output`.

## CodaBench scoring

CodaBench provides the OSL ground truth as `input/ref/reference.json` and unpacks the team's OSL prediction file to `input/res/predictions.json`. The scoring program compares those files and writes `output/scores.json`. Only the scoring environment needs the reference file.

The baseline guide includes a ready-to-upload [OSL submission ZIP](../baselines/gar-submission.zip). Submitted code supports reproducibility review under the [rules](../RULES.md).
