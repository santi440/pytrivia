import pandas as pd
import folium
import streamlit as st
import matplotlib as plt
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


def airport_map (df_airports,elevation):
    df_airports = df_airports[['name','latitude_deg','longitude_deg','elevation_name']]
    df_airports = df_airports.drop(df_airports[df_airports['elevation_name'] != elevation].index)

    mapa = folium.Map(
    location=(-33.457606, -65.346857),
    control_scale=True,
    zoom_start=5
    )
    df_airports.apply(lambda row: _add_marker(row, mapa), axis=1)
    return mapa
