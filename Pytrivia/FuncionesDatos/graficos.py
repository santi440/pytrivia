import pandas as pd
import folium
import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path



##AEROPUERTOS

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



def graph_airport_size (df_airports):
     # Diccionario de mapeo de los nombres actuales a los nuevos nombres deseados
    type_mapping = {
        'large_airport': 'Aeropuerto Grande',
        'medium_airport': 'Aeropuerto Mediano',
        'small_airport': 'Aeropuerto Pequeño',
        'closed': 'Aeropuerto Cerrado',
        'heliport': 'Helipuerto',
        'balloonport': 'Aeropuerto de Globos'
    }
    
    # Reemplazar los valores de la columna 'type'
    df_airports['type'] = df_airports['type'].replace(type_mapping)
    df_airports = df_airports.groupby('type').size()
    df_airports.plot(kind='pie', autopct='%1.1f%%', title='Tamaño de aeropuertos')
    
    st.pyplot(plt.gcf())



def bar_airport_elevation (df_airports):
    df_airports = df_airports.groupby('prov_name')['elevation_ft'].mean().sort_values() # Calcula la media de los valores de elevation_ft para cada grupo (provincia) y se ordenan con sort
    df_airports.plot(kind='barh', xlabel='Elevacion', ylabel='Provincia', title='Elevacion promedio de aeropuertos por Provincia', figsize = (7,15), colormap = 'viridis')
    st.pyplot(plt.gcf())



#-----------------------------------------------------------------------------------------------------------------------------------------
# LAGOS


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


def _separate_lake(df_lakes):
    nahuel_huapi_row = df_lakes[df_lakes['Nombre'] == 'Lago Nahuel Huapi']

    row_rio_negro = nahuel_huapi_row.copy()
    row_rio_negro['Ubicación'] = 'Río Negro'
        
    row_neuquen = nahuel_huapi_row.copy()
    row_neuquen['Ubicación'] = 'Neuquén'

    df_lakes = df_lakes[df_lakes['Nombre'] != 'Lago Nahuel Huapi']

    return pd.concat([df_lakes, row_rio_negro, row_neuquen], ignore_index=True) #concateno y reestablezco el indice del dataframe

def bar_lakes_depth (df_lakes):

    df_lakes = _separate_lake(df_lakes)

    df_lakes = df_lakes.groupby('Ubicación')['Profundidad media (m)'].mean().sort_values() # Calcula la media de los valores de elevation_ft para cada grupo (provincia) y se ordenan con sort
    df_lakes.plot(kind='barh', xlabel='Profundidad media', ylabel='Provincia', title='Profundidad promedio de lagos por Provincia', figsize = (7,15), colormap = 'viridis')
    st.pyplot(plt.gcf())


def graph_provinces_lakes (df_lakes):
    df_lakes = _separate_lake(df_lakes)
    
    # Agrupar por 'Ubicación' (provincia) y contar la cantidad de lagos por provincia
    df_lakes_count = df_lakes.groupby('Ubicación').size().reset_index(name='Cantidad')
    
    # Crear el gráfico de torta
    plt.figure(figsize=(8, 8))
    plt.pie(df_lakes_count['Cantidad'], labels=df_lakes_count['Ubicación'], autopct='%1.1f%%', startangle=140)
    plt.title('Porcentaje de Lagos por Provincia')
    plt.axis('equal')

    # Genero el grafico directamente con plt porque la funcion .plot de pandas es conveniente cuando el propio dataframe contiene valores numericos
    # Es decir, que los datos que se quieren mostrar son directamente numericos.
    # En este caso, yo quiero mostrar el % de lagos que tiene cada provincia en relacion al total del pais, para ello, debo contar las ocurrencias de cada provincia, lo cual es un dato String, no numerico
    
    st.pyplot(plt.gcf())