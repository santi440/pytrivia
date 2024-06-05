import pandas as pd

# FALTA IMPLEMENTARLO CON STREAMLIT

def estadistica_8(plays_route, users_route):
    plays_data = pd.read_csv(plays_route)
    users_data = pd.read_csv(users_route)
    
    '''
    * Con un merge se combinan las jugadas y los datos de los usuarios en un solo dataframe
    * Se hace con la columna 'Usuario' y de la forma 'Inner'
    '''
    merged_data = pd.merge(plays_data, users_data, on='Usuario', how='inner')
    
    '''
    * Agrupa por genero y tematica y calcula la suma de puntaje
    * El reset_index agrega la columna al dataset, para luego poder ordenar
    '''
    grouped_data = merged_data.groupby(['Genero', 'Tematica'])['Puntaje'].sum().reset_index()
    
    # Ordena la columna puntaje, de manera descendente
    grouped_data = grouped_data.sort_values(by='Puntaje', ascending=False)
    
    # Toma la primera tematica que aparece para cada genero, es decir, la mejor
    best_theme = grouped_data.groupby('Genero').first()
    
    # Imprime los resultados
    print(best_theme)
