# Kaggle Results

The notebook writes generated artifacts under:

```text
/kaggle/working/cse440-results/
|-- split_manifest.csv
|-- tuning_results.csv
|-- selected_configurations.csv
|-- final_test_results.csv
|-- figures/
|-- histories/
|-- checkpoints/
|-- reports/
`-- predictions/
```

Quick Save after each experiment stage. Download this directory as a backup or create a private Kaggle Dataset named `cse440-project-artifacts` from the notebook output. Attach that dataset before a later session so completed tuning runs and checkpoints can be restored.

Only compact notebook and documentation files belong in GitHub. Generated datasets and checkpoints remain outside the repository.
