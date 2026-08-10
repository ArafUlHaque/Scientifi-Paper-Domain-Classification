# Scientific Paper Domain Classification

CSE440: Natural Language Processing II - Lab Project, Summer 2026

## Project

This project classifies English scientific-paper abstracts into one of seven broad domains using the Web of Science WOS-11967 dataset. The required comparison covers TF-IDF-based traditional models, GloVe-based recurrent neural networks, and BERT Base.

The only model input is the abstract from `X.txt`. The only target is the parent-domain label from `YL1.txt`. Child labels and label-related metadata are never used as features.

Target classes:

1. Computer Science
2. Electrical Engineering
3. Psychology
4. Mechanical Engineering
5. Civil Engineering
6. Medical Science
7. Biochemistry

## Google Colab Workflow

1. Open `notebooks/CSE440_Project.ipynb` in Google Colab.
2. Select a GPU runtime before recurrent or BERT experiments.
3. Mount Google Drive when prompted.
4. Use `/content/drive/MyDrive/CSE440_Project` as the project storage directory.
5. Place WOS-11967 files under `data/WOS-11967/` inside that Drive directory.
6. Run notebook Sections 1-8 and review the pre-training gate before fitting any representation or model.

Large data, GloVe files, histories, and checkpoints stay in Google Drive. GitHub stores the notebook and compact documentation only.

## Required Work

- TF-IDF with Logistic Regression, Multinomial Naive Bayes, and Random Forest
- Pre-trained GloVe with SimpleRNN, GRU, LSTM, and their bidirectional variants
- `bert-base-uncased` with its official tokenizer
- At least three manual configurations for each of the ten required models
- Validation macro-F1 for selection and one final test evaluation per model
- One executed notebook, one 7-8 page ACL-style report, and one 8-12 minute presentation

## Repository Layout

```text
data/          Dataset placement instructions; raw files are not committed
notebooks/     Main Google Colab notebook
results/       Generated artifacts remain in Google Drive
report/        ACL report workspace
presentation/  Recording and viva preparation
```

## Current Milestone

The notebook implements the project through dataset audit, EDA, preprocessing decisions, and frozen split creation. It intentionally stops before TF-IDF fitting, GloVe loading, model construction, or training until the first milestone has been executed and reviewed.

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
