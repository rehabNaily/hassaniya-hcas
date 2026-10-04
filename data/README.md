# Data

## What is in this folder
- `hcas_ratings_round1.csv`: first-round H-CAS ratings of 200 randomly drawn texts by two native
  speakers (A1, A2), on three dimensions scored 1-5: `affect`, `cultural`, `linguistic`.
  Columns: `id`, `label` (sentiment label of the source corpus), `CDI_raw` / `CDI_group`
  (Cultural-Dialectal Index of the text), and the six ratings (`affect_A1`, ..., `linguistic_A2`).
  `id` is the value of the `id` column of the source file (or the 0-based row index if the file has no such column).
  **The file contains no corpus text.**

## What is not in this folder
The text of the source corpus is not redistributed here. The ratings can be joined to the texts through `id`.

## Source corpus
HASSANIYA Dataset, first release (file `projectHA_DATASET - VF.csv`; Facebook comments labelled
positive / negative / neutral), licence CC BY 4.0:
El Arby, M. E. M. (2025). Mendeley Data, V1. https://doi.org/10.17632/m2swkr2bhx.1

The notebook was run on a copy of this file hosted on Kaggle (`drrourou/hassaniya-emotion-dataset`).
To reproduce the results, download the file from Mendeley Data and set `CSV_PATH` in the first
cell of the notebook.

A later release, HASSANIYA-DTCD (https://doi.org/10.17632/r5k9ktwr4g.1), also exists. It was not used here.

## Licence of the ratings
CC BY 4.0, compatible with the CC BY 4.0 licence of the source corpus. Please cite the source corpus
(El Arby, 2025) when you use the ratings together with its texts.

## Reproduce the agreement figures
    python scripts/compute_iaa.py
