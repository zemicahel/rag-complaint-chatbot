If your file structure looks jumbled on GitHub, it is usually because the Markdown code blocks (the ``` symbols) are missing or not separated by blank lines. GitHub needs those backticks to tell it "show this exactly as written in a fixed-width font."

Here is the cleanest possible version of the project structure. Copy the text starting from the # RAG title all the way to the end.

RAG Complaint Chatbot

A Retrieval-Augmented Generation (RAG) system designed to analyze and retrieve information from the Consumer Financial Protection Bureau (CFPB) complaint dataset.

📂 Project Structure


rag-complaint-chatbot/
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .vscode/
│   └── settings.json
├── data/
│   ├── raw/                       # Place complaints.csv here
│   └── processed/                 # filtered_complaints.csv saved here
├── notebooks/
│   ├── __init__.py
│   └── 01_full_pipeline.ipynb     # Main execution notebook
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py      # Task 1: Cleaning logic
│   └── indexing.py                # Task 2: Embedding logic
├── tests/
│   ├── __init__.py
│   └── test_logic.py
├── vector_store/
│   └── faiss_index/               # Persisted vector database
├── app.py                         # Chatbot interface
├── requirements.txt               # Dependencies
├── README.md
└── .gitignore                     # To ignore data/ and vector_store/
🚀 Getting Started
1. Setup Environment

git clone https://github.com/zemicahel/rag-complaint-chatbot.git
cd rag-complaint-chatbot
pip install -r requirements.txt
2. Run Data Pipeline

You can run the full process from the terminal:

Step 1: Preprocessing


python src/data_preprocessing.py

Step 2: Indexing


python src/indexing.py
🛠 Project Components
Task 1: EDA & Preprocessing

Cleaned CFPB narratives by removing redactions (XXXX) and boilerplate text.

Filtered for Credit Card, Personal Loan, Savings Account, and Money Transfers.

Task 2: Embedding & Vector Store

Sampling: 15,000 records (Stratified).

Chunking: 500 characters with 50-character overlap.

Model: all-MiniLM-L6-v2.

Store: FAISS.

✅ Task Checklist

Task 1: EDA and Data Preprocessing

Task 2: Text Chunking, Embedding, and Indexing

Task 3: RAG Retrieval Logic

Task 4: UI Development


