import pandas as pd
import streamlit as st
from vega_datasets import data

@st.cache_data
def load_weather():
    df = data.seattle_weather()
    return df
