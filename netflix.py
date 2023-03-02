import streamlit as st
import numpy as np
import pandas as pd
import codecs

sidebar = st.sidebar
sidebar.image('credencial.jpg')
st.title('Netflix')
DATA_URL = ('movies.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")


sidebar.title("Itzel Mendez Martinez")
sidebar.write("Matricula: S20006761")
#
st.header("Dataset")
agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(data)

#
@st.cache
def load_data_film(names):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered_name = data[data['name'].str.contains(names)]

    return filtered_name

selected_title = sidebar.text_input("Select title of the film")
button_name = sidebar.button("Buscar titulo")

if(button_name):
    filtroname = load_data_film(selected_title)
    st.dataframe(filtroname)

st.markdown("___")

#
@st.cache
def load_data_bydirector(direct):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc)
    filtered = data[data['director'] == direct]

    return filtered

director_c = sidebar.selectbox("Select director", data['director'].unique())
btn_d = sidebar.button("Buscar director")

if(btn_d):
    filtro = load_data_bydirector(director_c)
    count_row = filtro.shape[0] 
    st.write(f"Total items : {count_row}")

    st.dataframe(filtro)

st.markdown("___")