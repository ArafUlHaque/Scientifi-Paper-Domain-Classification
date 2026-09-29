# Planned abstract-classification demo

Status: design only. No demo is deployed and model weights are not included in this repository.

## User experience

A visitor pastes an English scientific abstract or chooses a short example, selects BERT or the fast Logistic Regression baseline, and clicks **Classify**. The interface returns the predicted domain and ranked scores for the seven labels. An optional comparison shows both models' predictions and measured inference times for that request.

The page will explain that the model chooses one of seven known fields, that scores are uncalibrated model probabilities, and when BERT truncates a long abstract. Example abstracts will be clearly labeled as examples. The app will not intentionally store submitted text.

## Implementation

- Python with Streamlit for the interface.
- Separate inference functions for BERT and TF-IDF + Logistic Regression.
- Load model artifacts once and reuse them across requests.
- BERT uses the fine-tuned `BERT_3` checkpoint, its saved tokenizer, the exact seven-label mapping, and the original 384-token limit.
- Logistic Regression uses `LR_3.joblib` and the matching fitted `tfidf_vectorizer.joblib`; preserve the notebook's Unicode, lowercasing, and whitespace normalization.
- Handle blank input, very long input, unavailable artifacts, and out-of-vocabulary baseline input explicitly. Never fall back silently to an unfine-tuned BERT classifier.
- Keep a separate, minimal demo dependency file; TensorFlow and training dependencies are unnecessary for these two inference options.

## Artifact request

From `/kaggle/working/cse440-results/` or the restored artifact bundle:

| Artifact | Use |
|---|---|
| `checkpoints/BERT_3/best_model/` (entire folder) | Fine-tuned BERT weights, model configuration, tokenizer files |
| `checkpoints/LR_3.joblib` | Selected baseline model |
| `tfidf_vectorizer.joblib` | Matching fitted vocabulary and IDF weights |
| Original `selected_configurations.csv` | Checkpoint identity and configuration |
| Original `predictions/bert_base.csv` and `predictions/logistic_regression.csv` | Prediction agreement check, together with matching dataset text and split |

The exact paths should be checked against the original selection table. No retraining is needed if the selected checkpoints and preprocessing artifacts are intact. A notebook and its output tables alone cannot perform new inference.

## Hosting

Proposed first deployment: **Streamlit Community Cloud**, connected to this GitHub repository. Its official documentation describes free hosting and GitHub integration: https://docs.streamlit.io/deploy/streamlit-community-cloud (checked 2026-09-29).

Start with the lightweight Logistic Regression option, then test BERT's memory footprint and latency on the actual deployment. If BERT exceeds the chosen host's practical limits, use an appropriately sized inference service or host; do not promise a free BERT deployment before measuring it. Large weights belong in a versioned model artifact store with checksums, not regular source commits.

An alternative is Gradio on Hugging Face Spaces. Current Spaces documentation makes compute-Space creation dependent on account/plan eligibility, so free CPU hosting should not be assumed: https://huggingface.co/docs/hub/spaces-overview (checked 2026-09-29).

## Completion checks

1. Verify class ordering, tokenizer settings, and fitted TF-IDF preprocessing.
2. Compare inference predictions with saved predictions on matching examples before publication.
3. Measure actual cold-start time, warm inference latency, and memory use.
4. Check empty/long-input behavior and readable output on desktop and mobile.
5. Add the working public URL and a screenshot to the repository only after deployment succeeds.
