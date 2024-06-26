import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def grafico_dias(game):
    """Muestra un grafico de barras en streamlit con la cantidad partidas jugadas en cada dia de la semana
        Args:
             game (str): Una direccion del archivo que contiene los resultados de cada vez que se juega
             
        Returns:
                None"""
                
    df = pd.read_csv(game)
    
    # Revisa si tiene informacion el DataFrame e imprime si esta vacio
    if df.empty:
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return
    
    #Convierto el campo Fecha y hora a un tipo de dato de pandas 
    df['Fecha y hora'] = pd.to_datetime (df['Fecha y hora'])
    
    # Agregar una nueva columna con el nombre del día de la semana (comodidad, no se refleja en el dataset)
    df['dia_semana'] = df['Fecha y hora'].dt.day_name()

    # Contar el número de registros por día de la semana
    conteo_dias_semana = df.groupby('dia_semana').size()

    # Ordenar los días de la semana 
    dias_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    conteo_dias_semana = conteo_dias_semana.reindex(dias_orden)
    
    # Rellenar los valores faltantes (días sin registros) con ceros
    conteo_dias_semana.fillna(0, inplace=True)
    conteo_dias_semana = conteo_dias_semana.astype('int64') #Me lo tomaba como float y en este caso no corresponde
    
    # Crear el gráfico de barras
    grafico = plt.bar(conteo_dias_semana.index, conteo_dias_semana.values)

    # Agregar etiquetas y título
    plt.xlabel('Día de la Semana')
    plt.ylabel('Recuento de Registros')
    plt.title('Recuento de Registros por Día de la Semana')
    
    st.pyplot(plt.gcf())
    #print(conteo_dias_semana)