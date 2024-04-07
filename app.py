import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(
    page_title="World air quality chart",
    page_icon="🗺️",
    layout="centered",
)

st.title("☁︎World air quality☁︎")

st.divider()

st.write("Air quality is an emerging issue that poses a significant threat to our health. In this project, I have visualized air quality data from around the world to offer a comprehensive overview of the global air quality landscape.")
st.write("To facilitate user interaction and enable specific inquiries, I've incorporated multiple filters such as sliders, toggles, and dropdown menus, allowing users to narrow down their search to a particular country easily.")
st.write("Additionally, the application features a map and displays various types of pollutants, enhancing the understanding of air quality dynamics and its implications on public health.")

st.divider()

# Assuming the file path is correct and the CSV format is valid
df = pd.read_csv("openaq.csv", sep=';')

# Slider for selecting a range of air quality values
min_value, max_value = st.slider(
    "Value(µg/m³)",
    0.0,  # Minimum value
    3000.0,  # Maximum value
    (25.0, 300.0)  # Default range
)

# Dropdown for selecting a country
country_label = ['All'] + sorted(df['Country Label'].dropna().unique())
selected_country_label = st.selectbox(
   "What country do you want to choose?",
   options=country_label,
   index=0,
   help="Select a country code to filter the air quality data."
)
st.write('You selected:', selected_country_label)

# Initial filtering based on country selection
if selected_country_label != 'All':
    df = df[df['Country Label'] == selected_country_label]

# Further filtering based on air quality value range
df = df[(df['Value'] >= min_value) & (df['Value'] <= max_value)]

st.divider()

col1, col2 = st.columns([0.65, 0.35])

with col1:
    on = st.toggle('Hide unknown cities')

    if on:
        df = df[df['City'].notna() & (df['City'] != '')]
        st.write("Unknown cities hidden successfully!")

with col2:
    st.subheader(f"Total: {len(df)} cities")

# Display the filtered dataframe
st.write(df)

st.divider()

st.subheader("🗺️Map of data been collected🗺️")
# Assuming your 'Coordinates' column is in 'latitude,longitude' format
# Split the 'Coordinates' column into two new columns: 'lat' and 'lon'
df[['lat', 'lon']] = df['Coordinates'].str.split(',', expand=True)

# Convert 'lat' and 'lon' columns to numeric values, errors='coerce' will set invalid parsing to NaN
df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

# Remove rows where either 'lat' or 'lon' is NaN
df = df.dropna(subset=['lat', 'lon'])

st.map(df[['lat', 'lon']])

# Example pollutants data
pollutants_data = pd.DataFrame({
    "Pollutant": ["CO", "O3", "NO2", "SO2", "PM2.5"],
    "Value (µg/m³)": np.random.uniform(low=0, high=3000, size=5)  # Generate random data for illustration
})

# Create an Altair chart
chart = alt.Chart(pollutants_data).mark_bar().encode(
    x=alt.X('Pollutant', sort=None),  # Prevent sorting to maintain the order
    y=alt.Y('Value (µg/m³)', scale=alt.Scale(domain=(0, 3000))),  # Specify the scale's domain for y-axis
    color='Pollutant'  # Color bars by pollutant type
).properties(
    title='Pollutant Values in µg/m³'
)

st.divider()

st.subheader("📊Data of pollutant in the selected country📊")

# Dropdown for selecting a country
country_label =  sorted(df['Country Label'].dropna().unique())
selected_country_label = st.selectbox(
   "What country do you want to choose?",
   options=country_label,
   index=0,
   help="Select a country code to filter the air quality data."
)
st.write('You selected:', selected_country_label)

df = df[df['Country Label'] == selected_country_label]


col1, col2 = st.columns([0.65, 0.35])

with col1:
    st.altair_chart(chart, use_container_width=True)

with col2:
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")    
    st.table(pollutants_data)
