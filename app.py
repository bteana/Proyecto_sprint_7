import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de datos de anuncios de venta de coches usados en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

dispert_button = st.checkbox('Calcular desviación estándar') # crear otro botón

if dispert_button:
    st.write('Creación de un gráfico de desviación estándar de los datos:')

    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) # crear gráfico de dispersión