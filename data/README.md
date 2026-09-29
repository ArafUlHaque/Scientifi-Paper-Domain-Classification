# Dataset and inputs

The study uses **WOS-11967**, version 6: 11,967 abstracts in seven parent domains.

- [Web of Science dataset on Mendeley Data](https://data.mendeley.com/datasets/9rw3vkcfy4/6)
- DOI: `10.17632/9rw3vkcfy4.6`
- Dataset license: CC BY 4.0, as documented in the submitted report
- [GloVe 6B vectors from Stanford](https://nlp.stanford.edu/projects/glove/): use `glove.6B.100d.txt`

Supply exactly one `WOS-11967/X.txt` under `/kaggle/input`. The notebook discovers its parent folder automatically. The input layout is:

| Relative path | Purpose |
|---|---|
| `WOS-11967/X.txt` | Abstract text |
| `WOS-11967/YL1.txt` | Parent-domain target |
| `glove.6B.100d.txt` | Pretrained GloVe vectors, alongside the WOS-11967 folder |

`Y.txt` and `YL2.txt` are not model inputs. Raw data and downloaded embeddings are excluded from Git history.

The completed notebook also requires a saved experiment bundle at `/kaggle/input/datasets/arafulhaque/cse440-project-artifacts/cse440-results`. Public access to that bundle has not been verified. See [reproduction notes](../docs/reproducibility.md) before running it.

## Supplied split artifacts

`splits/split_manifest.csv` and `splits/split_manifest_metadata.json` are the author's separately supplied files. Their SHA-256 checksum agrees, and the manifest contains 11,967 unique document IDs. Split sizes are 8,376/1,795/1,796. No duplicate group crosses a partition.

**Compatibility:** the supplied CSV names its columns `label_id`, `label_name`, and `duplicate_group_id`; the notebook expects `label`, `domain`, and `duplicate_group`. It is preserved unchanged for traceability. Matching aggregate counts alone does not prove that it is the exact manifest used for the displayed model scores. Compare it against the manifest inside the original Kaggle artifact bundle before using it to reproduce those scores.
