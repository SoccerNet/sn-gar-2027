# Data

The gated [OpenSportsLab/SoccerNet-GAR](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR) dataset provides four synchronized inputs for each group activity: `tracking`, `frames`, `videos`, and `tracking-full`. Request dataset access on Hugging Face before downloading any inputs.

The complete OpenSportsLib JSON manifests are provided for [train](annotations_train.json), [validation](annotations_valid.json), and [test](annotations_test.json). Each manifest contains the ground-truth action label and one input reference for each branch. The video and tracking files remain on Hugging Face; this repository only contains their paths in the manifests.

Each sample has the standard OSL fields `id`, `inputs`, `labels`, and `metadata`. Each input uses its OSL type and a path relative to the repository's `data/` directory after downloading that branch into a same-named folder. The `branch` field distinguishes the two `tracking_parquet` inputs. The exact Hugging Face commit for each source branch is recorded in `metadata.hf_sources`.

For example, download each split to a folder named for its branch:

```python
from opensportslib.tools import download_dataset_split_from_hf

for branch in ("tracking", "frames", "videos", "tracking-full"):
    download_dataset_split_from_hf(
        repo_id="OpenSportsLab/SoccerNet-GAR",
        revision=branch,
        split="train",
        output_dir="data",
    )
```

OpenSportsLib places each downloaded split under `data/<branch>/train/`, matching manifest paths such as `tracking/train/clip_000000.parquet`. Replace `train` with `valid` or `test` to download the other splits. The same event IDs and action labels are aligned across all four branches.

The test labels are included because they are available to approved dataset users on Hugging Face. The challenge ranks submissions on this existing test split. Do not train, tune, or select models using test examples or labels; see the [challenge rules](../RULES.md).
