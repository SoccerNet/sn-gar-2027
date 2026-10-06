# Group Activity Recognition challenge rules

📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).

Submissions predict one of the ten SoccerNet-GAR group activity classes for each test clip. Pixel, position, and combined-input methods share **one leaderboard**, ranked by balanced accuracy.

The challenge uses the existing SoccerNet-GAR test split. Although its labels are accessible to approved dataset users, **do not use test examples or labels for training, validation, tuning, or model selection**. Final submissions must include code that reproduces the reported predictions and score without test-set training.

Follow the [dataset access terms](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) and do not redistribute protected video or tracking data. The [evaluation guide](evaluation/README.md) defines the prediction file and scoring metric.
