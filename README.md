

RAG Complaint Chatbot

A Retrieval-Augmented Generation (RAG) system designed to analyze and retrieve information from the Consumer Financial Protection Bureau (CFPB) complaint dataset. This project processes large-scale financial complaint data, indexes it into a vector store, and provides a semantic search interface.

📂 Project Structure
code
Text
download
content_copy
expand_less
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

Download the CFPB Complaint Dataset (CSV format).

Place the file in data/raw/ and rename it to complaints.csv.

3. Run the Pipeline

You can run the pipeline via the Jupyter Notebook in notebooks/01_full_pipeline.ipynb or via terminal:

Step 1: Preprocessing (Task 1)


python src/data_preprocessing.py

Action: Filters data for Credit Cards, Personal Loans, Savings Accounts, and Money Transfers, and cleans the text.

Step 2: Indexing (Task 2)


python src/indexing.py

Action: Performs stratified sampling (15k records), chunks text, generates embeddings, and saves a FAISS index.

🛠 Project Components
Task 1: EDA & Preprocessing

Objective: Cleanse and prepare the raw CFPB data.

Key Actions:

Filtered for 5 specific product categories.

Removed records without narratives.

Normalized text: lowercasing, removing special characters, and stripping CFPB redaction marks (e.g., "XXXX").

Output: data/processed/filtered_complaints.csv.

Task 2: Embedding & Vector Store

Sampling: Stratified sampling of 15,000 records to ensure proportional representation.

Chunking: RecursiveCharacterTextSplitter with a chunk size of 500 and overlap of 50.

Model: sentence-transformers/all-MiniLM-L6-v2.

Store: FAISS (Facebook AI Similarity Search) for efficient similarity retrieval.

🛰 Git & Remote Compatibility

This repository is optimized for Git. However, because the raw data and vector indices can be large, the following are excluded via .gitignore:

data/raw/ (Huge CSV files)

vector_store/ (Binary index files)

__pycache__/

Pushing to Remote

git add .
git commit -m "Complete Task 1 and 2"
git push origin main
🧰 Tech Stack

Language: Python 3.9+

Data: Pandas, Scikit-learn

RAG Framework: LangChain, LangChain-Core

Embeddings: Sentence-Transformers (HuggingFace)

Vector DB: FAISS

✅ Task Checklist

Task 1: EDA and Data Preprocessing

Task 2: Text Chunking, Embedding, and Indexing

Task 3: RAG Retrieval Logic (Pending)

Task 4: UI Development (Pending)

