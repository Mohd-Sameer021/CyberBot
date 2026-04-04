import os

from datasets import load_dataset

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


print("Loading IT Act PDF...")

loader = PyPDFLoader("docs/it act 2000.pdf")
pdf_docs = loader.load()


print("Loading HuggingFace criminal dataset...")

dataset = load_dataset("PaxwellPaxwell/law_documents_criminal_qa_ready_train")

dataset_docs = []

# Using only first 500 rows for faster testing
for item in dataset["train"].select(range(500)):

    instruction = item["instruction"]
    input_text = item["input"]
    output = item["output"]

    text = f"Question: {instruction} {input_text}\nAnswer: {output}"

    dataset_docs.append(Document(page_content=text))


print("Combining PDF + dataset documents...")

all_docs = pdf_docs + dataset_docs


print("Splitting documents...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(all_docs)


print("Creating embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


print("Creating FAISS vector database...")

vectorstore = FAISS.from_documents(chunks, embeddings)


print("Saving vector database...")

vectorstore.save_local("vectorstore")


print("Vector database created successfully!")