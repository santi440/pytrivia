import pandas as pd
import streamlit as st


def tematica_por_genero(plays_route, users_route):
    '''
    Listar para cada género cuál es la temática en la cual demuestra mayor
    conocimiento. Tambien muestra la cantidad total de puntos que tiene.


        Args: Recibe la ruta del dataset de jugadas y la ruta del dataset
        que contiene la informacion de los usuarios.
    '''
    
    plays_data = pd.read_csv(plays_route)
    users_data = pd.read_csv(users_route)

    # Se controla que haya datos en el dataset. No hace falta controlar el de usuarios
    if plays_data.empty:
        st.subheader('Temática en la que cada género demuestra mayor conocimiento:')
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!.")
        return
    
    '''
    * Con un merge se combinan las jugadas y los datos de los usuarios en un solo dataframe
    * Se hace con la columna 'Usuario' y de la forma 'Inner'
    '''
    merged_data = pd.merge(plays_data, users_data, left_on='Email', right_on='Email', how='inner')    
                        # A la hora de juntar todo con el juego ver con que campos tomar el merge
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
