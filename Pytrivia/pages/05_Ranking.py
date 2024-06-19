import pandas as pd
import streamlit as st
from pathlib import Path
from FuncionesSesion import Sesiones



df = pd.read_csv(Path('..','Pytrivia','csv','resultado.csv'))

#sumo todos los puntos de los jugadores
df_filtrado = df.groupby(['Usuario', 'Email'])['Puntos'].sum().reset_index()

# Ordenar los jugadores por puntos en orden descendente
df_filtrado = df_filtrado.sort_values(by='Puntos', ascending=False).reset_index(drop=True)

# Agregar columna de posición empezando desde 1
df_filtrado['Posición'] = df_filtrado.index + 1
    
st.header("Los mejores 15 jugadores")
df_filtrado_display = df_filtrado.head(15).set_index('Posición')
st.table(df_filtrado_display)

#st.table(df_filtrado.head(15).drop(columns='Email').style.hide(axis='index'))

user = Sesiones.get_logged_in_user()

if user is not None and not user.empty:
    email = user['Email'].values[0]
    usuario = df_filtrado_display.loc[df_filtrado_display['Email'] == email]
    if not usuario.empty:
        st.subheader('Tu puntaje')
        st.table(usuario)


if st.session_state.get('step') == 'completed':
    st.subheader("Última Partida Jugada")
    st.write(f"Respuestas correctas: {st.session_state['correct_count']}. Puntos obtenidos: {st.session_state['points']}")

    answers = st.session_state['user_answers']

    if answers:
        # Crear un DataFrame con las respuestas y las respuestas correctas
        data = {
            'Pregunta': [f"Pregunta {i + 1}" for i in range(len(answers))],
            'Tu Respuesta': [answer for answer, correct_answer in answers],
            'Respuesta Correcta': [correct_answer for answer, correct_answer in answers]
        }
        df = pd.DataFrame(data)
        
        # Mostrar la tabla de las respuestas
        st.write("Respuestas de la última partida:")
        st.table(df)