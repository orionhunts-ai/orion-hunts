    """
    A PyTorch implementation of an RL approach focusing on being environment agnostic
    and flexible. Adaptors can be built by the community.
    
    """
    
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size),
            nn.Softmax(dim=-1),
        )
    
    def forward(self, x):
        return self.network(x)

def update_policy(policy_network, optimizer, rewards, log_probs):
    discounted_rewards = []
    R = 0
    for r in rewards[::-1]:
        R = r + 0.99 * R
        discounted_rewards.insert(0, R)
    
    discounted_rewards = torch.tensor(discounted_rewards)
    discounted_rewards = (discounted_rewards - discounted_rewards.mean()) / (discounted_rewards.std() + 1e-9)  # Normalize
    
    policy_gradient = []
    for log_prob, reward in zip(log_probs, discounted_rewards):
        policy_gradient.append(-log_prob * reward)
    
    optimizer.zero_grad()
    policy_loss = torch.stack(policy_gradient).sum()
    policy_loss.backward()
    optimizer.step()
