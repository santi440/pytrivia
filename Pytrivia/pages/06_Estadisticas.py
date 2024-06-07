import streamlit as st
import FuncionesEstadisticas as fe
import matplotlib.pyplot as plt
from pathlib import Path

file_game = Path('..','Pytrivia','csv','resultado.csv')
file_players = Path('..','Pytrivia','csv','datosformularios.csv')

# Lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3','Opción 4', 'Opción 5', 'Opcion 6', 'Opcion 7', 'Opcion 8', 'Opcion 9', 'Opcion 10']

# Crear el selectbox
opcion_seleccionada = st.selectbox('Selecciona una opción:', opciones)

match opcion_seleccionada:
    case 'Opción 1':
        fe.graficar_genero(file_game,file_players)    
    case 'Opción 2':
        fe.graficar_porcentaje(file_game)
    case 'Opción 3':
        fe.grafico_dias(file_game)
    case 'Opción 4':
        fe.promedio_fechas(file_game)
    case 'Opción 5':
        fe.mejores(file_game)
    case 'Opcion 6':
        fe.estadistica_6(file_game)
    case 'Opcion 7':
        fe.estadistica_7(file_game)
    case 'Opcion 8':
        fe.estadistica_8(file_game, file_players)
    case 'Opcion 9':
        fe.estadistica_9(file_game)
    case 'Opcion 10':
        fe.estadistica_10(file_game)