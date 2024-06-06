import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import streamlit as st

def promedio_fechas(game):
    df = pd.read_csv(game)
    
    #Convierto el campo Fecha y hora a un tipo de dato de pandas 
    df['Fecha y hora'] = pd.to_datetime (df['Fecha y hora'])
    
    fecha1 = st.date_input("Primera fecha")
    fecha2 = st.date_input("Segunda Fecha")
    #Supongo que el usuario me va a poner fecha1 < fecha2
    
    fecha1 = pd.to_datetime (fecha1)
    fecha2 = pd.to_datetime (fecha2)
    df_filtrado = df[(df['Fecha y hora'] >= fecha1) & (df['Fecha y hora'] <= fecha2)]

    # Extraer el año y mes de la fecha y hora
    df_filtrado['Año-Mes'] = df_filtrado['Fecha y hora'].dt.to_period('M')

    # Calcular el promedio de preguntas acertadas por mes
    promedio_mensual = df_filtrado.groupby('Año-Mes')['Cantidad de respuestas correctas'].mean()
    
    st.write(promedio_mensual)