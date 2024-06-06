import streamlit as st
import FuncionesEstadisticas as fe
import matplotlib.pyplot as plt
from pathlib import Path

file_game = Path('..','Pytrivia','Csv','resultado.csv')
file_players = Path('..','Pytrivia','Csv','datos_formularios.csv')

# Lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3', 'Opcion 6', 'Opcion 7', 'Opcion 8', 'Opcion 9']

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
    case 'Opcion 6':
        fe.estadistica_6(file_game)
    case 'Opcion 7':
        fe.estadistica_7(file_game)
    case 'Opcion 8':
        fe.estadistica_8(file_game, file_players)
    case 'Opcion 9':
        fe.estadistica_9(file_game)