import torch.nn.functional as F

def contrastive_loss(z1, z2, temperature=0.5):
    """ Computes contrastive loss between two hypergraph views. """
    sim = F.cosine_similarity(z1, z2)
    loss = -torch.log(torch.exp(sim / temperature) / torch.sum(torch.exp(sim / temperature)))
    return loss
