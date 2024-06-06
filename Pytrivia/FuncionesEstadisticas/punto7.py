import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def estadistica_7(plays_route):
    '''
    Pide al usario seleccionar dos usuarios y muestra gráfico que compara la evolución 
    de puntaje entre los mismos a lo largo del tiempo.


        Args: Recibe la ruta del dataset de jugadas.
    '''

    file = pd.read_csv(plays_route)

    # Lista de usuarios únicos
    unique_users = file['Usuario'].unique()

    # Widget para seleccionar el primer usuario y segundo usuario
    user1 = st.selectbox("Selecciona el primer usuario:", unique_users)
    user2 = st.selectbox("Selecciona el segundo usuario:", unique_users)

    # Columna 'Fecha y hora' a datetime
    file['Fecha y hora'] = pd.to_datetime(file['Fecha y hora'])

    # Filtrar jugadas para los dos usuarios seleccionados
    user1_data = file[file['Usuario'] == user1]
    user2_data = file[file['Usuario'] == user2]
     
    # Ordenar los datos por fecha
    user1_data = user1_data.sort_values('Fecha y hora')
    user2_data = user2_data.sort_values('Fecha y hora')

    # Datos de los usuarios en el grafico
    plt.plot(user1_data['Fecha y hora'], user1_data['Puntos'], color='green')
    plt.plot(user2_data['Fecha y hora'], user2_data['Puntos'], color='purple')

    # Titulo del grafico 
    plt.title(f'Comparación de la evolución del puntaje entre {user1} y {user2}.')

    # Se indican leyendas, titulos de ejes, rotacion de los titulos, tamaño del grafico
    plt.legend ([user1, user2]) 

    plt.xlabel ('Tiempo')
    plt.ylabel ('Puntos')

    plt.xticks(rotation=45)
 
    # Se muestra. Se utiliza plt.gfc() , significa 'get current figure'
    st.pyplot(plt.gcf())
