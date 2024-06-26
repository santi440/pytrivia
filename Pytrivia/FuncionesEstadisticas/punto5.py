import pandas as pd
import streamlit as st

def mejores(game):
    """Muestra una tabla en streamlit de los mejores jugadores
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
    
    #Convierto el campo Fecha y hora a un tipo de dato de pandas 
    df['Fecha y hora'] = pd.to_datetime (df['Fecha y hora']).dt.to_period('D')
    
    fecha1 = st.date_input("Primera fecha")
    fecha2 = st.date_input("Segunda Fecha")
    #Supongo que el usuario me va a poner fecha1 < fecha2
    
    fecha1 = pd.to_datetime(fecha1).to_period('D')
    fecha2 = pd.to_datetime(fecha2).to_period('D')
    
    df_filtrado = df[(df['Fecha y hora'] >= fecha1) & (df['Fecha y hora'] <= fecha2)]

    #sumo todos los puntos de los jugadores
    df_filtrado = df_filtrado.groupby('Usuario')['Puntos'].sum()
    df_filtrado = df_filtrado.sort_values(ascending = False)
    
    st.write("Los mejores 10 jugadores entre fechas")
    st.write (df_filtrado.head(10))


