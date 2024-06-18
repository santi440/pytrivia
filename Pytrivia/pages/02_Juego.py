import streamlit as st
import pandas as pd
from pathlib import Path
from FuncionesJuego import generadores as gen
from FuncionesSesion import Sesiones

# Definir la ruta base
base_path = Path(__file__).resolve().parent.parent.parent

# Cargar los datasets
airports_path = base_path / 'datasets_custom' / 'ar-airports-custom.csv'
aeropuertos = pd.read_csv(airports_path)

lagos_path = base_path / 'datasets_custom' / 'lagos_arg_custom.csv'
lagos = pd.read_csv(lagos_path)

conec_path = base_path / 'datasets_custom' / 'Conectividad_Internet.csv'
conectividad = pd.read_csv(conec_path)

censo_path = base_path / 'datasets_custom' / 'Censo_Modificado.csv'
censo_2022 = pd.read_csv(censo_path)


# Título de la página
st.title('Juego de Trivia')
if(Sesiones.is_user_logged_in()):
    # Seleccionar usuario
    usuario = st.selectbox('Selecciona tu usuario', ['Usuario1', 'Usuario2', 'Usuario3'])

    # Seleccionar temática
    tematica = st.selectbox('Selecciona una temática', ['Aeropuertos', 'Lagos', 'Conectividad', 'Censo 2022'])

    # Seleccionar dificultad
    dificultad = st.selectbox('Selecciona la dificultad', ['Fácil', 'Media', 'Alta'])

    # Generar preguntas
    if st.button('Comenzar Juego'):
        preguntas = []
        if tematica == 'Aeropuertos':
            for _ in range(5):
                preguntas.append(gen.generar_pregunta_aeropuertos(aeropuertos))
        elif tematica == 'Lagos':
            for _ in range(5):
                preguntas.append(gen.generar_pregunta_lagos(lagos))
        elif tematica == 'Conectividad':
            for _ in range(5):
                preguntas.append(gen.generar_pregunta_conectividad(conectividad))
        elif tematica == 'Censo 2022':
            for _ in range(5):
                preguntas.append(gen.generar_pregunta_censo(censo_2022))

        # Mostrar preguntas
        for idx, (respuesta_correcta, opciones) in enumerate(preguntas):
            st.write(f'Pregunta {idx+1}')
            opcion_seleccionada = st.radio(f'Selecciona una opción:', opciones['name'].tolist())
            if opcion_seleccionada == respuesta_correcta:
                st.success('¡Correcto!')
            else:
                st.error(f'Incorrecto. La respuesta correcta era: {respuesta_correcta}')

else:
    st.subheader("Antes de jugar, debes Registrarte o Iniciar Sesion")
    if (st.button('Registrarse')):
        st.switch_page("pages/03_Formulario de Registro.py")

