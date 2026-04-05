import os
import streamlit as st
from groq import Groq

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# -----------------------------
# API KEY (STREAMLIT CLOUD)
# -----------------------------
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# -----------------------------
# EMBEDDINGS
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# VECTOR DB
# -----------------------------
if not os.path.exists("vectorstore"):

    documents = []

    for file in os.listdir("docs"):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(f"docs/{file}")
            try:
                documents.extend(loader.load())
            except Exception:
                pass

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vectorstore")

else:
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

retriever = db.as_retriever(search_kwargs={"k": 10})

# -----------------------------
# UI CONFIG
# -----------------------------
st.set_page_config(page_title="CyberBot", layout="wide")

st.markdown("""
<style>
.stApp {
    display:flex;
    justify-content:center;
    align-items:center;
    background: linear-gradient(135deg,#0f2027,#2c5364);
}
.card {
    width:60%;
    text-align:center;
    padding:40px;
}
.title {font-size:40px;color:white;}
.subtitle {color:#cbd5e1;margin-top:10px;}
.answer-box {
    margin-top:20px;
    color:white;
    background:rgba(255,255,255,0.05);
    padding:15px;
    border-radius:10px;
}

.note{color:#cbd5e1;margin-top:10px;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# UI
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)


st.markdown('<div class="title">⚖️ Cyber Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Legal Guide to Cyber Crimes, IT Act 2000, and Criminal Law</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Digital AI Assistant for any legal queries</div>', unsafe_allow_html=True)
query = st.text_input("", placeholder="Ask your legal question...")
ask = st.button("Ask")
# -----------------------------
# MAIN LOGIC
# -----------------------------
if ask and query:

    # Removed the hardcoded keyword filter so the LLM evaluates the queries based on its strict system prompt.

    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    # -----------------------------
    # PROMPT
    # -----------------------------
    system_msg = f"""You are CyberBot, a highly specialized legal assistant.

YOUR DOMAIN IS STRICTLY LIMITED TO:
- Cyber Law
- Cyber Crime
- IT Act 2000
- Indian Penal Code (IPC)
- Bharatiya Nyaya Sanhita (BNS)
- Criminal Law

CRITICAL RULES:
1. You MUST ONLY answer questions directly related to the topics listed above.
2. If the user asks about ANY other topic (including personal law, corporate law, family law, civil law, or general knowledge), YOU MUST REFUSE TO ANSWER.
3. To refuse, reply EXACTLY with: "I am a specific legal assistant. I only answer questions related to Cyber Law, Cyber Crime, IT Act 2000, IPC, BNS, and Criminal Law."
4. Include relevant sections (IPC / IT Act / BNS) when answering valid questions.
5. Answer in English only.

DOCUMENT CONTEXT:
{context}"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": query}
        ]
    )

    answer = response.choices[0].message.content

    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
 <div class="note">
 ⚠️ Note: This is for informational purposes only.
 👉 If you need legal help , please consult a qualified legal advisor.           
 👉 Type <b>exit</b> to end chat.
 </div>
 <div class="footer">© 2026 CyberBot</div>
 """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)