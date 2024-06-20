import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def graficar_porcentaje(game): 
    """Muestra un grafico en streamlit de los jugadores por encima de la media 
        Args:
             game (str): Una direccion del archivo que contiene los resultados de cada vez que se juego

        Returns:
                None
    """
    df_result = pd.read_csv(game)
    # Revisa si tiene informacion el DataFrame e imprime si esta vacio
    if df_result.empty:
        st.write("Todavía no hay información sobre partidas. ¡Juega y luego podrás ver tus estadísticas!")
        return

    # Calcular los percentiles
    percentile_50 = df_result["Puntos"].quantile(0.5)
    
    #percentile_50 = df_result.loc['50%', 'Puntos']
    great_players = df_result[df_result["Puntos"] >= percentile_50] 
    
    # Configurar los datos para el gráfico de torta
    labels_players = great_players['Usuario']
    values_players = great_players['Puntos']
    
    #hoverinfo para que se vea el porcentaje al pasar por encima 
    fig_pie = go.Figure(data=[go.Pie(labels=labels_players, values=values_players, hole=0.3,hoverinfo="label+value")])
    fig_pie.update_layout(title="Partidas que superan la media")
    
    st.plotly_chart(fig_pie)
