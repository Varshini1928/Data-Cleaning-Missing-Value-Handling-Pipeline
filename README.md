#  Data Cleaning & Missing Value Handling

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📌 What I Have Done in This Project

### Project Overview
I built a complete end-to-end data cleaning pipeline for the Titanic dataset as part of my AI/ML internship Task 2. The project handles missing values, outliers, and duplicates using Python libraries like Pandas, NumPy, Scikit-learn, and visualizes results with Matplotlib, Seaborn, and Streamlit.

---

## 🔧 Step-by-Step Work Done

### 1. Project Setup
- Created folder structure: `data/raw/`, `data/processed/`, `src/`, `assets/`, `notebooks/`
- Set up virtual environment and installed dependencies
- Created modular Python files for reusability

### 2. Data Loading
- Loaded Titanic dataset (891 rows, 12 columns)
- Dataset auto-downloads from URL if not found locally
- Checked shape, columns, data types, and basic info

### 3. Missing Value Detection
- Used `.isnull().sum()` to identify missing values
- Found missing data in:
  - **Cabin:** 687 missing (77.1%)
  - **Age:** 177 missing (19.9%)
  - **Embarked:** 2 missing (0.2%)
  - **Fare:** 1 missing (0.1%)
- Created heatmap visualization using Seaborn to visualize missing patterns

### 4. Handling Missing Values (3 Different Methods)

| Column | Method | Code Used | Why This Method |
|--------|--------|-----------|-----------------|
| Cabin | Deletion (drop column) | `df.drop('Cabin', axis=1)` | 77% missing - imputation would create bias |
| Embarked | Deletion (drop rows) | `df.dropna(subset=['Embarked'])` | Only 2 rows - minimal impact |
| Age | Median Imputation | `df['Age'].fillna(df['Age'].median())` | Robust to outliers, skewed distribution |
| Fare | SimpleImputer (mean) | `SimpleImputer(strategy='mean')` | Only 1 missing, near-normal distribution |

### 5. Outlier Detection & Treatment
- Used IQR (Interquartile Range) method
- Formula: `IQR = Q3 - Q1`, bounds = `Q1 - 1.5*IQR` and `Q3 + 1.5*IQR`
- Applied to 'Age' and 'Fare' columns
- Capped outliers instead of removing them to preserve data

### 6. Duplicate Removal
- Used `df.drop_duplicates()` to check and remove duplicate rows
- No duplicates found in the dataset

### 7. Final Dataset Verification
- Ran `.isnull().sum().sum()` to confirm zero missing values
- Verified shape, data types, and memory usage
- Saved cleaned dataset to `data/processed/cleaned_titanic.csv`

### 8. Streamlit Dashboard
Built an interactive web app with:
- **Raw data preview** section
- **Cleaned data preview** section
- **Missing value heatmaps** (before vs after)
- **Distribution plots** for Age and Fare
- **Download button** to export cleaned CSV

### 9. Version Control & Deployment
- Initialized Git repository
- Created `.gitignore` for Python files
- Pushed code to GitHub
- Deployed Streamlit app on Streamlit Cloud

---

## 📊 Results Achieved

| Metric | Before Cleaning | After Cleaning |
|--------|----------------|----------------|
| Rows | 891 | 889 |
| Columns | 12 | 11 |
| Total Missing Values | 867 | **0** ✅ |
| Missing in Age | 177 | 0 (median imputed) |
| Missing in Fare | 1 | 0 (mean imputed) |
| Missing in Embarked | 2 | 0 (rows dropped) |
| Cabin Column | Present | Removed (77% missing) |
| Outliers in Age | Present | Capped (IQR method) |
| Outliers in Fare | Present | Capped (IQR method) |
| Duplicates | 0 | 0 |


---

# 1. Clone repository
git clone https://github.com/Varshini1928/Data-Cleaning-Missing-Value-Handling-Pipeline.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run cleaning pipeline
python main.py

# 4. Launch dashboard
streamlit run app.py
