# Saved experimental evidence

The CSV files here were extracted from the completed notebook's saved HTML tables. They preserve the displayed precision and should not be mistaken for original full-precision Kaggle artifacts.

| File | Contents | Precision |
|---|---|---|
| `final_test_results.csv` | Ten selected models on the test set | Six decimal places |
| `selected_configurations.csv` | Selected configuration and validation scores per model | Six decimal places |
| `tuning_results_displayed.csv` | All 30 configurations and full hyperparameter descriptions | Percentages/time rounded to two decimals |
| `classification_reports/*.csv` | Ten per-class reports | Four decimal places |
| `top_confusion_pairs.csv` | Ten most frequent BERT error pairs | Integer counts |
| `provenance.json` | Source notebook hash, cell indices, extraction details | Exact provenance |

The confusion matrices and model-comparison PNG are decoded directly from notebook image outputs. The three EDA PNG files (`class_distribution.png`, `class_wordclouds.png`, `text_length_analysis.png`) were supplied separately by the project author.

To regenerate extracted files from the repository root:

```bash
python -m pip install pandas lxml
python scripts/extract_notebook_outputs.py
```

The extraction script does not execute notebook code. These presentation exports do not replace the complete Kaggle bundle, which also contains original CSVs, checkpoints, tokenizers, and prediction files. In particular, do not use the rounded tuning table as an input for model selection or checkpoint restoration.
