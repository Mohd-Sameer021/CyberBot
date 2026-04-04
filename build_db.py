import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = []
for file in os.listdir("docs"):
    if file.endswith(".pdf"):
        print(f"Loading {file}...")
        loader = PyPDFLoader(f"docs/{file}")
        documents.extend(loader.load())

print("Splitting documents...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)

print("Building vector database...")
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("vectorstore")
print("Done!")
