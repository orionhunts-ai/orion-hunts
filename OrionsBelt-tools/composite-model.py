    """A composite model including anomaly detection and signature detection
    
    Including with an example of training and inference
    """
    # Model Architecture 
    
    class CompositeModel(nn.Module):
    def __init__(self, anomaly_model, signature_model):
        super(CompositeModel, self).__init__()
        self.anomaly_model = anomaly_model
        self.signature_model = signature_model
        
        # Fusion layer to combine outputs from both models
        self.fusion = nn.Sequential(
            nn.Linear(2, 1),
            nn.Sigmoid()
        )
        
    def forward(self, x1, x2):
        anomaly_output = self.anomaly_model(x1)
        signature_output = self.signature_model(x2)
        
        # Concatenate outputs and pass through the fusion layer
        combined_output = torch.cat((anomaly_output, signature_output), dim=1)
        final_output = self.fusion(combined_output)
        return final_output
    
# Train model

def train_model(model, dataloaders, criterion, optimizer, num_epochs=25):
    for epoch in range(num_epochs):
        # Iterate over data.
        for inputs1, inputs2, labels in dataloaders['train']:
            outputs = model(inputs1, inputs2)
            loss = criterion(outputs, labels)
            
            # Zero the parameter gradients
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
        print(f'Epoch {epoch}/{num_epochs}, Loss: {loss.item()}')
    
    return model


