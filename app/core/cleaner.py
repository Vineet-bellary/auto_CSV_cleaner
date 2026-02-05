"""
Docstring for app.core.cleaner

- Duplicate4 rows remove
- strip column names
- Handle missing values
"""

import pandas as pd


def auto_cleaner(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    # Remove duplicate Rows
    cleaned_df = cleaned_df.drop_duplicates()

    # Strip column names
    cleaned_df.columns = cleaned_df.columns.str.strip()

    # 3. Handle missing values
    for col in cleaned_df.columns:
        if cleaned_df[col].dtype in ["int64", "float64"]:
            cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())
        else:
            if not cleaned_df[col].mode().empty:
                cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mode()[0])

    # 4. Strip spaces in string columns
    for col in cleaned_df.select_dtypes(include="object").columns:
        cleaned_df[col] = cleaned_df[col].str.strip()

    return cleaned_df
