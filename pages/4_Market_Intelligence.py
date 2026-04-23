import streamlit as st
import plotly.express as px
from utils.data_loader import load_market_data

st.title("📊 Market Intelligence (Real Data - Mexico)")

df = load_market_data()

fig = px.line(df, x="Year", y="DataCenterGrowth_MX_%",
              title="Data Center Growth in Mexico (%)",
              markers=True)

st.plotly_chart(fig, use_container_width=True)

st.caption("Source: Statista, CBRE Data Center Trends LATAM 2024")