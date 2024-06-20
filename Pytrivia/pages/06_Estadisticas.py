import streamlit as st
import FuncionesEstadisticas as fe
from pathlib import Path

file_game = Path('..','Pytrivia','csv','resultado.csv')
file_players = Path('..','Pytrivia','csv','datos_formularios.csv')

# Lista de opciones
opciones = ['Jugadores que jugaron por género', 
            'Jugadores que superan la media', 
            'Cantidad de partidas por dia de la semana',
            'Promedio de respuestas correctas por meses', 
            'Top 10 de usuarios con mayor cantidad de puntos acumulados', 
            'Ordenar temáticas por dificultad', 
            'Comparar puntaje de dos jugadores', 
            'Temática con más conocimiento por género', 
            'Informacion de puntaje de cada dificultad', 
            'Usuarios en racha']

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
    case 'Ordenar temáticas por dificultad':
        fe.dificultad_datasets(file_game)
    case 'Comparar puntaje de dos jugadores':
        fe.comparar_dos_usuarios(file_game)
    case 'Temática con más conocimiento por género':
        fe.tematica_por_genero(file_game, file_players)
    case 'Informacion de puntaje de cada dificultad':
        fe.info_dificultades(file_game)
    case 'Usuarios en racha':
        fe.usuarios_en_racha(file_game)