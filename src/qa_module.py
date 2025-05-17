from transformers import pipeline

# Load the QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
