# GAR baseline

The reference method is the tracking GIN + MaxPool model with positional edges from [*Pixels or Positions?*](https://github.com/drishyakarki/pixels_vs_positions). It uses 16 sampled frames per clip from the `tracking` branch. Participants may also explore the `videos` and `tracking-full` branches or combine modalities. See the [OpenSportsLib SN-GAR guide](https://github.com/OpenSportsLab/opensportslib/tree/main/examples/sngar) for the reference configuration and model details.

This repository includes the trained [epoch-78 checkpoint](best_epoch_78.pt), its [test predictions](predictions_test_epoch_final.json), the same predictions as [predictions.json](predictions.json), and a ready-to-submit [CodaBench ZIP](gar-submission.zip). Predictions use OpenSportsLib JSON and cover all 13,689 test clips. The supplied checkpoint scores **78.64% balanced accuracy**, **57.15% macro F1**, and **76.96% accuracy** with the [challenge evaluator](../evaluation/README.md); see [metrics.json](metrics.json).

## Reproduce the baseline with OpenSportsLib

Request access to [OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR), then authenticate with Hugging Face. These steps use the `tracking` branch and download the train, validation, and test splits. OpenSportsLib converts each Parquet split to OSL JSON and extracts the referenced tracking files from its TAR shards.

1. Clone and install [OpenSportsLib](https://github.com/OpenSportsLab/opensportslib), then install the graph dependency and authenticate:

   ```bash
   git clone https://github.com/OpenSportsLab/opensportslib.git
   cd opensportslib
   conda create -n osl-gar python=3.12 pip -y
   conda activate osl-gar
   python -m pip install -e .
   opensportslib setup
   python -m pip install torch-geometric
   hf auth login
   ```

2. Download and extract each split using OpenSportsLib's downloader:

   ```bash
   for split in train valid test; do
     python tools/download/download_osl_hf.py \
       --repo-id OpenSportsLab/SoccerNet-GAR \
       --revision tracking \
       --split "$split" \
       --format parquet \
       --output-dir "$PWD/data/sngar"
   done
   ```

   This creates `data/sngar/tracking/{train,valid,test}/` with an OSL JSON annotation file and its extracted tracking inputs in each split directory.

   Note: this dataset contains ~90K samples, unzipping the data can take a few hours.

3. In `examples/sngar/sngar_tracking_local.yaml`, set `DATA.common.data_root` to the absolute path `.../opensportslib/data/sngar/tracking`. Set `SYSTEM.gpu.count` to the number of GPUs to use. Then train from the OpenSportsLib repository root:

   ```bash
   python tools/train/train_config.py classification examples/sngar/sngar_tracking_local.yaml
   ```

   The local configuration trains the GIN + MaxPool model with positional edges, 16 sampled frames, 100 epochs, and seed 42. Training uses the train split and selects the checkpoint using validation data. Do not use the test split for training, tuning, or checkpoint selection; see the [challenge rules](../RULES.md).

4. To export and score test predictions, use the trained validation-selected checkpoint with the OpenSportsLib API from the OpenSportsLib root:

   ```python
   from opensportslib.apis import ClassificationModel

   model = ClassificationModel(config="examples/sngar/sngar_tracking_local.yaml")
   predictions = model.infer(weights="/path/to/best_checkpoint.pt", use_wandb=False)
   model.save_predictions(output_path="predictions.json", predictions=predictions)
   ```

   Compare the resulting OSL prediction file with the OSL test ground truth using the challenge scorer:

   ```bash
   python /path/to/sn-gar-2027/evaluation/scoring.py \
     --ground-truth /path/to/sn-gar-2027/data/annotations_test.json \
     --predictions predictions.json
   ```

The supplied checkpoint is one trained run and may score differently from a new run. Report the test score once after selecting the model on validation data.
