import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos 1
data = pd.read_csv('IMDB-Movie-Data.csv')

# Configuración de la página
st.set_page_config(layout="wide")

# Título de la aplicación
st.title('Análisis de Películas')

# Extraer géneros únicos
unique_genres = set()
data['Genre'].str.split(',').apply(unique_genres.update)
unique_genres = sorted(unique_genres)

# Sidebar: Filtros
st.sidebar.header('Filtros')
selected_genre = st.sidebar.selectbox('Seleccione el Género:', unique_genres)
min_year, max_year = int(data['Year'].min()), int(data['Year'].max())
year_range = st.sidebar.slider('Seleccione el Rango de Años:', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Aplicar filtros
filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
filtered_data = filtered_data[filtered_data['Genre'].str.contains(selected_genre, case=False, na=False)]

# Gráfico elaborado con Seaborn
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Rating', y='Revenue (Millions)', hue='Genre', style='Genre', s=100)
plt.title('Rating vs Revenue por Género')
plt.xlabel('Rating')
plt.ylabel('Revenue (Millions)')
st.pyplot(fig)

# Mostrar tabla dinámica
st.write("Películas seleccionadas y su Ingreso:")
st.dataframe(filtered_data[['Title', 'Revenue (Millions)']].sort_values(by='Revenue (Millions)', ascending=False))
