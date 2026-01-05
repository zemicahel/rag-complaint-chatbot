RAG Complaint Chatbot

A Retrieval-Augmented Generation (RAG) system designed to analyze and retrieve information from the Consumer Financial Protection Bureau (CFPB) complaint dataset. This project processes large-scale financial complaint data, indexes it into a vector store, and provides a semantic search interface.

📂 Project Structure

rag-complaint-chatbot/
├── .github/workflows/       # CI/CD for unit tests
├── data/
│   ├── raw/                 # Original CFPB complaints.csv (Git ignored)
│   └── processed/           # Cleaned and filtered data
├── vector_store/            # Persisted FAISS index files
├── notebooks/               # EDA and Pipeline execution notebooks
├── src/                     # Source code for the pipeline
│   ├── __init__.py
│   ├── data_preprocessing.py # Task 1: Cleaning & Filtering logic
│   └── indexing.py           # Task 2: Chunking & Embedding logic
├── tests/                   # Pytest suite
├── app.py                   # Future Gradio/Streamlit interface
├── requirements.txt         # Project dependencies
└── README.md
🚀 Getting Started
1. Clone and Setup

git clone https://github.com/zemicahel/rag-complaint-chatbot.git
cd rag-complaint-chatbot
pip install -r requirements.txt
2. Data Preparation

Download the CFPB Complaint Dataset.

Place the file in data/raw/ and rename it to complaints.csv.

3. Run the Pipeline

You can run the pipeline via the Jupyter Notebook in notebooks/01_full_pipeline.ipynb or via terminal:

Step 1: Preprocessing (Task 1)

code
Bash
download
content_copy
expand_less
python src/data_preprocessing.py

Action: Filters data for specified products and cleans the text narratives.

Step 2: Indexing (Task 2)



Action: Performs stratified sampling, chunks text, and generates the FAISS vector index.

🛠 Project Components
Task 1: EDA & Preprocessing

Objective: Cleanse and prepare raw CFPB data for embedding.

Key Actions:

Filtered for Credit Card, Personal Loan, Savings Account, and Money Transfers.

Removed records with empty narratives.

Normalized text (lowercasing, special character removal, and stripping "XXXX" redactions).

Output: data/processed/filtered_complaints.csv.

Task 2: Embedding & Vector Store

Sampling: Stratified sampling of 15,000 records to maintain proportional representation across categories.

Chunking: Used RecursiveCharacterTextSplitter (Size: 500, Overlap: 50).

Model: sentence-transformers/all-MiniLM-L6-v2.

Store: FAISS (Facebook AI Similarity Search) for local vector persistence.

🛰 Git & Remote Compatibility

This repository uses a .gitignore file to ensure large data files and local environment files are not tracked.

Pushing to GitHub

If you are setting this up as a new remote, use these commands:


git init
git add .
git commit -m "Initial commit: Completed Task 1 and Task 2"
git branch -M main
git remote add origin https://github.com/zemicahel/rag-complaint-chatbot.git
git push -u origin main
🧰 Tech Stack

Language: Python 3.9+

Data Science: Pandas, Scikit-learn, Matplotlib

LLM Tools: LangChain, LangChain-Core

Embeddings: HuggingFace Sentence-Transformers

Vector DB: FAISS

✅ Task Checklist

Task 1: EDA and Data Preprocessing

Task 2: Text Chunking, Embedding, and Indexing

Task 3: RAG Retrieval Logic (In Progress)

Task 4: UI Development (Pending)

