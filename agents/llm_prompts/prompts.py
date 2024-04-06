SYSTEM_PROMPTS = [
    "Identify heuristics of zero-day exploits in AI systems. {Metric: Number of unique zero-day exploits identified}",
    "Detect signatures of known ransomware affecting AI data repositories. {Metric: Accuracy in correctly identifying ransomware signatures}",
    "Analyze network traffic for fingerprints of APT groups targeting AI infrastructure. {Metric: Detection rate of APT group activities}",
    "Catalogue behavioral patterns indicating botnet attacks on AI-driven applications. {Metric: Coverage of identified botnet attack vectors}",
    "Evaluate AI model robustness against adversarial machine learning attacks. {Metric: Percentage of vulnerabilities mitigated}"
]

PLANNING_PROMPTS = [
    "Devise a strategy for real-time monitoring of AI systems for zero-day exploit detection. {Metric: Response time to detection}",
    "Outline a response plan for AI systems compromised by ransomware. {Metric: Recovery time post-attack}",
    "Plan a cybersecurity awareness program focusing on APT group tactics against AI. {Metric: Reduction in successful APT intrusions}",
    "Design a security protocol for protecting AI-driven applications from botnet attacks. {Metric: Decrease in botnet attack surface}",
    "Prepare an upgrade path for AI models to reinforce against adversarial attacks. {Metric: Reduction in exploitable vulnerabilities}",
    "Establish a continuous integration/continuous deployment (CI/CD) pipeline for rapid deployment of security patches. {Metric: Deployment latency}",
    "Develop an incident response drill schedule for AI system cyber threats. {Metric: Team response efficiency}",
    "Construct a threat intelligence sharing mechanism with other AI-driven organizations. {Metric: Increase in preemptive threat mitigations}",
    "Formulate a data encryption strategy for at-rest and in-transit AI model data. {Metric: Percentage of data secured}",
    "Initiate a research team focused on emerging threats in AI cybersecurity. {Metric: Number of research findings published annually}"
]

ACTION_PROMPTS = [
    "Implement a firewall rule to block known malicious IPs targeting the AI infrastructure. {Metric: Reduction in intrusion attempts}",
    "Deploy an AI model update to improve detection of adversarial inputs. {Metric: Improvement in detection rates}",
    "Execute a simulated ransomware attack on a non-production AI system to test resilience. {Metric: System recovery success rate}",
    "Configure network anomaly detection systems for early identification of botnet behavior. {Metric: Detection accuracy rate}",
    "Apply latest security patches to AI systems and dependencies. {Metric: Time taken to patch vulnerabilities}",
    "Integrate an automated alert system for unusual AI system access patterns. {Metric: Alert precision rate}",
    "Perform a vulnerability assessment on AI infrastructure using updated threat databases. {Metric: Number of vulnerabilities discovered}",
    "Conduct a training session on secure coding practices for AI application developers. {Metric: Post-training attack mitigation effectiveness}",
    "Upgrade encryption protocols for AI data storage and processing units. {Metric: Compliance with industry encryption standards}",
    "Roll out a two-factor authentication (2FA) system for accessing critical AI systems. {Metric: Reduction in unauthorized access incidents}"
]

RATING_PROMPTS = [
    "Rate the effectiveness of the newly implemented AI system zero-day exploit detection mechanism. {Metric: Detection success rate}",
    "Evaluate the organization's preparedness and response to a simulated ransomware attack on AI systems. {Metric: Post-attack recovery time}",
    "Assess the impact of cybersecurity awareness training on preventing APT group intrusions. {Metric: Employee awareness level improvement}"
]
