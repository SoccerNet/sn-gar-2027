# SoccerNet Challenge 2027 — Group Activity Recognition (GAR)

📢 **Group Activity Recognition (GAR) Challenge!** 🚀

📅 **Submission deadline:** April 25, 2027, 23:59 Anywhere on Earth (AoE; UTC−12).\
👥 **Task lead:** Silvio Giancola

🏠 [Challenge website](https://www.soccer-net.org/challenges/2027) · 🗂️ [Data on Hugging Face](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) · 💻 [Baseline](baselines/README.md) · 📚 [Rules](RULES.md) · 📊 [Evaluation server](https://www.codabench.org/competitions/18326/) · 🧮 [Evaluation code](evaluation/README.md)

## Task

Predict one of ten group activity classes for each soccer clip using video pixels, player positions, or both. All modalities share one leaderboard ranked by **balanced accuracy**. The supplied baseline uses 16 sampled frames of player and ball positions from the `tracking` branch; participants are welcome to explore the `videos` and `tracking-full` branches or combine available representations. The task and reference method are described in [*Pixels or Positions? Benchmarking Modalities in Group Activity Recognition*](https://openaccess.thecvf.com/content/CVPR2026W/CVsports/html/Karki_Pixels_or_Positions_Benchmarking_Modalities_in_Group_Activity_Recognition_CVPRW_2026_paper.html).

## Data

The gated [SoccerNet-GAR dataset](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) provides train, valid, and test material. Request access on Hugging Face and choose among the [`tracking`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/tracking), [`frames`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/frames), [`videos`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/videos), and [`tracking-full`](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/tracking-full) branches. The challenge uses the existing test split for ranking. Its labels are accessible to approved dataset users, so final results require reproducible code and compliance with the [no-test-training rule](RULES.md). See the [data guide](data/README.md).

## Baseline

The reference method is the GIN + MaxPool + positional-edge tracking model from [Karki et al.](https://github.com/drishyakarki/pixels_vs_positions). The [baseline guide](baselines/README.md) provides its trained checkpoint, test predictions, submission ZIP, and instructions to reproduce inference with OpenSportsLib. The supplied predictions score **78.64% balanced accuracy** on the challenge test set.

## Evaluation

Submit predictions through the [CodaBench evaluation server](https://www.codabench.org/competitions/18326/). The [evaluation guide](evaluation/README.md) documents the prediction format and scorer. The scorer calls OpenSportsLib's classification metrics and reports balanced accuracy, macro F1, and accuracy; **balanced accuracy** is the ranking metric.

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

## Community

Follow the [SoccerNet challenge website](https://www.soccer-net.org/challenges/2027) and [Discord](https://discord.gg/cPbqf2mAwF) for challenge announcements and discussion.
