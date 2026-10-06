# SoccerNet Challenge 2027 — Group Activity Recognition

📢 **Group Activity Recognition Challenge!** 🚀

How do pixels and player positions contribute to understanding collective activities in football? Building on SN-GAR, this challenge explores group activity recognition using visual and positional information. Participants will investigate how these complementary representations help interpret the actions of players as a group.

⏳ **Status:** In preparation — submissions are not open.  
📅 **Submission deadline:** April 25, 2027; cutoff time and timezone to be announced.  
👥 **Task lead(s):** Silvio Giancola  
🤝 **Sponsor:** To be announced

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) / 🗂️ [Data](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) / 💻 [Baseline repository](https://github.com/drishyakarki/pixels_vs_positions) / 📚 [Rules](docs/rules.md) / 📊 [Evaluation](evaluation/README.md)

## Task

[Task specification and open decisions](docs/task.md) describes the current scope. This repository will hold the versioned evaluation code and submission instructions for the 2027 challenge. Baselines may live here or in an external repository linked below.

## Data

Access the dataset on [Hugging Face](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR). Follow its access conditions and download instructions.

The existing release stores modality-specific Parquet and WebDataset assets. See [the data guide](docs/data.md) and [split layout](data/README.md). The organizers plan to rank on the existing **test split**, whose labels are already available to approved dataset users. Participants must publish reproducible code and must not train on that split.

## Baseline

External SN-GAR baseline: Pixels or Positions? Benchmarking Modalities in Group Activity Recognition. Follow the upstream installation and training instructions. Challenge compatibility and a pinned release are still to be validated.

See [baseline instructions](baselines/README.md). Existing research baselines must be checked against the final challenge format before their scores are advertised as 2027 reference results.

## Evaluation

Balanced accuracy is the selected ranking metric on **one leaderboard**. The local scorer uses OpenSportsLib, but the 2027 reference split and CodaBench server still need to be frozen and tested.

See [evaluation instructions](evaluation/README.md) for current code, submission formats and remaining decisions. CodaBench test and challenge links will be added after the servers have been validated.

## Release readiness

| Item | Current state |
| --- | --- |
| Task definition | Draft rules; one leaderboard and balanced accuracy confirmed |
| Data and splits | Existing gated SN-GAR train/valid/test; test reused for ranking; stable submission IDs pending |
| Baseline | Research code available; 2027 prediction files pending |
| Evaluation | OpenSportsLib scorer locally tested; real adapter pending |
| Benchmark | CodaBench server pending |
| Sponsor | Not confirmed |

Each task launches independently after its rules, data, baseline, evaluator and benchmark are verified. See the [task specification](docs/task.md) for remaining technical decisions.

## Getting started

1. Read the [task specification](docs/task.md) and [draft rules](docs/rules.md).
2. Follow the [data access guide](docs/data.md).
3. Consult the [baseline instructions](baselines/README.md).
4. Check the [evaluation status](evaluation/README.md) before generating submissions.

## Updates and support

Each task launches independently once ready. Follow the [challenge website](https://www.soccer-net.org/challenges/2027) and [SoccerNet Discord](https://discord.gg/cPbqf2mAwF). Use repository issues for reproducible code problems; do not post access tokens, restricted data or private labels.

## Citation and licensing

Please cite [Karki et al., *Pixels or Positions?*, CVPR Workshops 2026](https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Karki_Pixels_or_Positions_Benchmarking_Modalities_in_Group_Activity_Recognition_CVPRW_2026_paper.html) when using SoccerNet-GAR. Use `\cite{Karki_2026_CVPR}` in LaTeX; its conference BibTeX is in [CITATION.bib](CITATION.bib). The 2027 challenge citation and repository code license will be confirmed before release. Dataset access terms and external baseline licenses apply independently.
