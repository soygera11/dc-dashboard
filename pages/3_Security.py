import streamlit as st
from utils.data_loader import load_market_data
from utils.charts import bar_chart

st.title("Security & Compliance")

df = load_market_data("data/security.csv")

compliant_count = (df["status"] == "Compliant").sum()
partial_count = (df["status"] == "Partial").sum()

c1, c2, c3 = st.columns(3)
c1.metric("Compliant Controls", compliant_count)
c2.metric("Partial Controls", partial_count)
c3.metric("Security Posture", "Moderate")

status_summary = df.groupby(["status"]).size().reset_index(name="count")
category_summary = df.groupby(["category"]).size().reset_index(name="count")

st.plotly_chart(bar_chart(status_summary, "status", "count", "Compliance Status"), use_container_width=True)
st.plotly_chart(bar_chart(category_summary, "category", "count", "Controls by Category"), use_container_width=True)

st.markdown("### Control Checklist")
st.dataframe(df, use_container_width=True)