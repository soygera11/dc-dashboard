import pandas as pd
import streamlit as st


@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)