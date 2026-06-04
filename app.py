import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# carregar modelo
model = joblib.load("model.pkl")

st.title("🌊 Flood Risk Prediction")

st.write("Modelo de Machine Learning para previsão de enchentes.")

# inputs
rainfall = st.slider("Chuva (mm)", 0, 300)
river = st.slider("Nível do rio (m)", 1, 10)
soil = st.slider("Saturação do solo", 0, 100)
drain = st.slider("Capacidade de drenagem", 0, 100)
elev = st.slider("Altitude (m)", 0, 500)
urban = st.slider("Urbanização (%)", 0, 100)
temp = st.slider("Temperatura", 10, 40)
humidity = st.slider("Umidade", 30, 100)
wind = st.slider("Velocidade do vento", 0, 20)

# previsão
features = np.array([[rainfall, river, soil, drain, elev, urban, temp, humidity, wind]])
prediction = model.predict(features)

labels = ["Baixo", "Médio", "Alto"]

st.write("### Risco de enchente:", labels[prediction[0]])

# 📊 gráfico (AVALIAÇÃO VISUAL)
valores = [rainfall, river, soil, drain, elev, urban, temp, humidity, wind]
nomes = ["Chuva", "Rio", "Solo", "Drenagem", "Altitude", "Urbanização", "Temp", "Umidade", "Vento"]

fig, ax = plt.subplots()
ax.barh(nomes, valores)

st.pyplot(fig)