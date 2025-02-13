# Text-Attributed Hypergraph Learning (TAHG)

This repository implements **Text-Attributed Hypergraph Learning (TAHG)** for **zero-shot multi-label text classification (ZMTC)** in biomedical domains. It constructs a **hypergraph-based representation** where nodes correspond to MeSH terms, hyperedges represent PubMed abstracts, and text attributes provide enriched semantic information. The framework integrates **Mixture-of-Prompt-Experts**, **VAE-based augmentation**, and **contrastive learning** to enhance classification performance.

---

##  Features
- **Text-Attributed Hypergraph (TAHG)** construction from **MeSH codes and PubMed abstracts**.
- **Mixture-of-Prompt-Experts (MoP)** using LLMs for **semantic perturbations**.
- **Variational Autoencoder (VAE)** for controlled augmentation of text attributes.
- **Contrastive Learning** for **better generalization on unseen labels**.
- **Fully modular design** with separate implementations for each step.

---

---

##  Installation & Execution

```sh
cd tahg_project
pip install -r requirements.txt

cd tahg_project
Install dependencies
pip install -r requirements.txt
Run Full Pipeline
Execute the entire process end-to-end:
python main.py

---

---
## Acknowledgments
We would like to thank the authors of [[GAugLLM]](https://arxiv.org/abs/2406.11945) for providing part of the LLM-based code that contributed to this implementation. 
 
# TAHGzerocon
