import streamlit as st
from core.profiler import profile_dataset


def show_profiling(df):
    st.subheader("Dataset Profiling Update")

    profile = profile_dataset(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Duplicate Rows", profile["duplicate_rows"])

    tab1, tab2, tab3 = st.tabs(["Data Types", "Unique Values", "Missing Values"])
    with tab1:
        st.dataframe(profile["dtypes"])
    with tab2:
        st.dataframe(profile["unique_values"])
    with tab3:
        missing_df = profile["missing_values"]
        missing_df = missing_df[missing_df["missing_count"] > 0]
        st.dataframe(missing_df)
