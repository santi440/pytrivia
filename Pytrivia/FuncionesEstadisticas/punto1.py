import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def graficar_genero(game,players):
    registered_players = pd.read_csv(players)   
    
    df_result = pd.read_csv(game)
    
    # saco un listado de los jugadores (email) que jugaron 
    email_filter = df_result.Email.unique() 
    
    # sobre los jugadores registrados pregunto si ademas jugaron
    df_filtrado = registered_players[registered_players['Email'].isin(email_filter)]
    
    # Agrupo por genero
    agrupado = df_filtrado.groupby('Genero').size()
    
    grafico = agrupado.plot(kind='pie', autopct='%1.1f%%', title='Jugadores Por genero')
    
    # Ver el listado de usuarios agrupados
    #print(df_filtrado.groupby('Genero')['Email'].apply(list))
    
    st.pyplot(plt.gcf())

if(__name__ == "__main__"):
    file_game = Path('Pytrivia','csv','resultado.csv')
    file_players = Path('Pytrivia','csv','datosformularios.csv')
    graficar_genero(file_game,file_players)