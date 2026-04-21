"""
Functions for handling missing values, outliers, and duplicates.
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def handle_missing_values_drop(df, subset=None, axis=0, how='any'):
    """
    Drop rows or columns with missing values.
    """
    if subset is None:
        subset = df.columns.tolist()
    return df.dropna(subset=subset, axis=axis, how=how)

def handle_missing_values_impute(df, column, strategy='median'):
    """
    Impute missing values in a single column using mean, median, or mode.
    """
    if strategy == 'mean':
        value = df[column].mean()
    elif strategy == 'median':
        value = df[column].median()
    elif strategy == 'mode':
        value = df[column].mode()[0]
    else:
        raise ValueError("strategy must be 'mean', 'median', or 'mode'")
    
    df[column].fillna(value, inplace=True)
    return df

def handle_missing_values_simple_imputer(df, column, strategy='mean'):
    """
    Use sklearn SimpleImputer to handle missing values in a column.
    """
    imputer = SimpleImputer(strategy=strategy)
    # Reshape for imputer (needs 2D)
    values = df[[column]].values
    imputed_values = imputer.fit_transform(values)
    df[column] = imputed_values.flatten()
    return df

def treat_outliers(df, columns, method='iqr', factor=1.5):
    """
    Cap outliers using IQR (Interquartile Range) method.
    """
    for col in columns:
        if col not in df.columns:
            continue
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR
        df[col] = df[col].clip(lower_bound, upper_bound)
    return df

def remove_duplicates(df, subset=None):
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates(subset=subset, keep='first')
