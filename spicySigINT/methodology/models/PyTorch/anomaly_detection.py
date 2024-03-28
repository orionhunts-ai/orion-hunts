import torch.nn as nn
import torch

class NetworkAnomalyDetector(nn.Module):
    def __init__(self, input_features):
        super(NetworkAnomalyDetector, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_features, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid(),
        )
    
    def forward(self, x):
        return self.network(x)

# Assuming network_traffic_data is a tensor representing the network traffic features
network_traffic_data = torch.randn(1, 10)  # Example tensor
model = NetworkAnomalyDetector(input_features=10)
prediction = model(network_traffic_data)
print(f"Anomaly Score: {prediction.item()}")
