import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime
from pathlib import Path
from FuncionesJuego import generadores as gen
from FuncionesSesion import Sesiones
import numpy as np

# Título de la página
st.title('Juego de Trivia')

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

base_path= Path (__file__).resolve().parent.parent
datos_path= base_path / 'csv' / 'datos_formularios.csv'
resultado_path= base_path/ 'csv' / 'resultado.csv'
datos= pd.read_csv(datos_path)
    
if(Sesiones.is_user_logged_in()):
    # Seleccionar usuario
    user = st.selectbox('Selecciona tu usuario', options= datos['Email'].unique())

    # Seleccionar temática
    theme = st.selectbox('Selecciona una temática', ['Aeropuertos', 'Lagos', 'Conectividad', 'Censo 2022'])

    # Seleccionar dificultad
    difficulty = st.selectbox('Selecciona la dificultad', ['Fácil', 'Media', 'Alta'])

    # Explicacion de como funciona cada nivel de dificultad.

    st.info("""
        **Fácil:** Se proporciona una pista detallada.  
        **Media:** Se proporciona una pista general.  
        **Alta:** No se proporciona ninguna pista.
    """)
    
    # Generar preguntas basadas en la temática
    questions = gen.generateQuestions(theme, aeropuertos, lagos, conectividad, censo_2022)
    
    # Almacenar respuestas del usuario
    user_answers = []
    for i, (question, correct_answer) in enumerate(questions):
        st.write(f"Pregunta {i + 1}:")
        st.write(question)
        
        if difficulty != 'Alta':
            hint = gen.generate_hint(correct_answer, difficulty)
            if hint:
                st.write(f"Pista: {hint}")

        user_answer = st.text_input(f"Respuesta a la pregunta {i + 1}:")
        user_answers.append((user_answer, correct_answer))

    # Empezar con las 5 preguntas del tema elegido, dar la pista correspondiente a la dificultad. Si es dificil no hay pista. Sumar 1 punto por cada respuesta correcta.

    # Mostrar mensaje que diga Juego completado y la cantidad de respuestas correctas. Si la dificultad es media el puntaje se multiplica por 1.5, si es dificil el puntaje se multiplica x2.

    # Almacenar en resultado_path : - Fecha y hora: momento en el cual se responde la trivia.
#                                   - Usuario: identificador del usuario.
#                                   - Email: email del usuario.
#                                   - Dificultad: dificultad elegida por el usuario.
#                                   - Temática: temática elegida por el usuario.
#                                   - Cantidad de respuestas correctas.
#                                   - Puntos: puntos obetinos en la partida.


    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Volver a jugar"):
            st.rerun()
    
    with col2:
        if st.button("Ir al Ranking"):
            st.switch_page("pages/05_Ranking.py")


else:
    st.subheader("Antes de jugar, debes Registrarte o Iniciar Sesion")
    if (st.button('Registrarse')):
        st.switch_page("pages/03_Formulario de Registro.py")
