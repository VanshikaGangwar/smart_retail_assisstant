from backend.azure.blob_storage import (
    download_all_pdfs
)

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS

# Download PDFs from Azure Blob
pdf_files = download_all_pdfs()

print("PDFs Downloaded From Azure")

documents = []

# Load PDFs
for file in pdf_files:

    loader = PyPDFLoader(file)

    docs = loader.load()

    documents.extend(docs)

print("PDFs Loaded")

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Chunks Created: {len(chunks)}")

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

# Save vector DB
vectorstore.save_local("faiss_index")

print("FAISS Vector Store Created")