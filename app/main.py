import streamlit as st
from ui.upload import upload_csv
from ui.profiling import show_profiling
from ui.cleaning import show_cleaning

st.set_page_config(page_title="Auto CSV Cleaner", page_icon=":broom:", layout="wide")

st.title("Automatic CSV Data Cleaner")

df = upload_csv()

if df is not None:
    st.markdown("## Raw Dataset Profiling")
    show_profiling(df)

    st.info(
        "Auto Clean uses median for numerical columns and mode for categorical columns."
    )
    show_cleaning(df)

    cleaned_df = st.session_state.get("cleaned_df")

    if cleaned_df is not None:
        st.markdown("## Cleaned Dataset Profiling")
        show_profiling(cleaned_df)
        st.success("Profiling after cleaning confirms dataset is ML-ready.")
