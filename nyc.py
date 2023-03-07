import streamlit as st
import numpy as np
import pandas as pd
import codecs
import matplotlib.pyplot as plt

st.title('Recorridos en bicicleta en NYC')
DATE_COLUMN = 'started_at'
DATA_URL = ('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    doc = codecs.open(DATA_URL, 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat':'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #la fecha lo vuelve string
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text("Done!")

sidebar = st.sidebar
sidebar.image('uv.jpg')
sidebar.title("Itzel Mendez Martinez")
sidebar.write("Matricula: S20006761")
sidebar.write("zs20006761@estudiantes.uv.mx")
sidebar.markdown("___")

#Dataset
st.header("Dataset")
agree = sidebar.checkbox("Selecciona para mostrar el dataset")
if agree:
  st.dataframe(data)

#HISTOGRAMA RECORRIDOS
st.header("Grafica de barras")
agree = sidebar.checkbox("Recorridos por hora")
if agree:
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
    

#Horas
hour_to_filter = sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de recorridos iniciados a las %s:00' % hour_to_filter)
st.map(filtered_data)