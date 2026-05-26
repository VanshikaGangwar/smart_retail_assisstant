import os

from backend.azure.blob_storage import download_all_pdfs

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

# ---------------------------------------------------
# STEP 1: Download PDFs From Azure Blob Storage
# ---------------------------------------------------

pdf_files = download_all_pdfs()

print("PDFs Downloaded From Azure Blob Storage")

# ---------------------------------------------------
# STEP 2: Load PDF Documents
# ---------------------------------------------------

documents = []

for file in pdf_files:

    try:

        print(f"Loading PDF: {file}")

        loader = PyPDFLoader(file)

        docs = loader.load()

        documents.extend(docs)

    except Exception as e:

        print(f"Error loading {file}: {e}")

print(f"Total Documents Loaded: {len(documents)}")

# ---------------------------------------------------
# STEP 3: Split Documents Into Chunks
# ---------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Chunks Created: {len(chunks)}")

# ---------------------------------------------------
# STEP 4: Create Embeddings
# ---------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embeddings Model Loaded")

# ---------------------------------------------------
# STEP 5: Create FAISS Vector Store
# ---------------------------------------------------

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

print("FAISS Vector Store Created")

# ---------------------------------------------------
# STEP 6: Save Vector Database
# ---------------------------------------------------

FAISS_INDEX_PATH = "faiss_index"

# Create folder if not exists
os.makedirs(FAISS_INDEX_PATH, exist_ok=True)

vectorstore.save_local(FAISS_INDEX_PATH)

print(f"FAISS Index Saved At: {FAISS_INDEX_PATH}")