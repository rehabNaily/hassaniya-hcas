# H-CAS: a leakage-free, human-rated evaluation of sentiment models for Hassaniya Arabic

Code, annotation guide, human ratings and results accompanying the manuscript

> **What Macro-F1 Cannot Tell: A Leakage-Free, Human-Rated Evaluation of Sentiment Models for Hassaniya Arabic**
> (submitted to *Language Resources and Evaluation*).

All numbers in the manuscript come from the two notebooks in `notebooks/`, run once on Kaggle. The rating file and the
script in `scripts/` let anyone recompute the inter-annotator agreement on a laptop in a few seconds.

## Repository contents

| Path | Content |
|---|---|
| `notebooks/Hassaniya_HCAS_v7_2.ipynb` | Main analysis: cleaning, Cultural-Dialectal Index (CDI), leakage-free benchmark (TF-IDF, AraBERT, CAMeLBERT-DA, MARBERTv2, CDI-weighted MARBERTv2, stacking; 3 seeds each), test set scored once with bootstrap intervals and paired comparisons, inter-annotator agreement, CDI vs. human ratings, out-of-fold error analysis against the ratings, exploratory attribution and attention |
| `notebooks/Hassaniya_HCAS_v7_2_LLM_open.ipynb` | LLM judge and LLM baseline with open models (Qwen2.5-7B-Instruct, ALLaM-7B-Instruct), run locally; re-uses the frozen outputs of the main notebook |
| `data/hcas_ratings.csv` | Human ratings of the 200 annotated texts, documented format: text id, original label, CDI, ratings of both annotators on the three dimensions, both rounds for affect (no corpus text) |
| `data/hcas_ratings_round2.csv` | The same ratings in the exact file read by the notebooks (SHA-256 `ef77daf3...`, checked by the notebooks); also contains derived columns (means, gaps) |
| `data/data_splits_ids.csv` | Text ids of the train / validation / test splits |
| `data/corpus_cdi_scores.csv` | CDI markers and score of every text of the cleaned corpus (ids only) |
| `results/` | Tables and figures produced by the notebooks (see `results/README.md`) |
| `scripts/compute_iaa.py` | Recomputes the agreement table of the paper from `data/hcas_ratings.csv` |
| `docs/annotation_guide_HCAS_FR.docx` | Annotation guide given to the two annotators (French) |

## Quick start: recompute the agreement

```bash
git clone https://github.com/rehabNaily/hassaniya-hcas.git
cd hassaniya-hcas
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/compute_iaa.py
```

Expected output (n = 200, quadratic weighted kappa): affect 0.061 (round 1) and 0.168 (round 2),
cultural grounding 0.305, linguistic authenticity 0.621.

## Reproducing the full analysis

1. Download the corpus from its original release (see `data/README.md`) and check its SHA-256.
2. On Kaggle, create a notebook from `notebooks/Hassaniya_HCAS_v7_2.ipynb`, add the corpus and `data/hcas_ratings_round2.csv`
   as inputs, select **GPU T4 x2**, enable Internet, and run all cells (about 1 hour). The notebook checks the
   checksums of its inputs and writes every table and figure to `Hassaniya_HCAS_v7_2/`.
3. Create a second notebook from `notebooks/Hassaniya_HCAS_v7_2_LLM_open.ipynb`, add the same inputs plus the output
   of step 2, and run it (GPU T4 x2, about 15 minutes). It needs no API key.

Exact package versions are listed in `results/environment.json` and `results/requirements_frozen.txt`.
GPU training is not bit-for-bit deterministic, so re-running step 2 can change the last decimals of the model scores.

## Data and licences

* Code: MIT (see `LICENSE`).
* Human ratings, CDI scores and split identifiers (`data/`): CC BY 4.0.
* Source corpus: HASSANIYA Dataset (El Arby, 2025, CC BY 4.0), https://doi.org/10.17632/m2swkr2bhx.1.
  It is not redistributed here; the files in `data/` are linked to it through `id`.

## Citation

See `CITATION.cff`.

## Contact

Rehab Naily, National Engineering School of Gabès, riheb.naili@isimg.tn
