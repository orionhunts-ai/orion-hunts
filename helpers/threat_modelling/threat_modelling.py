"""Collection of threats from the adversary to us in which we are threat modelling"""

def calculate_risk_level(rating: str, probability: float) -> str:
    """
    Calculate risk level based on rating and probability.
    """
    rating_scale = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
    rating_score = rating_scale.get(rating, 0)
    # Simplistic risk calculation: (Rating Score * Probability) / 100
    risk_score = (rating_score * probability) / 100

    if risk_score > 2.5:
        return "High Risk"
    elif risk_score > 1.5:
        return "Moderate Risk"
    else:
        return "Low Risk"

def trigger_alert(vector):
    """
    Trigger an alert based on the risk level of an attack vector.
    """
    risk_level = calculate_risk_level(vector["rating"], vector["probability"])
    if risk_level == "High Risk":
        # Placeholder for an actual alert mechanism
        print(f"ALERT: {vector['type']} detected with fingerprint {vector['fingerprint']} is considered {risk_level}. Action required!")
    else:
        print(f"INFO: {vector['type']} detected with fingerprint {vector['fingerprint']} is considered {risk_level}.")

def assess_and_alert(attack_vectors):
    """
    Assess and alert for each provided LLM attack vector.
    """
    for vector in attack_vectors:
        trigger_alert(vector)

def main():
    # Perform the threat assessment and trigger alerts as needed
    assess_and_alert(attack_vectors)

if __name__ == "__main__":
    main()