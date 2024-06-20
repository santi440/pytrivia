import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def graficar_genero(game,players):
    """Muestra un grafico en streamlit de los jugadores registrados segun su genero
        Args:
             game (str): Una direccion del archivo que contiene los resultados de cada vez que se juega
             players(str) : Una direccion del archivo donde con las personas registradas

        Returns:
                None
    """
    
    registered_players = pd.read_csv(players)   
    
    # Revisa si tiene informacion el DataFrame e imprime si esta vacio
    if registered_players.empty:
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return
    
    df_result = pd.read_csv(game)
    
    # saco un listado de los jugadores (email) que jugaron 
    email_filter = df_result.Email.unique() 
    
    # sobre los jugadores registrados pregunto si ademas jugaron
    df_filtrado = registered_players[registered_players['Email'].isin(email_filter)]
    
    # Agrupo por genero
    agrupado = df_filtrado.groupby('Genero').size()

    grafico = agrupado.plot(kind='pie', autopct='%1.1f%%', title='Jugadores Por genero que están registrados y jugaron')
    
    # Ver el listado de usuarios agrupados
    #print(df_filtrado.groupby('Genero')['Email'].apply(list))
    
    st.pyplot(plt.gcf())
