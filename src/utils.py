"""
Utility functions: dataset verification and saving.
"""

import pandas as pd
import os

def verify_dataset(df):
    """
    Check that the dataset has no missing values and report basic info.
    """
    print("\n" + "="*40)
    print("DATASET VERIFICATION")
    print("="*40)
    missing_counts = df.isnull().sum()
    total_missing = missing_counts.sum()
    print(f"Total missing values: {total_missing}")
    if total_missing == 0:
        print("✅ No missing values found. Dataset is clean.")
    else:
        print("⚠️ Warning: Missing values still present:")
        print(missing_counts[missing_counts > 0])
    
    print(f"Shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

def save_cleaned_data(df, output_path):
    """
    Save the cleaned DataFrame to a CSV file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[INFO] Cleaned data saved to {output_path}")
