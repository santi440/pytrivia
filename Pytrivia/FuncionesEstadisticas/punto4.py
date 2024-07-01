import pandas as pd
import streamlit as st

def entre_fechas(df):
    #Convierto el campo Fecha y hora a un tipo de dato de pandas 
    df['Fecha y hora'] = pd.to_datetime (df['Fecha y hora']).dt.to_period('D')
    
    fecha1 = st.date_input("Primera fecha")
    fecha2 = st.date_input("Segunda Fecha")
    #Supongo que el usuario me va a poner fecha1 < fecha2
    
    fecha1 = pd.to_datetime(fecha1).to_period('D')
    fecha2 = pd.to_datetime(fecha2).to_period('D')
    return df[(df['Fecha y hora'] >= fecha1) & (df['Fecha y hora'] <= fecha2)]

def promedio_fechas(game):
    """Muestra una tabla en streamlit de los promedios de respuestas correctas en los meses jugados
        Args:
             game (str): Una direccion del archivo que contiene los resultados de cada vez que se juega
             
        Returns:
                None
        """
    df = pd.read_csv(game)
    
    # Revisa si tiene informacion el DataFrame e imprime si esta vacio
    if df.empty:
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return
    
    df_filtrado = entre_fechas(df)

    # Extraer el año y mes de la fecha y hora
    df_filtrado['Año-Mes'] = df_filtrado['Fecha y hora'].dt.strftime('%Y/%m')

    # Calcular el promedio de preguntas acertadas por mes
    df_filtrado = df_filtrado.rename(columns={'Cantidad de respuestas correctas': 'Promedio de respuestas correctas'})
    promedio_mensual = df_filtrado.groupby('Año-Mes')['Promedio de respuestas correctas'].mean()
    
    st.write("Promedio Mensual jugado")
    st.write(promedio_mensual)
