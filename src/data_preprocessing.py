import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

def clean_text(text):
    """Clean the complaint narrative text."""
    if pd.isna(text):
        return ""
    # Lowercase
    text = text.lower()
    # Remove CFPB redaction marks (e.g., XXXX, XX/XX/2023)
    text = re.sub(r'x+', '', text)
    # Remove boilerplate text
    text = re.sub(r'i am writing to file a complaint|to whom it may concern', '', text)
    # Remove special characters and digits
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra whitespace
    text = " ".join(text.split())
    return text

def run_preprocessing(input_path, output_path):
    print("Loading dataset...")
    df = pd.read_csv(input_path, low_memory=False)
    
    # 1. Product Mapping (CFPB naming conventions)
    product_map = {
        'Credit card': 'Credit card',
        'Credit card or prepaid card': 'Credit card',
        'Personal loan': 'Personal loan',
        'Payday loan, title loan, or personal loan': 'Personal loan',
        'Savings account': 'Savings account',
        'Checking or savings account': 'Savings account',
        'Money transfer, virtual currency, or money service': 'Money transfers',
        'Money transfers': 'Money transfers'
    }
    
    # 2. Filter Products
    df_filtered = df[df['Product'].isin(product_map.keys())].copy()
    df_filtered['Product_Group'] = df_filtered['Product'].map(product_map)
    
    # 3. Handle Narratives
    # Identify count before removal
    total_in_scope = len(df_filtered)
    df_filtered = df_filtered.dropna(subset=['Consumer complaint narrative'])
    print(f"Removed {total_in_scope - len(df_filtered)} records without narratives.")
    
    # 4. Clean Narratives
    print("Cleaning text narratives...")
    df_filtered['cleaned_narrative'] = df_filtered['Consumer complaint narrative'].apply(clean_text)
    
    # 5. Length Analysis (Word Count)
    df_filtered['word_count'] = df_filtered['cleaned_narrative'].apply(lambda x: len(x.split()))
    
    # Save the cleaned dataset
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_filtered.to_csv(output_path, index=False)
    print(f"Saved {len(df_filtered)} records to {output_path}")
    return df_filtered

if __name__ == "__main__":
    # Update this path to your local raw data location
    run_preprocessing('../data/raw/complaints.csv', '../data/processed/filtered_complaints.csv')