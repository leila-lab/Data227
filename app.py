import streamlit as st

st.set_page_config(
    page_title="Seattle Weather Narrative Visualization",
    layout="wide"
)

st.title("Seattle Weather: A Narrative Visualization")

st.write("""
This project demonstrates a **narrative visualization** using charts created
with **Altair** and deployed using **Streamlit**.

The goal of this project is to guide the reader through patterns in Seattle's
daily weather data through a combination of visual evidence and explanation.
""")

st.write("""
### How to Navigate This Story

To explore the data story, use the pages in the sidebar:

**Central Narrative**  
We begin by examining daily weather patterns over time to understand
seasonal temperature trends.

**Exploration**  
Readers can interact with the data through several visualizations to
investigate how temperature varies across different weather conditions.

**Methodology**  
Finally, we describe the dataset used in this analysis and discuss
some limitations of the data.
""")