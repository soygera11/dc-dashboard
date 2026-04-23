import streamlit as st
from utils.data_loader import load_market_data
from utils.charts import line_chart, bar_chart

st.title("Operations Dashboard")

df = load_market_data("data/operations.csv")

last_row = df.iloc[-1]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Current Uptime SLA", f"{last_row['uptime_sla']:.2f}%")
c2.metric("Open Incidents", int(last_row["open_incidents"]))
c3.metric("Closed Changes", int(last_row["closed_changes"]))
c4.metric("Rack Utilization", f"{last_row['rack_utilization']}%")

st.plotly_chart(line_chart(df, "month", "uptime_sla", "Monthly Uptime SLA"), use_container_width=True)

col_a, col_b = st.columns(2)
with col_a:
    st.plotly_chart(bar_chart(df, "month", "open_incidents", "Open Incidents by Month"), use_container_width=True)

with col_b:
    st.plotly_chart(bar_chart(df, "month", "rack_utilization", "Rack Utilization Trend"), use_container_width=True)

st.markdown("### MAC Process Summary")
st.dataframe(df[["month", "closed_changes", "service_requests"]], use_container_width=True)