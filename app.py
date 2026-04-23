import streamlit as st
from utils.data_loader import load_market_data

st.set_page_config(
    page_title="QRO Nexus DC Intelligence GC",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    h1, h2, h3 {
        color: #00C6FF;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
body {
    background-color: #white;
    color: #f5f5f0;
}
h1, h2, h3 {
    color: #c9a84c;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='color:#c9a84c;'>QRO Nexus DC Intelligence</h1>
<h3 style='color:#7b2fb5;'>Operational Visibility for Mexico's Digital Infrastructure</h3>
""", unsafe_allow_html=True)
st.subheader("Operational Visibility for Mexico's Digital Infrastructure")

st.markdown("""
**QRO Nexus** is a fictional data center campus based in Querétaro, Mexico.
This dashboard combines:
- **Unit 3:** Data center administration
- **Unit 4:** Market intelligence and technology trends
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Campus Status", "Operational")
col2.metric("Tier Goal", "III")
col3.metric("Region", "Querétaro")
col4.metric("Mode", "Executive")

st.markdown("### Pages")
st.markdown("""
Use the sidebar to navigate through:
1. **Operations**
2. **Energy**
3. **Security**
4. **Market Intelligence**
5. **Emerging Tech**
""")

region = st.selectbox(
    "Select Data Center Region",
    ["Querétaro", "CDMX", "Monterrey"]
)

st.write(f"Showing data for: {region}")

df = load_market_data()

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "📥 Download Market Data",
    csv,
    "market_data.csv",
    "text/csv"
)

st.info("This project is designed for AWS ECS deployment using Docker, Terraform, and GitHub Actions.")