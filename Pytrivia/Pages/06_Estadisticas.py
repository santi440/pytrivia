import streamlit as st
import FuncionesEstadisticas as fe
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
        grafico = fe.graficar_genero(file_game,file_players)
        st.pyplot(plt.gcf())
    case 'Opción 2':
        grafico = fe.graficar_porcentaje(file_game)
        st.plotly_chart(grafico)
    case 'Opción 3':
        grafico = fe.grafico_dias(file_game)
        st.pyplot(plt.gcf())