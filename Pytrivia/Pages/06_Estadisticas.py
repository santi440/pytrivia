import streamlit as st
from FuncionesEstadisticas import *
import matplotlib.pyplot as plt
from pathlib import Path

file_game = Path('..','Pytrivia','Csv','resultado.csv')
file_players = Path('..','Pytrivia','Csv','datos_formularios.csv')

# Lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3']

# Crear el selectbox
opcion_seleccionada = st.selectbox('Selecciona una opción:', opciones)

match opcion_seleccionada:
    case 'Opción 1':
        grafico = punto1.graficar_genero(file_game,file_players)
        st.pyplot(plt.gcf())
    case 'Opción 2':
        grafico = punto2.graficar_porcentaje(file_game)
        st.plotly_chart(grafico)
    case 'Opción 3':
        grafico = punto3.grafico_dias(file_game)
        st.pyplot(plt.gcf())