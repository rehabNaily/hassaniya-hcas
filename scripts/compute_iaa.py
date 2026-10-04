"""Reproduce the round-1 inter-annotator agreement from data/hcas_ratings_round1.csv.

Usage:  python scripts/compute_iaa.py [path/to/ratings.csv]
Requires: pandas, scipy, scikit-learn
"""
import sys
import pandas as pd
from scipy.stats import spearmanr
from sklearn.metrics import cohen_kappa_score

path = sys.argv[1] if len(sys.argv) > 1 else "data/hcas_ratings_round1.csv"
df = pd.read_csv(path)
rows = []
for dim in ("affect", "cultural", "linguistic"):
    a, b = df[f"{dim}_A1"], df[f"{dim}_A2"]
    rows.append({
        "dimension": dim,
        "kappa_linear": cohen_kappa_score(a, b, weights="linear"),
        "kappa_quadratic": cohen_kappa_score(a, b, weights="quadratic"),
        "spearman": spearmanr(a, b)[0],
        "exact": (a == b).mean(),
        "within_1": ((a - b).abs() <= 1).mean(),
        "mean_A1": a.mean(),
        "mean_A2": b.mean(),
    })
out = pd.DataFrame(rows).set_index("dimension")
print(f"n = {len(df)} texts")
print(out.round(3).to_string())
