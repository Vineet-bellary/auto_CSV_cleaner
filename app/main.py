import streamlit as st
from ui.upload import upload_csv

st.set_page_config(page_title="Auto CSV Cleaner", page_icon=":broom:", layout="wide")

st.title("Automatic CSV Data Cleaner")

df = upload_csv()

if df is not None:
    st.write("### Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
