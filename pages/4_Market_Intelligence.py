import streamlit as st
from utils.data_loader import load_csv
from utils.charts import bar_chart

st.title("Market Intelligence")

df = load_csv("data/market_mexico.csv")

st.markdown("""
This page summarizes strategic indicators for the Mexican data center market,
with a special focus on **Querétaro** as a regional hotspot.
""")

st.plotly_chart(bar_chart(df, "segment", "value", "Mexico Data Center Market Indicators"), use_container_width=True)

st.markdown("### Strategic Interpretation")
st.write("""
- Strong cloud adoption continues to support colocation and hyperscale growth.
- Querétaro remains a priority market for new digital infrastructure.
- Energy availability is becoming one of the main limiting factors for expansion.
- AI infrastructure demand is creating pressure for new capacity and cooling strategies.
""")

st.info("Later, this page should include cited real market sources inside the dashboard.")