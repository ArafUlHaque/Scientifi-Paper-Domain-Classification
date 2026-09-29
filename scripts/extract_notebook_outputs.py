"""Export presentation artifacts from saved notebook outputs; never train models.

Requires pandas and lxml. Values retain the precision displayed in the notebook.
Run from the repository root: python scripts/extract_notebook_outputs.py
"""

import base64
import hashlib
import io
import json
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks/scientific_paper_domain_classification.ipynb"
OUT = ROOT / "results"


def text(value):
    return "".join(value) if isinstance(value, list) else value


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def main():
    notebook = json.loads(NOTEBOOK.read_text())
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    (OUT / "classification_reports").mkdir(exist_ok=True)
    records = []
    seen = set()

    def save_table(table, name, cell_index, precision):
        table.to_csv(OUT / name, index=False)
        records.append({"file": name, "notebook_cell_index": cell_index,
                        "precision": precision, "source": "saved text/html output"})
        seen.add(name)

    for index, cell in enumerate(notebook["cells"]):
        source = text(cell.get("source", ""))
        current_model = None
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if "text/markdown" in data:
                heading = text(data["text/markdown"]).strip()
                if heading.startswith("### "):
                    current_model = slug(heading[4:])
            if "text/html" in data:
                html = text(data["text/html"])
                if "<table" not in html:
                    continue
                table = pd.read_html(io.StringIO(html), index_col=0)[0]
                columns = set(table.columns)
                if {"accuracy", "macro_f1", "weighted_f1", "model"} <= columns:
                    if "final_test_results.csv" not in seen:
                        save_table(table, "final_test_results.csv", index, "six decimal places")
                elif {"Model", "Configuration", "Hyperparameters"} <= columns:
                    save_table(table, "tuning_results_displayed.csv", index,
                               "percentages and seconds rounded to two decimal places")
                elif {"config_id", "validation_macro_f1", "model"} <= columns and len(table) == 10:
                    save_table(table, "selected_configurations.csv", index, "six decimal places")
                elif {"true_domain", "predicted_domain", "errors"} <= columns:
                    save_table(table, "top_confusion_pairs.csv", index, "integer counts; top ten pairs")
                elif current_model and {"precision", "recall", "f1-score", "support"} <= columns:
                    table.index.name = "label"
                    save_table(table.reset_index(),
                               f"classification_reports/{current_model}.csv", index,
                               "four decimal places")
            if "image/png" in data:
                name = None
                if current_model:
                    name = f"{current_model}_confusion_matrices.png"
                elif 'comparison_path = FIGURES_DIR / "final_model_comparison.png"' in source:
                    name = "final_model_comparison.png"
                if name:
                    (OUT / "figures" / name).write_bytes(base64.b64decode(text(data["image/png"])))
                    records.append({"file": f"figures/{name}", "notebook_cell_index": index,
                                    "source": "saved image/png output; decoded without redrawing"})

    expected = {"final_test_results.csv", "tuning_results_displayed.csv", "selected_configurations.csv"}
    if not expected <= seen:
        raise ValueError(f"Missing notebook result tables: {expected - seen}")
    provenance = {"notebook": str(NOTEBOOK.relative_to(ROOT)),
                  "notebook_sha256": hashlib.sha256(NOTEBOOK.read_bytes()).hexdigest(),
                  "note": "Exports of saved notebook displays, not original full-precision Kaggle CSVs. No models were run.",
                  "artifacts": records}
    (OUT / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(f"Exported {len(records)} saved tables and figures.")


if __name__ == "__main__":
    main()
