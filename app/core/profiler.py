import pandas as pd


def profile_dataset(df: pd.DataFrame) -> dict:
    profile = {}

    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]

    profile["missing_values"] = (
        df.isnull()
        .sum()
        .reset_index()
        .rename(columns={"index": "column", 0: "missing_count"})
    )

    profile["duplicate_rows"] = df.duplicated().sum()

    profile["dtypes"] = (
        df.dtypes.astype(str)
        .reset_index()
        .rename(columns={"index": "column", 0: "dtype"})
    )

    profile["unique_values"] = (
        df.nunique()
        .reset_index()
        .rename(columns={"index": "column", 0: "unique_count"})
    )

    return profile
