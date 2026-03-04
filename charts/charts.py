import altair as alt

# 1. Time-series chart (opening hook)
def temp_timeseries(df):

    chart = alt.Chart(df).mark_line().encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("temp_max:Q", title="Maximum Temperature (°C)"),
        tooltip=["date:T", "temp_max"]
    ).properties(
        title="Maximum Temperature in Seattle Over Time"
    )

    return chart


# 2. Seasonality boxplot
def seasonality_boxplot(df):

    chart = alt.Chart(df).mark_boxplot().encode(
        x=alt.X("month(date):O", title="Month"),
        y=alt.Y("temp_max:Q", title="Maximum Temperature (°C)")
    ).properties(
        title="Seasonal Temperature Variation"
    )

    return chart


# 3. Extreme heat days (outliers)
def extreme_heat(df):

    import altair as alt

    # Calculate 99th percentile threshold
    threshold = df["temp_max"].quantile(0.99)

    # Base scatterplot (all points)
    base = alt.Chart(df).mark_circle(
        size=40,
        color="lightgray",
        opacity=0.6
    ).encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y("temp_max:Q", title="Daily max temp (°C)")
    )

    # Highlight extreme days
    extreme = alt.Chart(df[df["temp_max"] >= threshold]).mark_circle(
        size=70,
        color="red"
    ).encode(
        x="date:T",
        y="temp_max:Q",
        tooltip=["date:T", "temp_max"]
    )

    # Threshold line
    rule = alt.Chart(df).mark_rule(
        color="black",
        strokeDash=[6,6]
    ).encode(
        y=alt.datum(threshold)
    )

    chart = (base + rule + extreme).properties(
        title="Extremely Hot Days"
    )

    return chart

# 4. Precipitation vs temperature relationship
def precip_vs_temp(df):

    chart = alt.Chart(df).mark_circle(opacity=0.5).encode(
        x=alt.X("temp_max:Q", title="Maximum Temperature"),
        y=alt.Y("precipitation:Q", title="Precipitation"),
        color="weather:N",
        tooltip=["date:T", "temp_max", "precipitation", "weather"]
    ).properties(
        title="Temperature vs Precipitation"
    )

    return chart