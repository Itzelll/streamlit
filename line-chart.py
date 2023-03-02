import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame( #data frame de un array
     np.random.randn(100, 5), #matriz 20 filas, 3 columnas
     columns=['a', 'b', 'c', 'd', 'e'])

st.line_chart(chart_data)

st.dataframe(chart_data)