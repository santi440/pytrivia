from FuncionesDatos import graficos as func
import streamlit as st
import pandas as pd
import matplotlib as plt
from pathlib import Path


st.header("Conocemos nuestros datos")
st.subheader("Mapa de Aeropuertos")

airports_path = Path("..","datasets_custom")/ 'ar-airports-custom.csv'
df_airports = pd.read_csv(airports_path)

lakes_path = Path("..","datasets_custom") / "lagos_arg_custom.csv"
df_lakes = pd.read_csv(lakes_path)

option = st.selectbox("Elija que datos ver", options = ['Aeropuertos','Lagos'])

match option:
    case 'Aeropuertos':
        mapa = func.airport_map(df_airports)
        mapa
    case 'Lagos':
        st.write('b')