import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('IMDB-Movie-Data.csv')

# Título de la aplicación
st.title('Análisis de Películas')

# Filtros
year_filter = st.sidebar.multiselect('Seleccione el Año:', options=data['Year'].unique())
genre_filter = st.sidebar.multiselect('Seleccione el Género:', options=data['Genre'].unique())

# Aplicar filtros
filtered_data = data
if year_filter:
    filtered_data = filtered_data[filtered_data['Year'].isin(year_filter)]
if genre_filter:
    filtered_data = filtered_data[filtered_data['Genre'].isin(genre_filter)]

# Gráfico
fig, ax = plt.subplots()
ax.scatter(filtered_data['Rating'], filtered_data['Revenue (Millions)'])
ax.set_xlabel('Rating')
ax.set_ylabel('Revenue (Millions)')
ax.set_title('Rating vs Revenue')
st.pyplot(fig)
