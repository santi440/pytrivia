import pandas as pd
import streamlit as st


def estadistica_9(plays_route):
    file = pd.read_csv(plays_route)

    # Utilizando grupby y la funcion .mean() se obitene el promedio
    average_difficulty = file.groupby('Dificultad')['Puntaje'].mean()

    # De vuelta utilizando el groupby y la funcion .size() se obtiene la cantidad de ocurrencias
    quantity_difficulty = file.groupby('Dificultad').size()

    # Se crea un diccionario con toda la info recopilada y se tranforma en dataset para juntar todo e imprimirlo mejor
    result = pd.DataFrame.from_dict({'Puntaje Promedio': average_difficulty, 
                                     'Veces Elegido': quantity_difficulty})

    # Se muestra
    st.subheader('Puntaje promedio de cada dificultad y cantidad de veces que fueron seleccionadas:')
    st.write(result)
