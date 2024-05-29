import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('IMDB-Movie-Data.csv')

# Título de la aplicación
st.title('Análisis de Películas')

# Extraer géneros únicos
unique_genres = set()
data['Genre'].str.split(',').apply(unique_genres.update)
unique_genres = sorted(unique_genres)

# Lista desplegable para género
selected_genre = st.sidebar.selectbox('Seleccione el Género:', unique_genres)

# Slider de año
min_year, max_year = int(data['Year'].min()), int(data['Year'].max())
year_range = st.sidebar.slider('Seleccione el Rango de Años:', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Aplicar filtros
filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
filtered_data = filtered_data[filtered_data['Genre'].str.contains(selected_genre, case=False, na=False)]

# Gráfico
fig, ax = plt.subplots()
ax.scatter(filtered_data['Rating'], filtered_data['Revenue (Millions)'])
ax.set_xlabel('Rating')
ax.set_ylabel('Revenue (Millions)')
ax.set_title('Rating vs Revenue')
st.pyplot(fig)

# Mostrar tabla dinámica
st.write("Películas seleccionadas y su Ingreso:")
st.dataframe(filtered_data[['Title', 'Revenue (Millions)']])
