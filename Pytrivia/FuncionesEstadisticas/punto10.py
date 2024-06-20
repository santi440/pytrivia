import pandas as pd
from datetime import datetime, timedelta
import streamlit as st

def usuarios_en_racha(plays_route):
    '''
    Lista los usuarios que registran una partida con un puntaje mayor a cero en todos 
    los días durante los últimos 7.

        Args: Recibe la ruta del dataset de jugadas.
    '''

    file = pd.read_csv(plays_route)

    # Se controla que haya datos en el dataset
    if file.empty:
        st.subheader('Listado de usuarios en racha:')
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return

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

    ''' 
    -Primero se agrupa la informacion por usuario. Luego aplicando un filter y un lambda, se toman unicamente aquellos jugadores 
    los cuales tengan por lo menos una jugada por dia. 
    -El lambda pregunta si existen por los menos 7 valores unicos de fechas (aunque haya 10 jugadas, si no hay una por dia no lo toma)
    -El ['Usuario'].unique() es para que no haya usuarios repetidos en el listado
    '''
    streak_users = plays_more0.groupby('Usuario').filter(lambda x: x['Fecha_Sin_Hora'].nunique() >= 7)['Usuario'].unique()

    # Mostrar el listado de usuarios en racha
    st.subheader("Listado de usuarios en racha:")
    if len(streak_users) == 0:
        st.write('Todavía no hay ningun jugador en racha. ¡Juega y sé el primero!')
    else:
        for player in streak_users:
            st.write(player)


