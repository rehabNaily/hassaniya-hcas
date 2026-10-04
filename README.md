# H-CAS: evaluating dialectal and cultural competence in Hassaniya Arabic

Code, annotation guide and human ratings accompanying the manuscript
**"Blind Spots of F1 in Hassaniya: A Human-Rated Evaluation of a Lesser-Used Arabic Dialect"**
(in preparation).

> Status: work in progress. Results marked as pending in the manuscript (LLM judge, LLM baseline,
> explainability, second annotation round for *affect*) are **not** in this repository yet.

## What is here
| Path | Content |
|---|---|
| `notebooks/Hassaniya_HCAS_v7.0.ipynb` | End-to-end pipeline: cleaning, Cultural-Dialectal Index (CDI), leakage-free benchmark (TF-IDF, MARBERTv2, CAMeLBERT-DA, AraBERT, CDI-weighted fine-tuning, stacking), test scored once with bootstrap intervals, annotation sample, LLM-judge and XAI blocks (the latter need an API key / human ratings) |
| `data/hcas_ratings_round1.csv` | Round-1 human ratings (ids + ratings, no corpus text) |
| `scripts/compute_iaa.py` | Recomputes weighted kappa, Spearman, exact / within-one agreement and mean offsets |
| `docs/annotation_guide_HCAS.docx` | Guide given to the two annotators |

## Quick start
```bash
git clone https://github.com/rehabNaily/hassaniya-hcas.git
cd hassaniya-hcas
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/compute_iaa.py
```
Expected output (round 1, n = 200): quadratic-weighted kappa 0.061 (affect), 0.305 (cultural),
0.621 (linguistic).

The notebook was developed on Kaggle (GPU). It looks for the corpus under `/kaggle/input`; change
`CSV_PATH` in the first cell to run it elsewhere. Obtain the corpus from its original release (see `data/README.md`).
The LLM-judge and LLM-baseline cells read the key from the environment variable `ANTHROPIC_API_KEY`;
**never write a key in a file.**

## Data and licences
- Code: MIT (see `LICENSE`).
- Human ratings and CDI scores (`data/hcas_ratings_round1.csv`): CC BY 4.0.
- Source corpus: HASSANIYA Dataset (El Arby, 2025, CC BY 4.0), https://doi.org/10.17632/m2swkr2bhx.1.
  It is not redistributed here; the ratings are linked to it through `id`.

## Citation
See `CITATION.cff`.

## Contact
Rehab Naily, National Engineering School of Gabès, riheb.naili@isimg.tn
