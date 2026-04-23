import streamlit as st

st.set_page_config(
    page_title="QRO Nexus DC Intelligence",
    page_icon="🏢",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
[data-testid="stMetricValue"] {
    font-size: 1.6rem;
}
</style>
""", unsafe_allow_html=True)

st.title("QRO Nexus DC Intelligence")
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
col3.metric("Primary Region", "Querétaro")
col4.metric("Dashboard Mode", "Executive")

st.markdown("### Pages")
st.markdown("""
Use the sidebar to navigate through:
1. **Operations**
2. **Energy**
3. **Security**
4. **Market Intelligence**
5. **Emerging Tech**
""")

st.info("This project is designed for AWS ECS deployment using Docker, Terraform, and GitHub Actions.")