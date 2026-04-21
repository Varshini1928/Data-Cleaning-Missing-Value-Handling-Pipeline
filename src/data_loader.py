"""
Load Titanic dataset from local CSV or download if not found.
"""

import pandas as pd
import os

def load_data(filepath="data/raw/titanic.csv"):
    """
    Load the Titanic dataset.
    If the file does not exist, download from a public URL.
    """
    if os.path.exists(filepath):
        print(f"[INFO] Loading dataset from {filepath}")
        df = pd.read_csv(filepath)
    else:
        print("[INFO] Local dataset not found. Downloading from web...")
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"[INFO] Dataset saved to {filepath}")
    return df
