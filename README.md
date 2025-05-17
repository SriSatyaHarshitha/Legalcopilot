# ⚖️ LegalCopilot: AI-Powered Legal Document Assistant

LegalCopilot is a smart assistant that helps users extract and query legal contracts using AI. It supports automatic clause extraction and interactive Q&A using pre-trained NLP models. Built in Python with Hugging Face Transformers, it's ideal for legal-tech applications and AI testing portfolios.

## 🚀 Features

- ✅ Extract key legal clauses like Termination, Confidentiality, and Governing Law
- ✅ Ask custom legal questions in real-time via a command-line interface
- ✅ Automatically detects and loads all `.txt` contracts in the `data/` folder
- ✅ Uses `distilbert-base-uncased-distilled-squad` for question answering
- ✅ Well-structured, testable, and internship-ready project layout


## 🗂️ Project Structure
LegalCopilot/
├── data/ # 📁 Input legal documents (in .txt format)
│ ├── sample_contract.txt
│ ├── nda_agreement.txt
│ └── service_agreement.txt

├── src/ # 🧠 Core logic and AI models
│ ├── clause_extractor.py # Clause extraction logic (regex-based)
│ ├── qa_module.py # Question-answering using Hugging Face Transformers
│ └── init.py # Marks the src folder as a package

├── tests/ # 🧪 Unit tests for clause extractor
│ └── test_clause_extractor.py

├── main.py # 💬 Interactive CLI app to select a file and ask questions
├── main_batch.py # 🌀 (Optional) Batch processing of all files with predefined questions
├── README.md # 📄 Project documentation (you’re reading it)
├── requirements.txt # 📦 Python dependencies

## 📥 Example Input

Any legal document in plain `.txt` format, e.g.:

```txt
1. Confidentiality:
The parties agree not to disclose confidential information...

2. Termination:
This agreement shall remain in effect until terminated by either party...

3. Governing Law:
This agreement is governed by the laws of the State of California.

## Usage (Interactive Mode)
Run the interactive assistant:
python3 main.py

Then:
Select a contract file
Ask questions like:
"What does the agreement say about termination?"
"What are the confidentiality obligations?"
"Which law governs this agreement?"
Type exit to quit.

🧪 Running Unit Tests

To validate the clause extraction module:
python3 tests/test_clause_extractor.py

🔧 Installation

Install required packages:
pip install -r requirements.txt

📦 requirements.txt
transformers
torch
You can generate this with:
pip freeze > requirements.txt
👩‍💻 Author

Harshitha Jagadeesh
AI/ML enthusiast with experience in legal-tech, model validation, and intelligent automation. This project showcases NLP-based clause extraction and QA with real-world legal documents.







