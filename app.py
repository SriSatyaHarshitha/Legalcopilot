import os
import streamlit as st
from src.qa_module import answer_question
from src.clause_extractor import extract_clauses

st.set_page_config(page_title="LegalCopilot", page_icon="⚖️")
st.title("⚖️ LegalCopilot - Ask Questions & Extract Clauses")

# --- Document Upload or Selection ---
st.sidebar.header("📁 Choose or Upload a Document")

# Allow file upload
uploaded_file = st.sidebar.file_uploader("Upload a .txt legal document", type=["txt"])

# Or select from existing documents
data_folder = "data"
documents = [f for f in os.listdir(data_folder) if f.endswith(".txt")]
selected_file = st.sidebar.selectbox("Or choose from existing:", documents)

# --- Load document content ---
if uploaded_file:
    contract_text = uploaded_file.read().decode("utf-8")
    filename = uploaded_file.name
elif selected_file:
    file_path = os.path.join(data_folder, selected_file)
    with open(file_path, "r") as f:
        contract_text = f.read()
    filename = selected_file
else:
    st.warning("Please upload or select a document to continue.")
    st.stop()

st.subheader(f"📄 Preview: {filename}")
st.text_area("Document Text", contract_text, height=300)

# --- Clause Extraction Section ---
st.markdown("### 🔍 Extract Key Clauses")
if st.checkbox("Extract Confidentiality, Termination, and Governing Law Clauses"):
    with st.spinner("Extracting clauses..."):
        clauses = extract_clauses(contract_text)
    for clause, content in clauses.items():
        st.markdown(f"**{clause}**")
        st.info(content)

# --- Q&A Section ---
st.markdown("### ❓ Ask a Question")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("Type your legal question here:")

if question:
    with st.spinner("Finding the answer..."):
        answer = answer_question(question, contract_text)
    st.success("✅ Answer:")
    st.write(answer)

    # Save to chat history
    st.session_state.chat_history.append(("You", question))
    st.session_state.chat_history.append(("LegalCopilot", answer))

# --- Show Chat History ---
if st.session_state.chat_history:
    st.markdown("### 💬 Conversation History")
    for speaker, message in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {message}")
