# Dataset README

## Overview

This repository uses biomedical literature datasets derived from the PubMed to three domain-specific subsets (Neurology, Immunology, Embryology). All datasets use MeSH (Medical Subject Headings) labels for multi-label text classification.

---

## Data Sources

- **Source:** [BioASQ Task A](http://www.bioasq.org/)
- **Raw file:** `allMeSH_2022.json` — full PubMed corpus with MeSH annotations (16.2M articles)
- **We use:** Articles from years 2019–2021 (1,521,250 articles)
- **Download:** Register and download from the BioASQ website: http://www.bioasq.org/

### Domain Datasets (Neurology, Immunology, Embryology)
- Derived from the BioASQ corpus by filtering articles whose MeSH labels belong to domain-specific concept sets


---

Split ratio: 70% train / 10% val / 20% test (random split, seed=42)

---

## How to Reproduce the BioASQ Dataset

### Step 1 — Download the raw data
Register at http://www.bioasq.org/ and download:
- `allMeSH_2022.json` — the full PubMed corpus with MeSH annotations

### Step 2 — PMIDs for each Dataset are shared here. 


### Step 3 — Build the GZSL splits
```bash
python prepare_gzsl_splits_bioasq.py \
    --json_path  /path/to/allMeSH_2022_clean.json \
    --output_dir  splits/bioasq \ (Change to dataset names)
    --label_mode  unique_id \
    --seed        42 \
    --domain      bioasq \
    --overwrite
```





## Label Format

All datasets use MeSH **Unique IDs** as labels (e.g., `D006801`, `D005260`).
The full MeSH code list with headings and tree numbers is available at:
https://www.nlm.nih.gov/mesh/

---


