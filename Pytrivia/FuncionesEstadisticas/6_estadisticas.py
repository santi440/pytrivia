import pandas as pd

# FALTA IMPLEMENTARLO CON STREAMLIT

def estadistica_6(plays_route):
    file = pd.read_csv(plays_route)

    # Variable con la maxima cantidad de resp correctas
    max_correctas = 5
    
    ''' 
    -Se utiliza groupby con tematica y la cantidad de respuestas incorrectas
    -Se utiliza una funcion lambda para aplicar la resta de (max_correctas - respuestas correctas) a cada fila del dataset
    - El reset_index agrega la columna al dataset, para luego poder ordenar
    '''
    themes_info = file.groupby('Tematica').apply(lambda x: (max_correctas - x['Respuestas Correctas']).sum()).reset_index(name='Respuestas Incorrectas')

    # Se ordenan los elementos de manera descente a partir de la columna creada 'Respuestas Incorrectas' 
    themes_info = themes_info.sort_values(by='Respuestas Incorrectas', ascending=False)

    # Se muestra grafico
    print(themes_info)