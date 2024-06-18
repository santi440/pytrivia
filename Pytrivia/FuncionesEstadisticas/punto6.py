import pandas as pd
import streamlit as st


def dificultad_datasets(plays_route):
    '''
    Muestra los datasets ordenados por dificultad. Primero se muestra el dataset con
    mayor numero de errores. Tambien muestra la cantidad de respuestas incorrectas de cada uno.

        Args: Recibe la ruta del dataset de jugadas.
    '''

    file = pd.read_csv(plays_route)

    # Se controla que haya datos en el dataset
    if file.empty:
        st.subheader('Temáticas ordenados por dificultad:')
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return

    # Variable con la maxima cantidad de resp correctas
    max_correctas = 5
    
    ''' 
    * Se utiliza groupby con tematica y la cantidad de respuestas incorrectas
    * Se utiliza una funcion lambda para aplicar la resta de (max_correctas - respuestas correctas) a cada fila del dataset
    - El reset_index agrega la columna al dataset, para luego poder ordenar
    '''
    themes_info = file.groupby('Temática').apply(lambda x: (max_correctas - x['Cantidad de respuestas correctas']).sum()).reset_index(name='Respuestas Incorrectas')

    # Se ordenan los elementos de manera descente a partir de la columna creada 'Respuestas Incorrectas' 
    themes_info = themes_info.sort_values(by='Respuestas Incorrectas', ascending=False)

    # Se muestra 
    st.subheader('Temáticas ordenados por dificultad:')
    st.write(themes_info)  