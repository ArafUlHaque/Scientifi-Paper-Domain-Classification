# Kaggle Input Dataset

Create one private Kaggle Dataset named `cse440-wos11967-assets`:

```text
cse440-wos11967-assets/
|-- WOS-11967/
|   |-- X.txt
|   |-- YL1.txt
|   |-- YL2.txt
|   `-- Y.txt
`-- glove.6B.100d.txt
```

Download WOS-11967 version 6 from:

https://data.mendeley.com/datasets/9rw3vkcfy4/6

Download `glove.6B.100d.txt` from the official Stanford GloVe 6B release.

The notebook expects:

```text
/kaggle/input/cse440-wos11967-assets/WOS-11967/X.txt
/kaggle/input/cse440-wos11967-assets/WOS-11967/YL1.txt
/kaggle/input/cse440-wos11967-assets/glove.6B.100d.txt
```

`X.txt` is the only model input. `YL1.txt` is the only target. `Y.txt`, `YL2.txt`, and metadata are excluded to prevent target leakage.
