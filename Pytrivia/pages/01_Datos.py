from FuncionesDatos import graficos as func
import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_folium import folium_static
import folium


st.header("Conocemos nuestros datos")
st.subheader("Mapa de Aeropuertos")

# Definir rutas de los archivos a utilizar
airports_path = Path("..","datasets_custom")/ 'ar-airports-custom.csv'
df_airports = pd.read_csv(airports_path)

lakes_path = Path("..","datasets_custom") / "lagos_arg_custom.csv"
df_lakes = pd.read_csv(lakes_path)

# Selectbox para elegir los datos a ver
option = st.selectbox("Elija que datos ver", options = ['Aeropuertos','Lagos'])

# Creo un mapa con Folium
attr = (
'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
)
tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
mapa= folium.Map(
      location=(-33.457606, -65.346857),
      control_scale=True,
      zoom_start=5,
      name='es',
      tiles=tiles,
      attr=attr
)

match option:
   # Selección del tipo de gráfico para aeropuertos
    case 'Aeropuertos':
        option2 = st.selectbox("Elija grafico", options= ['Mapa', 'Grafico de torta', 'Grafico de Barra'])
        match option2:

             case "Mapa":
                # Selección de la elevación a mostrar en el mapa
                elevation = st.multiselect("Elevacion", options = ['bajo','medio','alto'])
                # Generar el mapa de aeropuertos con la elevación seleccionada
                mapa = func.airport_map(df_airports,elevation,mapa)
                folium_static(mapa)
                # Generar un gráfico de torta con el tamaño de los aeropuertos
             case "Grafico de torta":
                func.graph_airport_size(df_airports)
                # Generar un gráfico de barras con la elevación de los aeropuertos
             case "Grafico de Barra":
                func.bar_airport_elevation(df_airports)


    case 'Lagos':
        # Selección del tipo de gráfico para lagos
        option2 = st.selectbox("Elija grafico", options= ['Mapa', 'Grafico de torta', 'Grafico de Barra'])
        match option2:

             case "Mapa":
                # Generar el mapa de lagos
                mapa = func.lakes_map(df_lakes,mapa)
                folium_static(mapa)
             case "Grafico de torta":
                # Generar un gráfico de torta con los lagos por provincia
                func.graph_provinces_lakes(df_lakes)
             case "Grafico de Barra":
                # Generar un gráfico de barras con la profundidad media de los lagos por provincia
                func.bar_lakes_depth(df_lakes)