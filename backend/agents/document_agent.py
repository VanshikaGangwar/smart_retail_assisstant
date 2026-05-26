from backend.rag.rag_pipeline import ask_rag

def document_agent(question):

    response = ask_rag(question)

    return response