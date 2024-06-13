import streamlit as st
import FuncionesEstadisticas as fe
import matplotlib.pyplot as plt
from pathlib import Path

file_game = Path('..','Pytrivia','csv','resultado.csv')
file_players = Path('..','Pytrivia','csv','datos_formularios.csv')

# Lista de opciones
opciones = ['Jugadores que jugaron por género', 'Jugadores que superan la media', 'Cantidad de partidas por dia de la semana','Promedio de respuestas correctas por meses', 'Top 10 de usuarios con mayor cantidad de puntos acumulados', 'Opcion 6', 'Opcion 7', 'Opcion 8', 'Opcion 9', 'Opcion 10']

# Crear el selectbox
opcion_seleccionada = st.selectbox('Selecciona una opción:', opciones)

match opcion_seleccionada:
    case 'Jugadores que jugaron por género':
        fe.graficar_genero(file_game,file_players)    
    case 'Jugadores que superan la media':
        fe.graficar_porcentaje(file_game)
    case 'Cantidad de partidas por dia de la semana':
        fe.grafico_dias(file_game)
    case 'Promedio de respuestas correctas por meses':
        fe.promedio_fechas(file_game)
    case 'Top 10 de usuarios con mayor cantidad de puntos acumulados':
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