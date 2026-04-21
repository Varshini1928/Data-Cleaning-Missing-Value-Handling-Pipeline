"""
Streamlit dashboard to preview and download the cleaned Titanic dataset.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_data
from src.cleaning import (
    handle_missing_values_drop,
    handle_missing_values_impute,
    handle_missing_values_simple_imputer,
    treat_outliers,
    remove_duplicates
)

st.set_page_config(page_title="Titanic Data Cleaning", layout="wide")

st.title("🚢 Titanic Dataset Cleaning Dashboard")
st.markdown("This app demonstrates the **data cleaning and missing value handling** pipeline for the Titanic dataset.")

# Load raw data
@st.cache_data
def load_raw():
    return load_data()

df_raw = load_raw()

# Sidebar: show raw data preview
st.sidebar.header("Raw Data Preview")
st.sidebar.dataframe(df_raw.head())

# Main area: cleaning steps explanation
with st.expander("📌 Cleaning Steps Applied"):
    st.markdown("""
    1. **Drop rows** with missing 'Embarked' (only 2 rows).
    2. **Impute 'Age'** using median value.
    3. **Impute 'Fare'** using SimpleImputer (mean strategy).
    4. **Cap outliers** in 'Age' and 'Fare' using IQR (1.5x rule).
    5. **Remove duplicate rows** (if any).
    """)

# Perform cleaning (cached)
@st.cache_data
def run_cleaning(df):
    df_clean = df.copy()
    # Drop missing Embarked
    df_clean = handle_missing_values_drop(df_clean, subset=['Embarked'])
    # Impute Age median
    df_clean = handle_missing_values_impute(df_clean, column='Age', strategy='median')
    # Impute Fare mean with SimpleImputer
    df_clean = handle_missing_values_simple_imputer(df_clean, column='Fare', strategy='mean')
    # Outliers
    df_clean = treat_outliers(df_clean, columns=['Age', 'Fare'])
    # Duplicates
    df_clean = remove_duplicates(df_clean)
    return df_clean

df_clean = run_cleaning(df_raw)

# Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Missing Values Heatmap (Before)")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.heatmap(df_raw.isnull(), cbar=False, yticklabels=False, cmap='viridis', ax=ax1)
    ax1.set_title("Raw Data - Missing Values")
    st.pyplot(fig1)

with col2:
    st.subheader("Missing Values Heatmap (After)")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.heatmap(df_clean.isnull(), cbar=False, yticklabels=False, cmap='viridis', ax=ax2)
    ax2.set_title("Cleaned Data - No Missing Values")
    st.pyplot(fig2)

# Data previews
tab1, tab2 = st.tabs(["📋 Raw Data Sample", "✅ Cleaned Data Sample"])

with tab1:
    st.dataframe(df_raw.head(10))
    st.caption(f"Shape: {df_raw.shape} | Missing values: {df_raw.isnull().sum().sum()}")

with tab2:
    st.dataframe(df_clean.head(10))
    st.caption(f"Shape: {df_clean.shape} | Missing values: {df_clean.isnull().sum().sum()} (should be 0)")

# Download button
csv = df_clean.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Cleaned CSV",
    data=csv,
    file_name="cleaned_titanic.csv",
    mime="text/csv"
)

st.success("All missing values handled! The cleaned dataset is ready.")