import streamlit as st
from ui.upload import upload_csv
from ui.profiling import show_profiling

st.set_page_config(page_title="Auto CSV Cleaner", page_icon=":broom:", layout="wide")

st.title("Automatic CSV Data Cleaner")

df = upload_csv()

if df is not None:
    show_profiling(df)
