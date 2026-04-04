import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

if os.path.exists("vectorstore"):
    print("Vectorstore exists. Loading...")
    db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search("BNS 2", k=5)
    with open("test_out.txt", "w", encoding="utf-8") as f:
        for i, doc in enumerate(docs):
            f.write(f"\n--- DOC {i+1} ---\n")
            f.write(doc.page_content)
else:
    print("Vectorstore not found.")
