import os

from dotenv import load_dotenv
from openai import AzureOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

_client = None
_embeddings = None
_vectorstore = None


def get_openai_client():
    global _client

    if _client is None:
        api_key = os.getenv("FOUNDARY_API_KEY")
        endpoint = os.getenv("FOUNDARY_ENDPOINT")
        api_version = os.getenv("FOUNDARY_API_VERSION", "2024-05-01-preview")

        if not api_key or not endpoint:
            raise RuntimeError(
                "FOUNDARY_API_KEY and FOUNDARY_ENDPOINT must be configured"
            )

        _client = AzureOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=endpoint
        )

    return _client


def get_embeddings():
    global _embeddings

    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name=os.getenv(
                "EMBEDDING_MODEL",
                "sentence-transformers/all-MiniLM-L6-v2"
            )
        )

    return _embeddings


def get_vectorstore():
    global _vectorstore

    if _vectorstore is None:
        _vectorstore = FAISS.load_local(
            "faiss_index",
            get_embeddings(),
            allow_dangerous_deserialization=True
        )
        print("FAISS Vector DB Loaded")

    return _vectorstore


def ask_rag(question):

    try:
        # STEP 1: Retrieve Relevant Chunks
        
        docs = get_vectorstore().similarity_search(
            question,
            k=3
        )

        # STEP 2: Build Context
        
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        print("Retrieved Context:")
        print(context)

        # STEP 3: Prompt

        prompt = f"""
        You are a Smart Retail Assistant.

        Answer ONLY using the provided context.

        If answer is not found in context,
        say:
        "Information not available in documents."

        Context:
        {context}

        Question:
        {question}
        """

        # STEP 4: Azure Foundry Response

        response = get_openai_client().chat.completions.create(
            model=os.getenv("FOUNDARY_MODEL", "gpt-oss-120b"),
            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent retail assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=300
        )

        answer = response.choices[0].message.content

        return answer

    except Exception as e:

        return f"RAG ERROR: {str(e)}"
