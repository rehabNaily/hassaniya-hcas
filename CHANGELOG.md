# Changelog

## v1.0 (submission version)
* Replaces notebook v7.0 by v7.2. Corrections: identical loss for all transformer runs; three seeds for the
  CDI-weighted variants; stacking selected on a cross-validated validation score; augmentation no longer inserts the
  letter gaf and copies inherit the CDI of their source; best checkpoint reloaded correctly under Transformers 5;
  all test candidates, confusion matrix and CDI-group results reported; out-of-fold error analysis; single,
  pre-declared definition of H-CAS_human.
* Adds the LLM notebook (open models, no API key needed).
* Ratings file now contains both rounds for affect (`data/hcas_ratings.csv` replaces `data/hcas_ratings_round1.csv`).
* `scripts/compute_iaa.py` now also reports the 95% CI of the quadratic kappa and Krippendorff's ordinal alpha.
