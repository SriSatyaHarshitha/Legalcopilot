import os
import sys

# ✅ Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.clause_extractor import extract_clauses

# ✅ Run a basic test manually
def run_test():
    sample_path = os.path.join(project_root, "data", "sample_contract.txt")
    with open(sample_path, "r") as f:
        text = f.read()

    clauses = extract_clauses(text)

    assert "Confidentiality" in clauses
    assert "Termination" in clauses
    assert "Governing Law" in clauses

    assert "not to disclose confidential information" in clauses["Confidentiality"]
    assert "terminated by either party" in clauses["Termination"]
    assert "State of California" in clauses["Governing Law"]

    print("✅ Test passed! All clauses were correctly extracted.")

if __name__ == "__main__":
    run_test()
