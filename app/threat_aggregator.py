import json

# Define the top 3 LLM attack vectors as a list of dictionaries
attack_vectors = [
    {
        "type": "Data Poisoning",
        "fingerprint": "LLM-DP-001",
        "rating": "High",
        "probability": 75.0,
    },
    {
        "type": "Model Inversion",
        "fingerprint": "LLM-MI-002",
        "rating": "Medium",
        "probability": 60.0,
    },
    {
        "type": "Adversarial Examples",
        "fingerprint": "LLM-AE-003",
        "rating": "Critical",
        "probability": 80.0,
    },
]

def assess_threats(attack_vectors):
    """
    Assess and print the provided LLM attack vectors.

    :param attack_vectors: A list of dictionaries, each representing an LLM attack vector.
    """
    # Example assessment: print details
    for vector in attack_vectors:
        print(json.dumps(vector, indent=4))

def main():
    # Perform the threat assessment
    assess_threats(attack_vectors)

if __name__ == "__main__":
    main()
