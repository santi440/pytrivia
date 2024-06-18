import pandas as pd
import streamlit as st


def info_dificultades(plays_route):
    '''
    Lista cada dificultad de juego junto con el puntaje promedio obtenido en cada una y
    con la cantidad de veces que fue elegida.

        Args: Recibe la ruta del dataset de jugadas.
    '''

    file = pd.read_csv(plays_route)

    # Se controla que haya datos en el dataset
    if file.empty:
        st.subheader('Puntaje promedio de cada dificultad y cantidad de veces que fueron seleccionadas:')
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return

    # Utilizando grupby y la funcion .mean() se obitene el promedio
    average_difficulty = file.groupby('Dificultad')['Puntos'].mean()

    # De vuelta utilizando el groupby y la funcion .size() se obtiene la cantidad de ocurrencias
    quantity_difficulty = file.groupby('Dificultad').size()

    # Se crea un diccionario con toda la info recopilada y se tranforma en dataset para juntar todo e imprimirlo mejor
    result = pd.DataFrame.from_dict({'Puntaje Promedio': average_difficulty, 
                                     'Veces Elegido': quantity_difficulty})

    # Se muestra
    st.subheader('Puntaje promedio de cada dificultad y cantidad de veces que fueron seleccionadas:')
    st.write(result)
