import streamlit as st
import pandas as pd
st.title('Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data')
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/main/UNdata_Export_20241005_161251297.csv')
  st.dataframe(df)
