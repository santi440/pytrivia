import pandas as pd
import matplotlib.pyplot as plt

# FALTA IMPLEMENTARLO CON STREAMLIT

def estadistica_7(plays_route):
    file = pd.read_csv(plays_route)
    user1 = input('Ingrese nombre del primer usuario a comparar: ')
    user2 = input('Ingrese nombre del segundo usuario a comparar: ')
    
    # Columna 'Fecha y hora' a datetime
    file['Fecha y hora'] = pd.to_datetime(file['Fecha y hora'])
    
    # Filtrar jugadas para los dos usuarios seleccionados
    user1_data = file[file['Usuario'] == user1]
    user2_data = file[file['Usuario'] == user2]
    
    # Ordenar los datos por fecha
    user1_data = user1_data.sort_values('Fecha y hora')
    user2_data = user2_data.sort_values('Fecha y hora')
    
    # Datos de los usuarios en el grafico
    plt.plot(user1_data['Fecha y hora'], user1_data['Puntaje'], color='green')
    plt.plot(user2_data['Fecha y hora'], user2_data['Puntaje'], color='purple')

    # Titulo del grafico 
    plt.title(f'Comparación de la evolución del puntaje entre {user1} y {user2}.')
    
    # Se indican leyendas, titulos de ejes, rotacion de los titulos, tamaño del grafico
    plt.legend ([user1, user2]) 

    plt.xlabel ('Tiempo')
    plt.ylabel ('Puntaje')

    plt.xticks(rotation=45)
    plt.figure(figsize=(10, 6)) 
    
    # Se muestra
    plt.show()
