import streamlit as st
import pandas as pd

st.title('Streamlit - Filter by sex')

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/streamlit-1-37f46.appspot.com/o/csv%2Fitzel%2Fdataset.csv?alt=media&token=54f7c0af-3a11-43d1-ac04-ce3e28fd4e6c')

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['sex'] == sex]

    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select Sex", data['sex'].unique())
btnFilterbySex = st.button('Filter by Sex')

if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0] #Gives number of rows
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbysex)