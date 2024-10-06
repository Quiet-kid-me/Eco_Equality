import streamlit as st
import pandas as pd
st.title('🌍 Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data'):
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/main/UNdata_Export_20241005_161251297.csv')
  st.dataframe(df)
with st.expander('Map'):
# Load a separate dataset with country latitudes and longitudes
country_lat_long = pd.read_csv('country_lat_long.csv')

# Merge the two datasets on country names
merged_df = pd.merge(df, country_lat_long, left_on='Country or Area', right_on='country')

# Prepare the data for mapping
map_df = merged_df.pivot_table(index='country', values='Value', aggfunc='mean')

# Create the map using st.map
st.map(map_df, lat='latitude', lon='longitude')
