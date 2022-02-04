import streamlit as st
import pandas as pd
import numpy as np

st.title('Caribou Release')

st.text('260 woodland caribou were tagged in British Columbia. Find out where they were released.')
st.text('This data comes from: BC Ministry of Environment (2014)')
DATA_URL = ('https://raw.githubusercontent.com/jieunyoo/caribou-tracking/main/Caribou.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(153)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

gender = st.radio('select a gender', ('m', 'f'))

filtered_data = data[data['sex'] == gender]
st.map(filtered_data)
