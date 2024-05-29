import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('IMDB-Movie-Data.csv')

# Título de la aplicación
st.title('Análisis de Películas')

# Filtro de género
genre_filter = st.sidebar.multiselect('Seleccione el Género:', options=data['Genre'].unique())

# Slider de año
min_year, max_year = int(data['Year'].min()), int(data['Year'].max())
year_range = st.sidebar.slider('Seleccione el Rango de Años:', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Aplicar filtros
filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
if genre_filter:
    filtered_data = filtered_data[filtered_data['Genre'].str.contains('|'.join(genre_filter))]

# Gráfico
fig, ax = plt.subplots()
ax.scatter(filtered_data['Rating'], filtered_data['Revenue (Millions)'])
ax.set_xlabel('Rating')
ax.set_ylabel('Revenue (Millions)')
ax.set_title('Rating vs Revenue')
st.pyplot(fig)
