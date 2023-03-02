import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

titanic_link = 'https://raw.githubusercontent.com/adsoftsito/nosql/main/csv/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots() #objeto de grafica

#ax.hist(titanic_data.age)
ax.hist(titanic_data['class']) #datos que queremos graficar en el histograma

st.header("Histograma del Titanic") #un encabezado

st.pyplot(fig) #para que imprima la grafica
st.markdown("___")

st.dataframe(titanic_data)