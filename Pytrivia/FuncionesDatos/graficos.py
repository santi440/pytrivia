import pandas as pd
import folium
import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path

def _get_color (elevation):     
    if elevation == 'bajo':
        color  = 'green'
    elif elevation == 'medio' :
        color = 'blue'
    else:
        color = 'red'
    return color

def _add_marker(row,mapa):
    color = _get_color(row['elevation_name'])
    folium.Marker(
        [row['latitude_deg'], row['longitude_deg']],
        popup= row['name'],
        icon= folium.Icon(color=color)
    ).add_to(mapa)


def airport_map (df_airports,elevation,mapa):
    df_airports = df_airports[['name','latitude_deg','longitude_deg','elevation_name']]
    df_airports = df_airports.drop(df_airports[~df_airports['elevation_name'].isin(elevation)].index)

    
    df_airports.apply(lambda row: _add_marker(row, mapa), axis=1)
    return mapa

def _add_marker_lake(row,mapa):
    folium.Marker(
        [row['Latitud(GD)'], row['Longitud(GD)']],
        popup= row['Nombre'],
        icon= folium.Icon(color= 'cadetblue')
    ).add_to(mapa)

def lakes_map (df_lakes,mapa):
    df_lakes = df_lakes[['Nombre','Latitud(GD)','Longitud(GD)']]
    df_lakes.apply(lambda row: _add_marker_lake(row,mapa), axis = 1)
    return mapa


def graph_airport_size (df_airports):
    df_airports = df_airports.groupby('type').size()
    grafico = df_airports.plot(kind='pie', autopct='%1.1f%%', title='Tamaño de aeropuertos')
    
    st.pyplot(plt.gcf())