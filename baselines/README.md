# GAR baseline

The tracking reference from [*Pixels or Positions?*](https://github.com/drishyakarki/pixels_vs_positions) is a GIN + MaxPool model with positional edges. It uses 16 sampled frames per clip from the dataset's `tracking` branch. This is the baseline's input choice; participants may explore the `videos` and `tracking-full` branches and combine available representations. The paper reports **77.8% balanced accuracy** and **57.0% macro F1**, averaged over five runs. The current [OpenSportsLib SN-GAR guide](https://github.com/OpenSportsLab/opensportslib/blob/main/examples/sngar/README.md) reproduces the configuration with the current Hugging Face layout.

This repository includes the trained [epoch-78 checkpoint](best_epoch_78.pt), its [OpenSportsLib test predictions](predictions_test_epoch_final.json), the [challenge-format predictions](predictions.json), and a ready-to-upload [CodaBench submission ZIP](gar-submission.zip). These predictions cover all 13,689 test clips. Using the [challenge evaluator](../evaluation/README.md), they score **78.64% balanced accuracy**, **57.15% macro F1**, and **76.96% accuracy**. The exact values are in [metrics.json](metrics.json).

1. Request access to [OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) and run `hf auth login`.
2. Clone [OpenSportsLib](https://github.com/OpenSportsLab/opensportslib), follow its installation guide, and install `torch-geometric`. The reference configuration requests a GPU.
3. From the OpenSportsLib root, run the paper configuration directly to train:

   ```bash
   python tools/train/train_config.py classification examples/sngar/sngar_tracking_hf.yaml
   ```

   To use a portable cache location **and produce the exact challenge submission ZIP**, run the [baseline runner](run_tracking.py) from the OpenSportsLib root:

   ```bash
   python /path/to/sn-gar-2027/baselines/run_tracking.py --output-dir gar-baseline-output
   ```

The runner pins the tracking dataset revision in the [test manifest](../data/test_manifest.json), trains on `train`, selects the checkpoint on `valid`, infers on `test`, and writes `gar-baseline-output/gar-submission.zip` plus the checkpoint path in `run.json`. To reuse the supplied model without retraining, pass `--checkpoint /path/to/sn-gar-2027/baselines/best_epoch_78.pt`. A GPU is required by the paper configuration; the paper reports approximately four GPU-hours for training. The [rules](../RULES.md) prohibit training or selecting models on the test split.

To run inference directly with OpenSportsLib from its repository root:

```python
from opensportslib.apis import ClassificationModel

model = ClassificationModel(config="examples/sngar/sngar_tracking_hf.yaml")
predictions = model.infer(
    weights="/path/to/sn-gar-2027/baselines/best_epoch_78.pt",
    use_ddp=False,
    use_wandb=False,
)
model.save_predictions("predictions_test_epoch_final.json", predictions)
```

The direct API writes OpenSportsLib JSON. The [runner](run_tracking.py) validates its IDs and converts it to the CodaBench submission format.
