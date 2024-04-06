from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class ThreatIntelligenceNLP:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
    
    def analyze_report(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        outputs = self.model(**inputs)
        predictions = torch.softmax(outputs.logits, dim=-1)
        threat_level = torch.argmax(predictions, dim=-1)
        return threat_level.item()

# Example usage:
nlp_analyzer = ThreatIntelligenceNLP()
report = "New ransomware variant discovered targeting healthcare institutions."
threat_level = nlp_analyzer.analyze_report(report)
print(f"Threat Level: {threat_level}")
