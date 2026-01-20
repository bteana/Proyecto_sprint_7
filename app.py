import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de datos de anuncios de venta de coches usados en EE.UU.') # Título de la aplicación

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_data['brand'] = car_data['model'].str.split().str[0] # extraer la marca del modelo

st.header("Visor de datos - Vehiculos usados en US") # Encabezado

show_missing = st.checkbox("Mostrar filas con valores faltantes", value=True) # Checkbox

if show_missing: # Filtro
    filtered_data = car_data
else:
    filtered_data = car_data.dropna()

columns = st.multiselect(
    "Seleccionar columnas para mostrar",
    options=filtered_data.columns.tolist(),
    default=[
        "cylinders", "fuel", "odometer",
        "transmission", "type",
        "paint_color", "is_4wd"
    ]
) # Selección de columnas del checkbox

st.dataframe(filtered_data[columns]) # Mostrar tabla

st.header("Distribución del kilometraje de los vehículos usados") # Encabezado

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

st.header("Desviación estándar") # Encabezado

dispert_button = st.checkbox('Calcular desviación estándar') # crear otro botón

if dispert_button:
    st.write('Creación de un gráfico de desviación estándar de los datos:')

    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) # crear gráfico de dispersión

st.header("Vehículos por marca y tipo de transmisión")

brand_transmission = (
    car_data
    .groupby(['brand', 'transmission'])
    .size()
    .reset_index(name='count')
) # agrupar por marca y tipo de transmisión

fig = px.bar(
    brand_transmission,
    x='brand',
    y='count',
    color='transmission',
    barmode='group',
)

st.plotly_chart(fig, use_container_width=True) # mostrar gráfico de barras