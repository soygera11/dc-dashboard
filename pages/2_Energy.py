import streamlit as st
from utils.data_loader import load_csv
from utils.charts import line_chart, gauge_chart

st.title("Energy Efficiency")

df = load_csv("data/energy.csv")
last_row = df.iloc[-1]

c1, c2, c3 = st.columns(3)
c1.metric("Current PUE", f"{last_row['pue']:.2f}")
c2.metric("IT Load", f"{last_row['it_load_kw']} kW")
c3.metric("Energy Cost", f"${last_row['energy_cost_usd']:,}")

st.plotly_chart(line_chart(df, "month", "pue", "PUE Trend"), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(line_chart(df, "month", "it_load_kw", "IT Load (kW)"), use_container_width=True)

with col2:
    st.plotly_chart(line_chart(df, "month", "energy_cost_usd", "Monthly Energy Cost (USD)"), use_container_width=True)

st.markdown("### Interactive PUE Calculator")

facility_power = st.number_input("Total Facility Power (kW)", min_value=1.0, value=658.0, step=1.0)
it_power = st.number_input("IT Equipment Power (kW)", min_value=1.0, value=470.0, step=1.0)

if it_power > 0:
    pue_calc = facility_power / it_power
    st.success(f"Calculated PUE: **{pue_calc:.2f}**")
    st.plotly_chart(gauge_chart(pue_calc, "Calculated PUE", 1, 3), use_container_width=True)