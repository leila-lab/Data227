import streamlit as st
import altair as alt
from utils.io import load_weather

df = load_weather()

st.title("Explore Seattle Weather")

st.write("""
This chart shows how maximum temperature varies across different
weather conditions.
""")

chart = alt.Chart(df).mark_boxplot().encode(
    x=alt.X("weather:N", title="Weather Type"),
    y=alt.Y("temp_max:Q", title="Maximum Temperature (°C)"),
    color="weather:N"
).properties(
    title="Temperature Distribution by Weather Condition"
)

st.altair_chart(chart, use_container_width=True)