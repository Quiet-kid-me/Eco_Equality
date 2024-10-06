import streamlit as st
import pandas as pd
st.title('🌍 Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data'):
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/refs/heads/main/data.csv')
  st.dataframe(df)
with st.expander('Map'):
  country_coordinates = {
    "Afghanistan": (33.93911, 67.709953),
    "Africa": (1.2921, 36.8219),  # This is a general point; adjust accordingly
    "Nepal": (28.3949, 84.1240),
}

# Create a new DataFrame for the map
map_data = pd.DataFrame(columns=["lat", "lon", "Value"])

# Populate the DataFrame with coordinates and values
for country, coords in country_coordinates.items():
    values = data[data['Country or Area'] == country]['Value'].astype(float).values
    for value in values:
        map_data = map_data.append({"lat": coords[0], "lon": coords[1], "Value": value}, ignore_index=True)

# Display the map
st.map(map_data)
