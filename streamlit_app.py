import streamlit as st
import pandas as pd
st.title('Eco_Equality')
st.info('This app shows the number of women in reproductive age having anemia.')
df = pd.read_csv('https://github.com/Quiet-kid-me/women_anemia/blob/main/UNdata_Export_20241005_161251297.csv')
