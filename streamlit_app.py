import streamlit as st
import pandas as pd
st.title('🌍 Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data'):
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/refs/heads/main/data.csv')
  st.dataframe(df)
# Sample data in a DataFrame
data = {
    "Country or Area": [
        "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan",
        "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan",
        "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan",
        "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan",
        "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa", "Africa",
        "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal",
        "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal", "Nepal",
        "Nepal", "Nepal", "Nepal", "Nepal", "Nepal"
    ],
    "Value": [
        3.80, 3.60, 3.40, 3.20, 3.00,
        2.90, 2.70, 2.50, 2.40, 2.30,
        2.20, 2.10, 2.00, 2.00, 1.90,
        1.80, 1.70, 1.70, 1.60, 1.50,
        122.70, 119.10, 115.90, 112.90, 110.20,
        107.60, 105.20, 103.10, 101.20, 99.70,
        98.30, 97.10, 96.00, 94.70, 93.40,
        91.80, 90.10, 88.30, 15.80, 85.10,
        3.20, 3.10, 3.00, 2.90, 2.80,
        2.70, 2.70, 2.60, 2.60, 2.60,
        2.50, 2.50, 2.50, 2.50, 2.50,
        2.50, 2.60, 2.60, 2.60, 2.60
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Coordinates for mapping (latitude, longitude)
coords = {
    "Afghanistan": [33.93911, 67.709953],  # Approximate center of Afghanistan
    "Africa": [1.2921, 36.8219],  # Approximate center of Africa (East Africa)
    "Nepal": [28.3949, 84.1240]  # Approximate center of Nepal
}

# Extracting latitude and longitude
df['Latitude'] = df['Country or Area'].map(lambda x: coords[x][0])
df['Longitude'] = df['Country or Area'].map(lambda x: coords[x][1])

# Create a map
st.title("Country Data Map")
st.map(df[['Latitude', 'Longitude', 'Value']])
