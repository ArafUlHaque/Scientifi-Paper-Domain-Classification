# Dataset Storage

The dataset is intentionally not stored in GitHub. Download Web of Science WOS-11967 version 6 manually from:

https://data.mendeley.com/datasets/9rw3vkcfy4/6

Place the extracted files in Google Drive:

```text
MyDrive/CSE440_Project/data/WOS-11967/
|-- X.txt
|-- YL1.txt
|-- YL2.txt
`-- Y.txt
```

- `X.txt` is the only model input.
- `YL1.txt` is the only target.
- `Y.txt` and `YL2.txt` are inspected only to document the child-label discrepancy.
- Do not add raw data, GloVe files, or checkpoints to Git.

The notebook verifies file existence, size, encoding, and SHA-256 hashes before analysis. It never downloads or silently modifies the raw dataset.
