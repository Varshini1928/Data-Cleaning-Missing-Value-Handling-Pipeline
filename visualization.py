"""
Visualisation functions for missing data and distributions.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_missing_heatmap(df, save_path=None):
    """
    Plot a heatmap of missing values in the DataFrame.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"[INFO] Heatmap saved to {save_path}")
    plt.show()

def plot_age_fare_distribution(df, save_path=None):
    """
    Plot distribution of Age and Fare after cleaning.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Age distribution
    sns.histplot(df['Age'].dropna(), kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title('Age Distribution (After Cleaning)')
    
    # Fare distribution
    sns.histplot(df['Fare'].dropna(), kde=True, ax=axes[1], color='salmon')
    axes[1].set_title('Fare Distribution (After Cleaning)')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
        print(f"[INFO] Distributions saved to {save_path}")
    plt.show()