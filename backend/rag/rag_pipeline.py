import os

from dotenv import load_dotenv

from openai import AzureOpenAI

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

# ---------------------------------------------------
# LOAD ENV VARIABLES
# ---------------------------------------------------

load_dotenv()

FOUNDARY_API_KEY = os.getenv("FOUNDARY_API_KEY")
FOUNDARY_ENDPOINT = os.getenv("FOUNDARY_ENDPOINT")

# ---------------------------------------------------
# AZURE OPENAI CLIENT
# ---------------------------------------------------

client = AzureOpenAI(
    api_key=FOUNDARY_API_KEY,
    api_version="2024-05-01-preview",
    azure_endpoint=FOUNDARY_ENDPOINT
)

# ---------------------------------------------------
# LOAD EMBEDDINGS
# ---------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------------------------------
# LOAD FAISS VECTOR DATABASE
# ---------------------------------------------------

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

print("FAISS Vector DB Loaded")

# ---------------------------------------------------
# MAIN RAG FUNCTION
# ---------------------------------------------------

def ask_rag(question):

    try:

        # -----------------------------------------
        # STEP 1: Retrieve Relevant Chunks
        # -----------------------------------------

        docs = vectorstore.similarity_search(
            question,
            k=3
        )

        # -----------------------------------------
        # STEP 2: Build Context
        # -----------------------------------------

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        print("Retrieved Context:")
        print(context)

        # -----------------------------------------
        # STEP 3: Prompt
        # -----------------------------------------

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

        # -----------------------------------------
        # STEP 4: Azure Foundry Response
        # -----------------------------------------

        response = client.chat.completions.create(
            model="gpt-oss-120b",
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