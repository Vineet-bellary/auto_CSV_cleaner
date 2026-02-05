import streamlit as st
import os


def download_cleaned_csv():
    cleaned_df = st.session_state.get("cleaned_df")
    orig_filename = st.session_state.get(key="uploaded_filename", default="dataset.csv")

    if cleaned_df is None:
        return

    base, ext = os.path.splitext(orig_filename)
    cleaned_filename = f"{base}_cleaned{ext}"

    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    st.subheader("Download Cleaned Dataset (.csv)")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv,
        file_name=cleaned_filename,
        mime="text/csv",
    )
