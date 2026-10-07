# Data

[OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) provides train, valid, and test data. Request access with your Hugging Face account. The supplied baseline uses 16 sampled frames per clip from the [`tracking`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/tracking) branch. Participants may also use the [`frames`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/frames), [`videos`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/videos), and [`tracking-full`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/tracking-full) branches, alone or in combination. See the [dataset card](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) for access and branch documentation.

The 2027 challenge evaluates the existing test split. The [test manifest](test_manifest.json) lists its **13,689 sample IDs** in submission order and the ten valid class names, without labels. The manifest pins the tracking and frames dataset revisions. Each ID is present in both modalities; predictions may be submitted in any order.

Approved users can access test labels upstream, so the [rules](../RULES.md) prohibit using that split for training or model selection. Dataset assets are not mirrored in this repository.
