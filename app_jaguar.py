import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Monitoreo y Riesgo - Panthera Onca", layout="wide")

st.title("🐾 Dashboard de Monitoreo y Auditoría Ética: Panthera onca")
st.markdown("### Proyecto de Recuperación y Mejora Continua en Ciencia de Datos")

# Sidebar
st.sidebar.header("Filtros de Monitoreo")
zona = st.sidebar.selectbox("Selecciona la Zona de Monitoreo", ["Todas", "Zona Norte", "Zona Centro", "Zona Sur"])

# Crear datos simulados rápidos
np.random.seed(42)
n = 200
data = pd.DataFrame({
    'Distancia_Carreteras': np.random.uniform(0.1, 15.0, n),
    'Temperatura_Media': np.random.uniform(18.0, 32.0, n),
    'NDVI_Vegetacion': np.random.uniform(0.2, 0.9, n),
    'Nivel_Riesgo': np.random.choice(['Bajo', 'Medio', 'Alto'], size=n, p=[0.3, 0.4, 0.3])
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ Mapa / Gráfico de Riesgo Antropogénico")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=data, x='Distancia_Carreteras', y='NDVI_Vegetacion', hue='Nivel_Riesgo', palette='Set1', ax=ax)
    ax.set_title("Relación NDVI vs. Distancia a Carreteras")
    st.pyplot(fig)

with col2:
    st.subheader("⚖️ Resultados de Auditoría Ética (Sesgo)")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.countplot(data=data, x='Nivel_Riesgo', palette='viridis', ax=ax2)
    ax2.set_title("Distribución de Muestreos por Nivel de Riesgo")
    st.pyplot(fig2)

st.success("Aplicación desplegada exitosamente para la toma de decisiones de conservación.")