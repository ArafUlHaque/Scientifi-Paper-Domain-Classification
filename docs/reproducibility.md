# Reproduction and evidence

## What is included

The repository contains the completed Kaggle notebook with saved outputs, the submitted report, presentation exports of result tables and figures, and separately supplied split files. The original notebook's code cells and outputs are preserved; a reading guide and concluding interpretation were added as Markdown cells.

The final-stage notebook loads saved results from an existing artifact bundle. Its outputs report 30 tuning runs, ten final models, ten classification reports, ten confusion matrices, and ten prediction files. The full bundle, raw dataset, embeddings, model checkpoints, and per-document predictions were not supplied with this repository update.

The notebook's saved outputs support the reported scores. This update did not retrain models, recompute predictions, or validate a clean installation. Exported tables retain only the precision displayed in the notebook. See [provenance](../results/provenance.json).

## Recorded environment

| Component | Saved environment output |
|---|---|
| Python | 3.12.13 |
| GPU | Tesla T4; CUDA available in the saved output |
| NumPy | 2.0.2 |
| pandas | 2.3.3 |
| scikit-learn | 1.6.1 |
| TensorFlow | 2.20.0 |
| PyTorch | 2.10.0+cu128 |
| Transformers | 5.0.0 |

These versions describe the displayed final-stage session. They do not prove that all earlier tuning sessions used identical environments. Notebook metadata says GPU disabled, whereas the saved environment output reports a T4; select the appropriate accelerator explicitly when rerunning.

`requirements.txt` records the known package versions and identifies dependencies whose versions were not displayed. It is not a fully locked or clean-install-tested environment. The earlier repository constrained Transformers below 5, which excluded the version in the completed notebook.

## Inspecting results

No setup is needed to read the notebook on GitHub or view the exported results. The ten-model comparison appears in the README. The final test table, complete displayed tuning grid, and per-class reports are under `results/`.

To regenerate presentation exports without training:

```bash
python -m pip install pandas lxml
python scripts/extract_notebook_outputs.py
```

The script reads notebook HTML and embedded PNG outputs. It never executes code cells. `tuning_results_displayed.csv` uses formatted percentage strings and is intentionally named differently from the original training input file.

## Restoring the submitted Kaggle workflow

1. Acquire WOS-11967 v6 and GloVe as described in [data setup](../data/README.md).
2. Attach the complete original experiment artifact bundle, including original result tables, reports, figures, predictions, preprocessing artifacts, and checkpoints.
3. Set `ARTIFACT_INPUT_DIR` to the actual attached bundle. The submitted notebook hard-codes `/kaggle/input/datasets/arafulhaque/cse440-project-artifacts/cse440-results`.
4. Use `ACTIVE_STAGE = "final"` to restore the submitted session. The notebook skips already completed model evaluations and displays saved evidence.
5. Use the bundle's original split manifest. The separate manifest committed here needs compatibility and identity checks described below.

Access to the author's Kaggle artifact dataset has not been verified publicly. A fresh reader needs access to that dataset or an exported bundle.

## Training again

The intended stage order is `audit`, `traditional`, `rnn`, `bert`, then `final`, retaining artifacts between stages. The submitted notebook currently requires an existing artifact directory and completed results near its start, regardless of stage. Consequently, it cannot train from an empty directory merely by changing `ACTIVE_STAGE`.

An independently runnable training version would need to gate restoration/completeness checks by stage, make paths configurable, preserve the same split and label mapping, and verify restored preprocessing artifacts. These are future engineering changes, not changes made to the submitted experiment in this presentation update. Existing results must remain attributed to their original run.

## Split artifact checks

The separately supplied manifest's SHA-256 is:

```text
805b04da648fd01729d17045be8c5d76acfaba4f9cdec207c53bbce4db526476
```

It matches `split_manifest_metadata.json`. It has 11,967 unique document IDs, seven labels in every split, matching aggregate per-class split counts, and no duplicate group crossing partitions.

Its columns are `label_id`, `label_name`, and `duplicate_group_id`; notebook code expects `label`, `domain`, and `duplicate_group`. Do not silently substitute it for the original artifact-bundle manifest. First compare document-to-split assignments and label mappings with the original. The metadata includes hashes for label files but does not include an `X.txt` source hash.

## Small report discrepancies

The original PDF is preserved unchanged. The repository tables follow the saved notebook outputs:

- Bidirectional LSTM test accuracy is displayed as `0.852450`, which formats to **85.24%** at two percentage decimals; the PDF reports 85.25%.
- Random Forest validation accuracy is displayed as `0.901950`. The notebook's detailed formatted tuning table gives **90.19%**, while PDF Table 4 gives 90.20%. Avoid deriving extra precision from displayed decimals near rounding boundaries.
- The rounded per-class BERT report and the six-decimal final table can differ in their last displayed weighted-F1 digit. Use the final table for aggregate summaries; retain provenance and retrieve the original CSV for full precision.

The headline BERT, Bidirectional GRU, and Logistic Regression macro-F1 values agree with the report to two percentage decimal places.

## Interpreting runtime and generalization

Timing boundaries differ: the traditional-model timer includes a validation prediction call, while the neural timers surround training and its validation callbacks. Measurements also depend on hardware/session conditions. They are useful descriptive run times, not a controlled inference-speed comparison.

The project evaluates one fixed split and seed. It does not establish statistical significance, robustness across seeds, deployment latency, or performance on unrelated domains. Model scores are not calibrated confidence estimates.
