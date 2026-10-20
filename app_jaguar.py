import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Monitoreo y Riesgo - Panthera Onca", layout="wide")

st.title("Dashboard de Monitoreo y Auditoría Ética: Panthera onca")
st.markdown("### Proyecto de Recuperación y Mejora Continua en Ciencia de Datos")

# Sidebar
st.sidebar.header("Filtros de Monitoreo")
zona = st.sidebar.selectbox("Selecciona la Zona de Monitoreo", ["Todas", "Zona Norte", "Zona Sur"])

# Crear datos simulados
np.random.seed(42)
n = 200
data = pd.DataFrame({
    'Distancia_Carreteras': np.random.uniform(0.1, 15.0, n),
    'NDVI_Vegetacion': np.random.uniform(0.2, 0.95, n),
    'Nivel_Riesgo': np.random.choice(['Bajo', 'Medio', 'Alto'], size=n, p=[0.35, 0.45, 0.20]),
    'Zona': np.random.choice(["Zona Norte", "Zona Sur"], size=n)
})

if zona != "Todas":
    data = data[data['Zona'] == zona]

# Gráfica 1: Scatter plot
st.subheader(" Mapa / Gráfico de Riesgo Antropogénico")
st.markdown("*Relación NDVI vs. Distancia a Carreteras*")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=data, 
    x='Distancia_Carreteras', 
    y='NDVI_Vegetacion', 
    hue='Nivel_Riesgo', 
    hue_order=['Bajo', 'Medio', 'Alto'],
    palette={'Bajo': 'tab:blue', 'Medio': 'tab:green', 'Alto': 'tab:red'}, 
    ax=ax1
)
ax1.set_xlabel("Distancia_Carreteras")
ax1.set_ylabel("NDVI_Vegetacion")
st.pyplot(fig1)

# Gráfica 2: Count plot
st.subheader("Resultados de Auditoría Ética (Sesgo)")
st.markdown("*Distribución de Muestreos por Nivel de Riesgo*")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.countplot(
    data=data, 
    x='Nivel_Riesgo', 
    order=['Bajo', 'Medio', 'Alto'],
    palette={'Bajo': 'tab:blue', 'Medio': 'tab:cyan', 'Alto': 'tab:green'}, 
    ax=ax2
)
ax2.set_xlabel("Nivel_Riesgo")
ax2.set_ylabel("count")
st.pyplot(fig2)
    
