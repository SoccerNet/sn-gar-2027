# Group Activity Recognition challenge rules

📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).

Submissions predict one of the ten SoccerNet-GAR group activity classes for each test clip. Pixel, position, and combined-input methods share **one leaderboard**, ranked by balanced accuracy.

Each team may submit up to **five times per day**. A team's best valid submission appears on the leaderboard. Equal balanced-accuracy scores share the same rank.

Any external training data, pretrained model, and local or remote model/API service may be used, provided every resource is fully disclosed. External datasets, model weights, and model/API implementations must be publicly available under open licenses, with the code and configuration needed to reproduce the submitted predictions. Teams must report the source URLs, licenses, versions or revisions, checkpoints, prompts where applicable, and inference settings. Closed-source or API-only systems that cannot be independently reproduced are not eligible. There is no modality-specific eligibility restriction or separate modality track.

The challenge uses the existing SoccerNet-GAR test split. Although its labels are accessible to approved dataset users, **do not use test examples or labels for training, validation, tuning, or model selection**. Final submissions must include code that reproduces the reported predictions and score without test-set training.

Follow the [dataset access terms](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) and do not redistribute protected video or tracking data. The no-test-training rule applies even if test examples appear in an external source. The [evaluation guide](evaluation/README.md) defines the prediction file and scoring metric.
