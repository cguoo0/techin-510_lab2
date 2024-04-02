import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="World air quality chart",
    page_icon="🗺️",
    layout="centered",
)

st.title("☁︎World air quality☁︎")

df = pd.read_csv("/Users/guochenxi/Desktop/techin510_lab 2/openaq.csv", sep=';')

Air_Quality_Value_slider = st.slider(
    "Value(µg/m³)"
)
st.write(df)

