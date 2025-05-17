import os
import streamlit as st
from src.qa_module import answer_question

st.set_page_config(page_title="LegalCopilot", page_icon="⚖️")
st.title("⚖️ LegalCopilot - Ask Questions About Contracts")

# Load available documents
data_folder = "data"
documents = [f for f in os.listdir(data_folder) if f.endswith(".txt")]

selected_file = st.selectbox("Select a legal document:", documents)

# Read file content
file_path = os.path.join(data_folder, selected_file)
with open(file_path, "r") as f:
    contract_text = f.read()

st.text_area("📄 Contract Preview", contract_text, height=300)

question = st.text_input("❓ Ask a question about the contract:")

if question:
    with st.spinner("Analyzing..."):
        answer = answer_question(question, contract_text)
    st.success("✅ Answer:")
    st.write(answer)
