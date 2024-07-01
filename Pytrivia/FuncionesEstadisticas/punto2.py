import streamlit as st
import matplotlib.pyplot as plt
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
    
    #Nueva columna Supera_media con el resultado de la mascara
    df_result['Supera_media'] = df_result["Puntos"] >= percentile_50
    
    # Cuenta el numero de usuarios para las categorias si supera o no (primer valor siempre falso)
    category_counts = df_result['Supera_media'].value_counts()
    
    #Grafico con formato para que quede mas estilizado
    plt.figure(figsize=(8, 8))
    plt.pie(category_counts,labels=['No superan la media','Superan la media'],autopct='%1.1f%%',startangle=140, colors=['#ff9999','#66b3ff'])
    plt.title('Distribución de usuarios según si superan al media de puntos')
    st.pyplot(plt.gcf())
