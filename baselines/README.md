# Baseline

The reference is [*Pixels or Positions?*](https://github.com/drishyakarki/pixels_vs_positions). Its GIN + MaxPool + positional-edge tracking model is the published balanced-accuracy baseline. The paper reports **77.8% balanced accuracy averaged over five runs**; an individual run can differ. The current [OpenSportsLib SN-GAR example](https://github.com/OpenSportsLab/opensportslib/blob/main/examples/sngar/README.md) reproduces that configuration using the current Hugging Face layout.

Repository: [https://github.com/drishyakarki/pixels_vs_positions](https://github.com/drishyakarki/pixels_vs_positions).

1. Request access to [OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) and run `hf auth login`.
2. Clone [OpenSportsLib](https://github.com/OpenSportsLab/opensportslib), follow its installation guide, and install `torch-geometric`. The paper configuration requests a GPU.
3. From the OpenSportsLib root, use `examples/sngar/sngar_tracking_hf.yaml`, which reads the `tracking` revision. Alternatively download each split with `python tools/download/download_osl_hf.py --repo-id OpenSportsLab/SoccerNet-GAR --revision tracking --split <train|valid|test> --output-dir ./sngar-data` and use `sngar_tracking_local.yaml`.
4. From that root, run this training and inference sequence, which selects a checkpoint on validation before test inference:

   ```python
   from opensportslib.apis import ClassificationModel

   model = ClassificationModel(config="examples/sngar/sngar_tracking_hf.yaml")
   checkpoint = model.train(use_ddp=False, use_wandb=False)
   predictions = model.infer(use_wandb=False)
   metrics = model.evaluate(predictions=predictions, use_wandb=False)
   print(checkpoint, metrics["balanced_accuracy"])
   ```

Convert the resulting test predictions to the ID/label contract in the [evaluation guide](../evaluation/README.md). The stable cross-modality test ID manifest is pending. Pin the package and data revisions for a 2027 run.

The 2027 test-set baseline prediction file is **TBD**. When supplied, commit a versioned prediction file (IDs and labels, without protected frames or tracking data), its producing code commit and inference command, and the score from [the OpenSportsLib scorer](../evaluation/README.md). Do not train or tune on the test split used for ranking.

Before release, record the tested commit, environment, weights, inference command, output conversion, score, and compute requirements. External code remains in its upstream repository under its own license.
