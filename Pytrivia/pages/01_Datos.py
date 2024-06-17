from FuncionesDatos import graficos as func
import streamlit as st
import pandas as pd
import matplotlib as plt
from pathlib import Path
from streamlit_folium import folium_static
import folium


st.header("Conocemos nuestros datos")
st.subheader("Mapa de Aeropuertos")

airports_path = Path("..","datasets_custom")/ 'ar-airports-custom.csv'
df_airports = pd.read_csv(airports_path)

lakes_path = Path("..","datasets_custom") / "lagos_arg_custom.csv"
df_lakes = pd.read_csv(lakes_path)

option = st.selectbox("Elija que datos ver", options = ['Aeropuertos','Lagos'])

mapa = folium.Map(
    location=(-33.457606, -65.346857),
    control_scale=True,
    zoom_start=5
    )

match option:

    case 'Aeropuertos':
        option2 = st.selectbox("Elija grafico", options= ['Mapa', 'Grafico de torta', 'Grafico de Barra'])
        match option2:

             case "Mapa":
                elevation = st.multiselect("Elevacion", options = ['bajo','medio','alto'])
                mapa = func.airport_map(df_airports,elevation,mapa)
                folium_static(mapa)
             case "Grafico de torta":
                func.graph_airport_size(df_airports)
             case "Grafico de Barra":
                func.bar_airport_elevation(df_airports)


    case 'Lagos':
        option2 = st.selectbox("Elija grafico", options= ['Mapa', 'Grafico de torta', 'Grafico de Barra'])
        match option2:

             case "Mapa":
                mapa = func.lakes_map(df_lakes,mapa)
                folium_static(mapa)
             case "Grafico de torta":
                func.graph_provinces_lakes(df_lakes)
             case "Grafico de Barra":
                func.bar_lakes_depth(df_lakes)