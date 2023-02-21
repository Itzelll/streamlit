import streamlit as st
import pandas as pd

st.title('Streamlit - Search names')

DATA_URL = ("https://firebasestorage.googleapis.com/v0/b/streamlit-1-37f46.appspot.com/o/csv%2Fitzel%2Fdataset.csv?alt=media&token=54f7c0af-3a11-43d1-ac04-ce3e28fd4e6c")

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL) #read csv
    filtered_data_byrange = data[(data['index'] >= startid) & (data['index']<= endid)]

    return filtered_data_byrange

startid = st.text_input('Start index :')
endid = st.text_input('End index :')
btnRange = st.button('Search by range')

if (btnRange):
    filterbyrange = load_data_byrange(int(startid), int(endid))
    count_row = filterbyrange.shape[0] #Gives number of rows
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbyrange)