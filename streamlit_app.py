import streamlit as st
import pandas as pd
st.title('🌍 Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
with st.expander('Data'):
  st.write('Raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/Quiet-kid-me/women_anemia/refs/heads/main/data.csv')
  st.dataframe(df)
with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='Unit', y='Value', color='Country or Area')
