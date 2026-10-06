# Data

Dataset: [https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR).

Request access and follow the dataset card’s conditions. This repository does not redistribute the dataset.

The gated [dataset repository](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/main) contains modality-specific Parquet and WebDataset assets for pixels/frames and positions/tracking, with train, valid and test material. Use the dataset card and OpenSportsLib readers for the current layout; older baseline instructions may describe legacy ZIPs. The exact sample-ID mapping across modality files must be checked before publishing a single-leaderboard submission manifest.

For 2027, the organizers plan to use the **existing test split** for final ranking. Its labels are available to approved dataset users, so this is an honor-system benchmark backed by reproducibility review, not a hidden-label challenge. Participants must not use test samples or labels for training, validation, tuning, or model selection. The final rules must specify the code, checkpoints, training logs, and inference command required to verify that a submitted score can be reproduced. The stable test ID manifest and baseline prediction files are pending.

See [the explicit split layout](../data/README.md).

## Release requirements

Before opening submissions, freeze the release version, stable sample IDs, split boundaries and public versus private fields. Verify that final-ranking labels have not already been released. Keep ground truth outside public Git history.
