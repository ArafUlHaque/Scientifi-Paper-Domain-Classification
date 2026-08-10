# Results Storage

Generated results are saved in Google Drive under `MyDrive/CSE440_Project/results/` so Colab sessions can resume safely.

Expected files and folders:

- `split_manifest.csv`: frozen document IDs, labels, and split assignments
- `tuning_results.csv`: every official and failed tuning run
- `final_test_results.csv`: one locked test evaluation per required model
- `figures/`: report-ready visualizations
- `histories/`: compact neural training histories
- `checkpoints/`: best neural checkpoints

Large generated artifacts are not committed to GitHub.
