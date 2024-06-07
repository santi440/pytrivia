import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st

def mejores(game):
    df = pd.read_csv(game)
    
    #Convierto el campo Fecha y hora a un tipo de dato de pandas 
    df['Fecha y hora'] = pd.to_datetime (df['Fecha y hora']).dt.to_period('D')
    
    fecha1 = st.date_input("Primera fecha")
    fecha2 = st.date_input("Segunda Fecha")
    #Supongo que el usuario me va a poner fecha1 < fecha2
    
    fecha1 = pd.to_datetime(fecha1).to_period('D')
    fecha2 = pd.to_datetime(fecha2).to_period('D')
    
    df_filtrado = df[(df['Fecha y hora'] >= fecha1) & (df['Fecha y hora'] <= fecha2)]

    #sumo todos los puntos de los jugadores
    df_filtrado = df_filtrado.groupby('Usuario')['Puntos'].sum()
    df_filtrado = df_filtrado.sort_values(ascending = False)
    st.write (df_filtrado.head(10))


