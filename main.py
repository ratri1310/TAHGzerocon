from tahg import TextAttributedHypergraph
from prompts import MixtureOfPromptExperts
from vae import VAE
from train import train_vae
import torch

# Load hypergraph
tahg = TextAttributedHypergraph()
mesh_definitions, abstract_data = tahg.load_data_from_csv("mesh.csv", "abstracts.csv")

# Generate prompt-based augmentations
prompt_expert = MixtureOfPromptExperts()
for mesh_code, text in mesh_definitions.items():
    mesh_definitions[mesh_code] = prompt_expert.augment_text(text)

# Train VAE on text embeddings
vae = VAE(input_dim=100, latent_dim=10)
train_vae(vae, torch.randn(100, 100))  # Dummy data

print("Pipeline Complete!")
