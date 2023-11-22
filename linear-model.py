import streamlit as st
import requests
import json
import numpy as np

# La URL del servidor especifica el endpoint del modelo "linear_model"
# con el nombre "linear-model" y utilizando la interfaz de predicción "predict".
SERVER_URL = 'https://linear-model-service-itzelll.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(input_values):
    payload = {'instances': [[value] for value in input_values]}
    print("Payload:", payload)
    response = requests.post(SERVER_URL, data=json.dumps(payload))
    response.raise_for_status()
    prediction = response.json()
    return prediction


def main():
    st.title("Linear Model Prediction App")

    # Capturar tres valores de entrada
    input_value1 = st.number_input("Ingrese el primer valor a predecir", value=0.0)
    input_value2 = st.number_input("Ingrese el segundo valor a predecir", value=0.0)
    input_value3 = st.number_input("Ingrese el tercer valor a predecir", value=0.0)

    if st.button("Realizar predicción"):
        # Hacer la predicción
        input_values = input_value1, input_value2, input_value3
        prediction = make_prediction(input_values)

        # Mostrar la predicción
        st.success(f"Predicción: {np.argmax(prediction['predictions'])}")

        # Mostrar la respuesta de la API (opcional)
        st.write(f"Respuesta de la API: {prediction}")


if __name__ == '__main__':
    main()
