import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embeddings & FAISS vector store
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# UPDATED: Use langchain_core for the Document class
from langchain_core.documents import Document  

def create_vector_store(csv_path, vector_store_path):
    df = pd.read_csv(csv_path)
    
    # 1. Stratified Sampling (15,000 samples)
    print("Performing stratified sampling...")
    # Add a check to ensure we don't try to sample more than we have
    sample_size = min(15000, len(df))
    df_sample, _ = train_test_split(
        df, 
        train_size=sample_size, 
        stratify=df['Product_Group'], 
        random_state=42
    )
    
    # 2. Convert to LangChain Documents
    documents = []
    for _, row in df_sample.iterrows():
        # Ensure cleaned_narrative is a string
        content = str(row['cleaned_narrative']) if pd.notna(row['cleaned_narrative']) else ""
        doc = Document(
            page_content=content,
            metadata={
                "complaint_id": str(row['Complaint ID']),
                "product": row['Product_Group'],
                "issue": row['Issue']
            }
        )
        documents.append(doc)
    
    # 3. Text Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks from {len(documents)} documents.")
    
    # 4. Embedding Model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # 5. Indexing with FAISS
    print("Generating embeddings and building FAISS index...")
    vector_db = FAISS.from_documents(chunks, embeddings)
    
    # 6. Persist Index
    os.makedirs(vector_store_path, exist_ok=True)
    vector_db.save_local(vector_store_path)
    print(f"Vector store persisted to {vector_store_path}")

if __name__ == "__main__":
    # If running as a script, use relative paths from the root
    create_vector_store('data/processed/filtered_complaints.csv', 'vector_store/faiss_index')