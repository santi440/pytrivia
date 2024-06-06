import pandas as pd
import streamlit as st


def estadistica_8(plays_route, users_route):
    '''
    Listar para cada género cuál es la temática en la cual demuestra mayor
    conocimiento. Tambien muestra la cantidad total de puntos que tiene.


        Args: Recibe la ruta del dataset de jugadas y la ruta del dataset
        que contiene la informacion de los usuarios.
    '''
    
    plays_data = pd.read_csv(plays_route)
    users_data = pd.read_csv(users_route)
    
    '''
    * Con un merge se combinan las jugadas y los datos de los usuarios en un solo dataframe
    * Se hace con la columna 'Usuario' y de la forma 'Inner'
    '''
    merged_data = pd.merge(plays_data, users_data, left_on='Usuario', right_on='Email', how='inner')    
    '''
    * Agrupa por genero y tematica y calcula la suma de puntaje
    * El reset_index agrega la columna al dataset, para luego poder ordenar
    '''
    grouped_data = merged_data.groupby(['Genero', 'Temática'])['Puntos'].sum().reset_index()
    
    # Ordena la columna puntaje, de manera descendente
    grouped_data = grouped_data.sort_values(by='Puntos', ascending=False)
    
    # Toma la primera tematica que aparece para cada genero, es decir, la mejor
    best_theme = grouped_data.groupby('Genero').first()
    
    # Imprime los resultados
    st.subheader('Temática en la que cada género demuestra mayor conocimiento:')
    st.write(best_theme)
