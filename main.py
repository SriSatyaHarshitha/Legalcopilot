import os
from src.qa_module import answer_question

# Step 1: List available legal documents
data_folder = "data"
documents = [f for f in os.listdir(data_folder) if f.endswith(".txt")]

if not documents:
    print("No .txt files found in the data/ folder.")
    exit()

print("📁 Available legal documents:")
for i, doc in enumerate(documents):
    print(f"{i + 1}. {doc}")

# Step 2: Let user choose a file
choice = input("\nEnter the number of the document you want to query: ")
try:
    index = int(choice) - 1
    if index < 0 or index >= len(documents):
        raise ValueError
    selected_file = documents[index]
except ValueError:
    print("❌ Invalid selection.")
    exit()

# Step 3: Read the selected document
file_path = os.path.join(data_folder, selected_file)
with open(file_path, "r") as f:
    context = f.read()

print(f"\n📄 You selected: {selected_file}")

# Step 4: Ask questions interactively
print("\n🔍 Ask your legal question (type 'exit' to quit):\n")

while True:
    question = input("❓ Your Question: ")
    if question.lower() == "exit":
        print("👋 Exiting LegalCopilot. Bye!")
        break
    answer = answer_question(question, context)
    print(f"✅ Answer: {answer}\n")
