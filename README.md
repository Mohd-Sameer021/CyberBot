

# ⚖️ CyberBot

This project is an AI-based chatbot that answers questions related to **Cyber Crime and Criminal Law** using legal documents like:

- IT Act 2000
- Indian Penal Code (IPC)/BNS
- Cyber Crime Handbook
- Criminal Law Handbook
- Secure API key handling using .env
It uses **RAG (Retrieval-Augmented Generation)** to give accurate answers.


---

## Features

- Answers only legal questions (Cyber + Criminal Law)
- Uses real PDFs as knowledge base
- Fast response using FAISS vector database
- Accurate answers using Groq LLM (LLaMA3)
- Simple UI built with Streamlit

---

## Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API

## Project Structure

CyberBot/│
├── app.py
├── requirements.txt
├── README.md
├── docs/|
    ├── BNS_English_30-04-2024.pdf
    ├── IPC_186045.pdf
    ├── it act 2000.pdf
    ├── IT-Act-Rules_2000_0.pdf
    ├── jhpolice_cyber_crime_investigation_manual.pdf
    ├── What is Cyber Crime21.pdf
├── vectorstore/
    ├── index.faiss
    ├── index.pkl
├── create_vector_db.py
├── build_db.py
├── .gitignore
├── .env


##  How It Works

1. PDFs are loaded and converted into text
2. Text is converted into embeddings
3. FAISS stores embeddings as vector database
4. User asks a question
5. Relevant data is retrieved
6. Groq LLM generates final answer

---

## Setup

1. Clone repo
git clone
https://github.com/Sameer021/CyberBot.git

2. Install
pip install -r requirements.txt

3. Add API Key
Create .env file:
GROQ_API_KEY=your_api_key

4. Run
streamlit run app.py


## Disclaimer
Educational Purpose Only


