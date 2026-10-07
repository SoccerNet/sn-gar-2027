# Data

[OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) provides train, valid, and test data in modality-specific Parquet and WebDataset formats. Request access with your Hugging Face account. The tracking data uses the `tracking` revision; video frames use the `frames` revision.

The 2027 challenge evaluates the existing test split. The [test manifest](test_manifest.json) lists its **13,689 sample IDs** in submission order and the ten valid class names, without labels. The manifest pins the tracking and frames dataset revisions. Each ID is present in both modalities; predictions may be submitted in any order.

Approved users can access test labels upstream, so the [rules](../RULES.md) prohibit using that split for training or model selection. Dataset assets are not mirrored in this repository.
