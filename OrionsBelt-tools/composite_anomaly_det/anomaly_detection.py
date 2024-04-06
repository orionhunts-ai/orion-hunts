import torch
import torch.nn as nn
from torchvision import models

class AnomalyDetectionModel(nn.Module):
    def __init__(self):
        super(AnomalyDetectionModel, self).__init__()
        # Utilize a pre-trained ResNet, removing the final layer
        # Any pretrained model can be used
        # Eg. the cybersecurity threat dataset;
        
        base_model = models.resnet50(pretrained=True)
        self.features = nn.Sequential(*list(base_model.children())[:-1])
        
        # Additional layers for anomaly detection
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
