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
st.table(df_filtrado_display) # La posición se muesta como el índice del DataFrame


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

        for i, (question, correct_answer) in enumerate(st.session_state.questions):
            st.write(f"Pregunta {i + 1}:")
            st.write(question)
    
            if i < len(st.session_state.user_answers):
                answer = st.session_state.user_answers[i][0]
                st.write(f'Tu Respuesta: {answer}')
                st.write(f'Respuesta Correcta: {correct_answer}')
                st.write('-----------------------------------------------------------------------------------------')

    st.subheader('Tu posición actual en el ranking')
    st.table(df_filtrado[df_filtrado['Email'] == st.session_state.email].set_index('Posición')) # La posición se muesta como el índice del DataFrame