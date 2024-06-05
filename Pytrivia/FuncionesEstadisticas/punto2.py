import plotly.graph_objects as go
import pandas as pd
from pathlib import Path

def graficar_porcentaje(game): 
    df_result = pd.read_csv(game)

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
    return fig_pie

if(__name__ == "__main__"):
    file_game = Path('Pytrivia','Csv','resultado.csv')
    fig_pie=graficar_porcentaje(file_game)
    fig_pie.show()