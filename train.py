import torch.optim as optim

def train_vae(vae, data, epochs=10):
    optimizer = optim.Adam(vae.parameters(), lr=0.001)
    loss_fn = nn.MSELoss()

    for epoch in range(epochs):
        optimizer.zero_grad()
        recon, mu, log_var = vae(data)
        loss = loss_fn(recon, data)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")
