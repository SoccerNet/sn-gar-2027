# SoccerNet Challenge 2027 — Group Activity Recognition (GAR)

📢 **Group Activity Recognition (GAR) Challenge!** 🚀

⏳ **Status:** In preparation — submissions are not open.\
📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).\
👥 **Task leads:** Silvio Giancola\
🤝 **Sponsor:** To be announced

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) · 🗂️ [Data on Hugging Face](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) · 💻 [Baseline](baselines/README.md) · 📚 [Rules](RULES.md) · 📊 [Evaluation](evaluation/README.md) · 🏆 [Evaluation server](https://www.codabench.org/) (task URL TBD)

## Task

Given soccer video pixels, player positions, or both, predict one of the ten SoccerNet-GAR group activity classes for each clip. The challenge compares these representations on **one leaderboard** ranked by balanced accuracy. The task and baseline originate in [*Pixels or Positions? Benchmarking Modalities in Group Activity Recognition*](https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Karki_Pixels_or_Positions_Benchmarking_Modalities_in_Group_Activity_Recognition_CVPRW_2026_paper.html).

## Data

The gated [SoccerNet-GAR dataset](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) provides modality-specific Parquet and WebDataset material for train, valid, and test. Request access, sign in to Hugging Face, and select the relevant `tracking` or `frames` revision. The [split inventory](data/README.md) records what is available and what still needs a stable ID manifest.

The existing **test set is the planned 2027 ranking set**. Its ground truth is already accessible to approved users; this is an honor-system evaluation backed by reproducibility review. Test examples and labels must not be used for training, validation, tuning, or model selection. No separate hidden-label GAR challenge set is currently planned.

## Baseline

The reference method is the GIN + MaxPool + positional-edge tracking model from [Karki et al.](https://github.com/drishyakarki/pixels_vs_positions). [Baseline instructions](baselines/README.md) explain how to obtain the Hugging Face data, run the OpenSportsLib implementation, and reproduce its test metrics. A 2027 prediction file is still pending.

## Evaluation

The [evaluation folder](evaluation/README.md) contains a CodaBench-style scorer that calls **OpenSportsLib's classification metric implementation** and reports balanced accuracy, macro F1, and accuracy. Balanced accuracy determines the single leaderboard. The real test-ID adapter and CodaBench server still need validation.

## Citation

Please cite the GAR benchmark paper in its CVPR Workshops version:

```bibtext
@InProceedings{Karki_2026_CVPR,
  author = {Karki, Drishya and Ramazanova, Merey and Cioppa, Anthony and Giancola, Silvio and Ghanem, Bernard},
  title = {Pixels or Positions? Benchmarking Modalities in Group Activity Recognition},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month = {June},
  year = {2026},
  pages = {9998--10008},
  url = {https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Karki_Pixels_or_Positions_Benchmarking_Modalities_in_Group_Activity_Recognition_CVPRW_2026_paper.html}
}
```

## Updates and support

Each task launches independently when ready. Follow the [challenge website](https://www.soccer-net.org/challenges/2027) and [SoccerNet Discord](https://discord.gg/cPbqf2mAwF) for announcements. Use repository issues for reproducible code problems; do not post access tokens or restricted data.

## Release readiness

| Item | Current state |
| --- | --- |
| Task definition | One leaderboard and balanced accuracy confirmed; modality eligibility and detailed rules pending |
| Data | Gated train/valid/test exist; test reused for ranking; ID manifest pending |
| Baseline | Research method/code available; 2027 predictions pending |
| Evaluation | OpenSportsLib scorer locally tested; real split adapter pending |
| Benchmark | CodaBench server TBD |
| Sponsor | TBD |

This section is for preparation and will be removed when this task is ready for release.
