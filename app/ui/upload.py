"""
Responsibilities:

- Upload CSV
- Parsing using Pandas
- Store in st.session_state
"""

import streamlit as st
import pandas as pd


def upload_csv():
    uploaded_file = st.file_uploader(
        label="Upload your Dataset to begin (*.csv)", type=["csv"], key="data"
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Storing in session state
        st.session_state["df"] = df
        st.session_state.pop("cleaned_df", None)
        st.session_state.pop("clean_done", None)

        st.success("CSV file uploaded successfully")

        st.subheader("Data Preview")
        st.dataframe(df)

        return df

    return None
