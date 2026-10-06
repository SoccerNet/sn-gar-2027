# GAR baseline

The tracking reference from [*Pixels or Positions?*](https://github.com/drishyakarki/pixels_vs_positions) is a GIN + MaxPool model with positional edges. The paper reports **77.8% balanced accuracy** and **57.0% macro F1**, averaged over five runs. The current [OpenSportsLib SN-GAR guide](https://github.com/OpenSportsLab/opensportslib/blob/main/examples/sngar/README.md) reproduces the configuration with the current Hugging Face layout.

1. Request access to [OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) and run `hf auth login`.
2. Clone [OpenSportsLib](https://github.com/OpenSportsLab/opensportslib), follow its installation guide, and install `torch-geometric`. The reference configuration requests a GPU.
3. From the OpenSportsLib root, use `examples/sngar/sngar_tracking_hf.yaml`, which reads the `tracking` revision. For a local copy, use `tools/download/download_osl_hf.py` and `sngar_tracking_local.yaml` as described in the upstream guide.
4. Train on `train`, select the checkpoint on `valid`, then infer and evaluate on `test`:

   ```python
   from opensportslib.apis import ClassificationModel

   model = ClassificationModel(config="examples/sngar/sngar_tracking_hf.yaml")
   checkpoint = model.train(use_ddp=False, use_wandb=False)
   predictions = model.infer(use_wandb=False)
   metrics = model.evaluate(predictions=predictions, use_wandb=False)
   print(checkpoint, metrics["balanced_accuracy"])
   ```

For submission, convert predictions to the ID/label JSON contract in the [evaluation guide](../evaluation/README.md). The [rules](../RULES.md) prohibit training or selecting models on the test split.
