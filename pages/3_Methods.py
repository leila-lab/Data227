import streamlit as st

st.title("Methods")

st.write("""
### Data source
This analysis uses the Seattle Weather dataset from the Vega Datasets
collection. The dataset contains daily weather observations in Seattle.

### Variables
The dataset includes several variables used in this analysis:

- **date** – date of observation
- **temp_max** – maximum daily temperature
- **temp_min** – minimum daily temperature
- **precipitation** – rainfall amount
- **wind** – wind speed
- **weather** – general weather classification (rain, sun, fog, etc.)

### Visualization approach
The goal of this project is to explore patterns in Seattle weather
through narrative visualization. The story begins with a time-series
view showing seasonal temperature patterns. The Explore page allows
users to interactively examine how temperature distributions differ
across weather types.

### Limitations
This dataset only contains weather observations from Seattle and does
not represent broader climate patterns. Additionally, the weather
categories are simplified labels and may not capture all meteorological
conditions.
""")