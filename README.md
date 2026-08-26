# Scientific Paper Domain Classification

CSE440: Natural Language Processing II - Lab Project, Summer 2026

## Project

This project classifies English scientific-paper abstracts into seven parent domains using Web of Science WOS-11967. It compares the ten models required by the course guideline:

- TF-IDF with Logistic Regression, Multinomial Naive Bayes, and Random Forest
- GloVe with SimpleRNN, GRU, LSTM, and their bidirectional variants
- BERT Base using `bert-base-uncased`

`X.txt` is the only model input and `YL1.txt` is the only target. Child labels and metadata are excluded from model features.

## Kaggle Workflow

1. Create a private Kaggle Dataset named `cse440-wos11967-assets` using the layout in `data/README.md`.
2. Attach that dataset to `notebooks/CSE440_Project.ipynb`.
3. Enable Internet when downloading `bert-base-uncased`, or attach the model as a Kaggle Model input.
4. Select the notebook stage: `audit`, `traditional`, `rnn`, `bert`, or `final`.
5. Run the relevant cells and Quick Save after each stage.
6. Back up `/kaggle/working/cse440-results` and attach it as `cse440-project-artifacts` when resuming in another session.

The notebook uses seed 42 and one frozen 70/15/15 split. Validation macro-F1 selects each model's best manual configuration. Test evaluation occurs only during the final stage.

## Required Experiments

- 3 traditional models x 3 configurations = 9 runs
- 6 recurrent models x 3 configurations = 18 runs
- 1 BERT model x 3 configurations = 3 runs
- Total = 30 official tuning runs

Bonus models, ensembles, ablations, deployment, and benchmark work are intentionally postponed.

## Repository Layout

```text
data/          Kaggle input instructions
notebooks/     Single canonical Kaggle notebook
results/       Generated-artifact documentation
report/        ACL report preparation
presentation/  Three-member presentation and viva preparation
```

## Dataset

- Web of Science WOS-11967, version 6
- Source: https://data.mendeley.com/datasets/9rw3vkcfy4/6
- DOI: `10.17632/9rw3vkcfy4/6`
- Licence: CC BY 4.0

## Submission Metadata

- Group number: pending
- Section: pending
- Member names and IDs: pending
- Deadline: pending
