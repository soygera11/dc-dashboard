import streamlit as st
from utils.data_loader import load_csv
from utils.charts import bar_chart

st.title("Emerging Technologies")

df = load_csv("data/emerging_tech.csv")

st.plotly_chart(
    bar_chart(df, "technology", "adoption_score", "Technology Adoption Score"),
    use_container_width=True
)

st.markdown("### Adoption Timeline")
st.dataframe(df.sort_values("target_year"), use_container_width=True)

top_tech = df.sort_values("adoption_score", ascending=False).iloc[0]
st.success(
    f"Priority recommendation: Focus first on **{top_tech['technology']}**, "
    f"with a target deployment by **{top_tech['target_year']}**."
)