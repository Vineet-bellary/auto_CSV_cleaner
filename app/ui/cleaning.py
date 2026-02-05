import streamlit as st
from core.cleaner import auto_cleaner


def show_cleaning(df):
    st.subheader("Auto Cleaning")

    if st.button("Clean Dataset"):
        cleaned_df = auto_cleaner(df)

        if cleaned_df is not None:

            # store the cleaned version in session
            st.session_state["cleaned_df"] = cleaned_df
            st.session_state["clean_done"] = True

            st.success("_Dataset Cleaned Successfully_")

            st.markdown("### Cleaned Dataset Preview")
            st.dataframe(cleaned_df.head())
