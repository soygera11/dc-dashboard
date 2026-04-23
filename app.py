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
/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #020817 0%, #06152b 100%);
    color: #ffffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827 !important;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* Tarjetas de métricas */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #162033 0%, #1d2b45 100%);
    border: 1px solid #3d5a80;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
}

[data-testid="stMetricLabel"] {
    color: #9ec5fe !important;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 2.1rem !important;
    font-weight: 800;
}

/* Selectbox label */
[data-testid="stWidgetLabel"] p,
label, .stSelectbox label {
    color: #ffffff !important;
    font-weight: 600;
}

/* Caja cerrada del select */
[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

/* Texto dentro del select */
[data-baseweb="select"] span,
[data-baseweb="select"] div {
    color: #ffffff !important;
}

/* Menú desplegable */
div[role="listbox"] {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #334155 !important;
}

/* Opciones del menú */
div[role="option"] {
    background-color: #1e293b !important;
    color: #ffffff !important;
}

/* Hover y opción seleccionada */
div[role="option"]:hover,
div[aria-selected="true"] {
    background-color: #334155 !important;
    color: #ffffff !important;
}

/* Inputs en general */
input, textarea {
    color: #ffffff !important;
}

/* Texto general */
p, li, div {
    color: #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* texto de opciones del dropdown */
div[role="option"] span {
    color: #ffffff !important;
}

/* texto interno del popup */
div[role="listbox"] * {
    color: #ffffff !important;
}

/* fondo de las opciones */
div[role="option"] {
    background-color: #1e293b !important;
}

/* hover */
div[role="option"]:hover {
    background-color: #334155 !important;
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