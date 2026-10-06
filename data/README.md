# Split layout

The existing gated [SoccerNet-GAR dataset](https://huggingface.co/datasets/OpenSportsLab/SoccerNet-GAR/tree/main) contains train, valid, and test assets in modality-specific Parquet/WebDataset form. This repository does not copy the protected assets. The [data guide](../docs/data.md) explains access and the cross-modality ID issue.

| Split | Status | Ground truth here? |
| --- | --- | --- |
| [train](train/) | In upstream dataset | No; request upstream access |
| [valid](valid/) | In upstream dataset | No; request upstream access |
| [test](test/) | In upstream dataset; used for 2027 ranking | No; request upstream access |
| [challenge](challenge/) | Submission phase reuses test IDs; separate hidden set not planned now | No additional labels |

Publish a versioned test submission ID manifest after the modality files are aligned. The existing test labels are already upstream; do not copy them into this Git repository or into the participant submission template. Reproducible code and a no-test-training rule are required for final rankings.
