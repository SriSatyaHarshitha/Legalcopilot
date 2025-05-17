import re

def extract_clauses(text):
    clauses = {
        "Confidentiality": "",
        "Termination": "",
        "Governing Law": ""
    }

    patterns = {
        "Confidentiality": r"(Confidentiality\s*[\s\S]*?)(?=\n\d+\.|\Z)",
        "Termination": r"(Termination\s*[\s\S]*?)(?=\n\d+\.|\Z)",
        "Governing Law": r"(Governing Law\s*[\s\S]*?)(?=\n\d+\.|\Z)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            clauses[key] = match.group(1).strip()

    return clauses
