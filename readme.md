## Techin 510_Lab2
This Lab2 is a practice of using Streamlit to analyze and vsualize data.

## Overview
```
Air quality is an emerging issue that poses a significant threat to our health. In this project, I have visualized air quality data from around the world to offer a comprehensive overview of the global air quality landscape. 
To facilitate user interaction and enable specific inquiries, I've incorporated multiple filters such as sliders, toggles, and dropdown menus, allowing users to narrow down their search to a particular country easily. 
Additionally, the application features a map and displays various types of pollutants, enhancing the understanding of air quality dynamics and its implications on public health.
```

## Getting started
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## What's included
```
- A text widget about the description of this code
- A slider filter to adjust pollutant value range
- A toggle filter to enable hide rows with unreadable values
- Two drop down filter for select contry informations
- One map to show where the air quaility data has been collected worldwidely.
- One chart and table to show the pollutant values in according to the pollutant type, like CO, O3, NO2, SO2, PM2.5.
```

## What I learned
```
- Formatting existing CSV, such as change Delimiters in panda chart to comma, add more column, extract data.
- Apply multiple filters to display data, such as use slider, dropdown box, or check boxes. 
- The new chart tool altair to display complex data
- How to use maps to visualize the location by using its coordinates.
- Apply complex color codes for data visualization, instead of simple name like red, yellow. 

```

## Questions
```
- If the format of chart is not correct format, especially for special data like time, how to edit this data?
- How to show more complex data in map, like show different pollutant type in different colors?
- Since the data are collected in different time, how can I only show the up to date date for one country instead of showing all datas?
```