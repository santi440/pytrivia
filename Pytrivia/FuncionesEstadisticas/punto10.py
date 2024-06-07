import pandas as pd
from datetime import datetime, timedelta
import streamlit as st
from pathlib import Path

def estadistica_10(plays_route):
    '''
    Lista los usuarios que registran una partida con un puntaje mayor a cero en todos 
    los días durante los últimos 7.

        Args: Recibe la ruta del dataset de jugadas.
    '''

    file = pd.read_csv(plays_route)

    # Convertir la columna 'Fecha y hora' a tipo datetime 
    file['Fecha y hora'] = pd.to_datetime(file['Fecha y hora'])

    # Fecha actual
    actual_date = datetime.now()

    # Fecha actual restandole 7 dias
    init_date = actual_date - timedelta(days=7)

    # Tomar las jugadas comprendidas entre las dos fechas. La actual y la actual - 7 dias.
    last_7days_plays = file[(file['Fecha y hora'] >= init_date) & (file['Fecha y hora'] <= actual_date)]

    # Tomar solos aquellas jugadas con puntaje mayor a cero
    plays_more0 = last_7days_plays[last_7days_plays['Puntos'] > 0]

    # A la columna fecha y hora se le saca la hora para poder comparar
    plays_more0['Fecha_Sin_Hora'] = plays_more0['Fecha y hora'].dt.date

    # Falta logica para calcular que haya una jugada para cada dia por jugador. Habria que hacer un 
    # un unique de fecha y usuario y ver si es 7

    # Mostrar el listado de usuarios en racha
    st.subheader("Listado de usuarios en racha:")


