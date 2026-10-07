# GAR baseline

The tracking reference from [*Pixels or Positions?*](https://github.com/drishyakarki/pixels_vs_positions) is a GIN + MaxPool model with positional edges. The paper reports **77.8% balanced accuracy** and **57.0% macro F1**, averaged over five runs. The current [OpenSportsLib SN-GAR guide](https://github.com/OpenSportsLab/opensportslib/blob/main/examples/sngar/README.md) reproduces the configuration with the current Hugging Face layout.

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

The runner pins the tracking dataset revision in the [test manifest](../data/test_manifest.json), trains on `train`, selects the checkpoint on `valid`, infers on `test`, and writes `gar-baseline-output/gar-submission.zip` plus the checkpoint path in `run.json`. To reuse a trained model, add `--checkpoint /path/to/checkpoint`. A GPU is required by the paper configuration; the paper reports approximately four GPU-hours for training. The [rules](../RULES.md) prohibit training or selecting models on the test split.
