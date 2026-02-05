import streamlit as st
import pandas as pd

st.title(body="Auto CSV Cleaner", anchor="CSVcleaner")

# Upload CSV file and display its contents.
df = None
uploaded_file = st.file_uploader(label="Upload CSV file", type="csv")
with st.spinner("File uploading...", show_time=True):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.success("File uploaded successfully!")

if df is not None:
    rows, cols = df.shape
    st.write(f"Number of Records: ***{rows}*** | Number of Attributes: ***{cols}***")
