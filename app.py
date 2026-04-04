# import os
# import streamlit as st
# from groq import Groq

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings

# from dotenv import load_dotenv
# load_dotenv()
# api_key=os.getenv("GROQ_API_KEY")

# api_key=st.secrets["GROQ_API_KEY"]
# # -----------------------------
# # API KEY
# # -----------------------------
# #client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# client=Groq(api_key=api_key)
# # -----------------------------
# # Embeddings
# # -----------------------------
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# # -----------------------------
# # Vector DB
# # -----------------------------
# if not os.path.exists("vectorstore"):

#     st.write("Building vector database...")

#     documents = []
#     for file in os.listdir("docs"):
#         if file.endswith(".pdf"):
#             loader = PyPDFLoader(f"docs/{file}")
#             #documents.extend(loader.load())
#             try:
#                 documents.extend(loader.load())
#             except Exception as e:
#                 print(f"Error loading PDF:{e}")

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )

#     chunks = splitter.split_documents(documents)

#     vectorstore = FAISS.from_documents(chunks, embeddings)
#     vectorstore.save_local("vectorstore")
#     db = vectorstore

# else:
#     db = FAISS.load_local(
#         "vectorstore",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

# retriever = db.as_retriever(search_kwargs={"k": 12})

# # -----------------------------
# # PAGE CONFIG
# # -----------------------------
# st.set_page_config(page_title="CyberBot", layout="wide")

# # -----------------------------
# # CSS
# # -----------------------------
# st.markdown("""
# <style>

# /* Full height */
# html, body, .stApp {
#     height: 100%;
#     margin: 0;
# }

# /* Center everything */
# .stApp {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     background: linear-gradient(135deg, #0f2027, #2c5364);
#     font-family: 'Segoe UI', sans-serif;
# }

# /* Card */
# .card {
#     width: 60%;
#     padding: 40px;
#     text-align: center;
# }

# /* Title */
# .title {
#     font-size: 42px;
#     font-weight: bold;
#     color: white;
# }

# /* Subtitle */
# .subtitle {
#     color: #cbd5e1;
#     margin-top: 10px;
# }

# /* Input + Button same line */
# .input-container {
#     display: flex;
#     align-items: center;
#     gap: 10px;
#     margin-top: 20px;
# }

# /* Input box takes full space */
# .input-box {
#     flex: 1;
# }

# /* Input styling */
# .stTextInput input {
#     border-radius: 30px;
#     padding: 14px;
#     height: 48px;
# }

# /* Button */
# .stButton button {
#     height: 48px;
#     border-radius: 25px;
#     background: #00bcd4;
#     color: white;
#     border: none;
#     padding: 0 25px;
#     white-space: nowrap;
# }

# /* Answer box */
# .answer-box {
#     margin-top: 20px;
#     color: white;
#     text-align: left;
#     background: rgba(255,255,255,0.05);
#     padding: 15px;
#     border-radius: 10px;
# }

# /* Footer */
# .note {
#     color: #f87171;
#     font-size: 13px;
#     margin-top: 15px;
# }

# .footer {
#     color: #94a3b8;
#     font-size: 12px;
# }

# </style>
# """, unsafe_allow_html=True)

# # -----------------------------
# # SESSION
# # -----------------------------
# if "response" not in st.session_state:
#     st.session_state.response = ""

# # -----------------------------
# # UI START
# # -----------------------------
# st.markdown('<div class="card">', unsafe_allow_html=True)

# st.markdown('<div class="title">⚖️ Cyber Bot</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Your Legal Guide to Cyber Crimes, IT Act 2000, and Criminal Law</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Digital AI Assistant for any legal queries</div>', unsafe_allow_html=True)

# # -----------------------------
# # INPUT + BUTTON
# # -----------------------------
# st.markdown('<div class="input-container">', unsafe_allow_html=True)

# st.markdown('<div class="input-box">', unsafe_allow_html=True)
# query = st.text_input(
#     "",
#     placeholder="Ask your Cyber Law & Criminal Law question...",
#     label_visibility="collapsed"
# )
# st.markdown('</div>', unsafe_allow_html=True)

# ask = st.button("Ask")

# st.markdown('</div>', unsafe_allow_html=True)

# # -----------------------------
# # EXIT
# # -----------------------------
# if ask and query.lower().strip() == "exit":
#     st.session_state.response = "Chat ended. Thank you for using CyberBot ⚖️"
#     st.stop()

# # -----------------------------
# # MAIN LOGIC
# # -----------------------------
# if ask and query:

#     docs = retriever.invoke(query)
#     context = "\n".join([doc.page_content for doc in docs])

#     prompt = f"""
# You are CyberBot, an expert legal AI assistant specialized in IPC, BNS, Cyber Crime, Cyber Law, and IT Act 2000.

# Rules:
# - Answer ONLY legal questions
# - Answer ONLY in English
# - Provide structured answers

# Context:
# {context}

# Question:
# {query}

# Answer:
# """

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     st.session_state.response = response.choices[0].message.content

# # -----------------------------
# # SHOW ANSWER
# # -----------------------------
# if st.session_state.response:
#     st.markdown(
#         f'<div class="answer-box">{st.session_state.response}</div>',
#         unsafe_allow_html=True
#     )

# # -----------------------------
# # FOOTER
# # -----------------------------
# st.markdown("""
# <div class="note">
# ⚠️ Note: This is for informational purposes only.
# 👉 Type <b>exit</b> to end chat.
# </div>
# <div class="footer">© 2026 CyberBot</div>
# """, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)


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
</style>
""", unsafe_allow_html=True)

# -----------------------------
# UI
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="title">⚖️ Cyber Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Cyber Law • IT Act • IPC • BNS • Criminal Law</div>', unsafe_allow_html=True)

query = st.text_input("", placeholder="Ask your legal question...")
ask = st.button("Ask")

# -----------------------------
# MAIN LOGIC
# -----------------------------
if ask and query:

    # ✅ MULTI LAW FILTER
    keywords = [
        "cyber", "hack", "online", "fraud", "phishing", "it act",
        "ipc", "bns", "criminal", "crime", "section",
        "punishment", "murder", "theft", "cheating"
    ]

    if not any(word in query.lower() for word in keywords):
        st.warning("❌ This bot only answers Cyber Law and Criminal Law queries.")
        st.stop()

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
<p style='color:#f87171;text-align:center;'>
⚠️ For educational purposes only
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)