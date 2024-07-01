import pandas as pd
import streamlit as st
from .punto4 import entre_fechas

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
    
    df_filtrado = entre_fechas(df)

    #sumo todos los puntos de los jugadores
    df_filtrado = df_filtrado.groupby('Usuario')['Puntos'].sum()
    df_filtrado = df_filtrado.sort_values(ascending = False)
    
    st.write("Los mejores 10 jugadores entre fechas")
    st.write (df_filtrado.head(10))


