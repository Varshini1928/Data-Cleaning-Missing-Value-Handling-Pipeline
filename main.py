"""
Main script to run the complete data cleaning pipeline.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_data
from src.cleaning import (
    handle_missing_values_drop,
    handle_missing_values_impute,
    handle_missing_values_simple_imputer,
    treat_outliers,
    remove_duplicates
)
from src.visualization import plot_missing_heatmap, plot_age_fare_distribution
from src.utils import verify_dataset, save_cleaned_data

def main():
    print("="*50)
    print("TITANIC DATA CLEANING PIPELINE")
    print("="*50)

    # Step 1: Load raw data
    df = load_data()
    print(f"\n[INFO] Original shape: {df.shape}")
    print(f"[INFO] Columns: {list(df.columns)}")

    # Step 2: Visualize missing data (saves heatmap)
    plot_missing_heatmap(df, save_path="assets/heatmap_before.png")

    # Step 3: Show initial missing counts
    print("\n[INFO] Missing values before any handling:")
    print(df.isnull().sum())

    # Step 4: Handle missing values
    # Option A: Drop rows with missing 'Embarked' (few)
    df = handle_missing_values_drop(df, subset=['Embarked'])
    # Option B: Impute 'Age' with median
    df = handle_missing_values_impute(df, column='Age', strategy='median')
    # Option C: Use SimpleImputer for 'Fare' (if any missing) – using mean
    df = handle_missing_values_simple_imputer(df, column='Fare', strategy='mean')

    # Step 5: Outlier treatment (cap 'Age' and 'Fare' at 1.5*IQR)
    df = treat_outliers(df, columns=['Age', 'Fare'])

    # Step 6: Remove duplicate rows if any
    df = remove_duplicates(df)

    # Step 7: Final verification
    verify_dataset(df)

    # Step 8: Visualize after cleaning (age & fare distribution)
    plot_age_fare_distribution(df, save_path="assets/distributions_after.png")

    # Step 9: Save cleaned dataset
    save_cleaned_data(df, output_path="data/processed/cleaned_titanic.csv")

    print("\n[SUCCESS] Cleaning pipeline finished. Cleaned data saved.")
    print(f"[INFO] Final shape: {df.shape}")

if __name__ == "__main__":
    main()