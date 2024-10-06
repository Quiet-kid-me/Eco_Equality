import streamlit as st
import pandas as pd
st.title('🌍 Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data'):
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/refs/heads/main/data.csv')
  st.dataframe(df)
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
