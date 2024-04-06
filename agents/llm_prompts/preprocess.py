"""
Pre-process steps for data.

"""

template = """GENERAL INSTRUCTIONS
Your task is to answer questions. If you cannot answer the question, request a helper or use a tool. Fill with Nil where no tool or helper is required.
 
AVAILABLE TOOLS
- Search Tool
- Math Tool
 
AVAILABLE HELPERS
- Decomposition: Breaks Complex Questions down into simpler subparts
 
CONTEXTUAL INFORMATION
<No previous questions asked>
 
QUESTION
How much did the revenue grow between Q1 of 2024 and Q2 of 2024?
 
ANSWER FORMAT
{"Tool_Request": "<Fill>", "Helper_Request "<Fill>"}"""
