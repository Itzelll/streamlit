import streamlit as st

st.title("Mi primera App con Streamlit")

sidebar = st.sidebar

sidebar.title("Esta es la barra lateral.")
sidebar.write("Datos del sidebar")

st.header("Header 1")
st.header("Header 2")
st.write("Datos del contenido")
