import streamlit as st
from core.profiler import profile_dataset


def show_profiling(df):
    st.subheader("Dataset Profiling Update")

    profile = profile_dataset(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Duplicate Rows", profile["duplicate_rows"])

    combined_df = profile["dtypes"].merge(profile["unique_values"], on="column")
    combined_df = profile["unique_values"].merge(profile["missing_values"], on="column")

    st.dataframe(combined_df, use_container_width=True)
