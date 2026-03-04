import streamlit as st
from utils.io import load_weather
from charts.charts import (
    temp_timeseries,
    seasonality_boxplot,
    extreme_heat,
    precip_vs_temp
)

df = load_weather()

st.title("Seattle Weather Story")

# Chart 1
st.header("Daily Temperature Over Time")

st.write("""
We begin by examining Seattle's daily maximum temperature over time.
This allows us to observe seasonal patterns throughout the year.
""")

st.altair_chart(temp_timeseries(df), use_container_width=True)

st.caption("Takeaway: Seattle temperatures clearly follow seasonal cycles.")


# Chart 2
st.header("Seasonal Temperature Variation")

st.write("""
Next we compare temperature distributions across months.
This reveals how temperature varies seasonally.
""")

st.altair_chart(seasonality_boxplot(df), use_container_width=True)

st.caption("Takeaway: Summer months show higher temperature distributions.")


# Chart 3
st.header("Extreme Heat Events")

st.write("""
Although Seattle generally has mild weather, there are occasional
extreme heat events that stand out in the dataset.
""")

st.altair_chart(extreme_heat(df), use_container_width=True)

st.caption("Takeaway: Extreme hot days are rare but noticeable outliers.")


# Chart 4
st.header("Temperature and Precipitation")

st.write("""
Finally, we examine the relationship between temperature and precipitation
to see how rainfall varies with temperature conditions.
""")

st.altair_chart(precip_vs_temp(df), use_container_width=True)

st.caption("Takeaway: Rainfall tends to occur at moderate temperatures.")