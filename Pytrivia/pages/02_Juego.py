import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
from FuncionesJuego import generadores as gen
from FuncionesSesion import Sesiones

# Título de la página
st.title('Juego de Trivia')

# Cargar datasets datos y resultado
base_path = Path(__file__).resolve().parent.parent
datos_path = base_path / 'csv' / 'datos_formularios.csv'
resultado_path = base_path / 'csv' / 'resultado.csv'
datos = pd.read_csv(datos_path)

# Crear el session state
if 'user' not in st.session_state:
    st.session_state.user = None

if 'theme' not in st.session_state:
    st.session_state.theme = None

if 'difficulty' not in st.session_state:
    st.session_state.difficulty = None

if 'questions' not in st.session_state:
    st.session_state.questions = []

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []

if 'step' not in st.session_state:
    st.session_state.step = 'start'

if 'correct_count' not in st.session_state:
    st.session_state.correct_count = None

if 'points' not in st.session_state:
    st.session_state.points = None

if 'start_time' not in st.session_state:
    st.session_state.start_time = None

if 'end_time' not in st.session_state:
    st.session_state.end_time = None

if 'email' not in st.session_state:
    st.session_state.email = None

if Sesiones.is_user_logged_in():
    if st.session_state.step == 'start':
        # Seleccionar usuario
        user = st.session_state.user
        st.write(f"¿Estás listo para jugar {user}?")

        # Seleccionar temática
        theme = st.selectbox(
            'Selecciona una temática',
            ['Aeropuertos', 'Lagos', 'Conectividad', 'Censo 2022']
        )

        # Seleccionar dificultad
        difficulty = st.selectbox(
            'Selecciona la dificultad',
            ['Fácil', 'Media', 'Alta']
        )

        # Explicación de niveles de dificultad
        st.info("""
            En las tematicas Aeropuertos, Lagos y Censo 2022:

            **Fácil:** Se proporciona una pista detallada.  
            **Media:** Se proporciona una pista general.  
            **Alta:** No se proporciona ninguna pista.

            En la tematica Conectividad:

            **Fácil:** Tienes 5 minutos para responder.  
            **Media:** Tienes 3 minutos para responder.    
            **Alta:** Tienes 1 minuto para responder.  
        """)

        if st.button('Comenzar Juego'):
            st.session_state.user = user
            st.session_state.theme = theme
            st.session_state.difficulty = difficulty
            st.session_state.questions = gen.generate_questions(theme)
            st.session_state.user_answers = []
            st.session_state.step = 'playing'
            st.rerun()

        if st.button('Cerrar Sesión'):
            st.session_state.email = None
            st.session_state.user = None
            st.session_state.step = 'start'
            st.rerun()

    if st.session_state.step == 'playing':
        if st.session_state.theme == 'Conectividad':
            gen.timer_count()

        for i, (question, correct_answer) in enumerate(st.session_state.questions):
            st.write(f"Pregunta {i + 1}:")
            st.write(question)

            if st.session_state.difficulty != 'Alta':
                hint = gen.generate_hint(
                    correct_answer, st.session_state.difficulty, st.session_state.theme
                )
                if hint:
                    st.write(f"Pista: {hint}")

            user_answer = st.text_input(f"Respuesta a la pregunta {i + 1}:", key=f"answer_{i}")
            if user_answer:
                if len(st.session_state.user_answers) < i + 1:
                    st.session_state.user_answers.append((user_answer, correct_answer))
                else:
                    st.session_state.user_answers[i] = (user_answer, correct_answer)

        if st.button("Enviar respuestas"):
            correct_count, points = gen.check_points(
                st.session_state.user_answers, st.session_state.difficulty
            )

            st.session_state.correct_count = correct_count
            st.session_state.points = points

            # Almacenar resultados
            new_result = {
                'Fecha y hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'Usuario': st.session_state.user,
                'Email': st.session_state.email,
                'Dificultad': st.session_state.difficulty,
                'Temática': st.session_state.theme,
                'Cantidad de respuestas correctas': correct_count,
                'Puntos': points
            }
            results_df = pd.read_csv(resultado_path)
            results_df = pd.concat([results_df, pd.DataFrame([new_result])], ignore_index=True)
            results_df.to_csv(resultado_path, index=False)

            st.write("Resultados guardados exitosamente.")
            st.session_state.step = 'completed'
            st.rerun()

    if st.session_state.step == 'completed':
        st.write(
            f"Juego completado. Respuestas correctas: {st.session_state.correct_count}. "
            f"Puntos obtenidos: {st.session_state.points}."
        )
        st.write("Puede ver los datos de su última partida al final del Ranking.")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Volver a jugar"):
                st.session_state.step = 'start'
                st.rerun()
        with col2:
            if st.button("Ir al Ranking"):
                st.switch_page("pages/05_Ranking.py")
            if st.button('Cerrar Sesión'):
                st.session_state.email = None
                st.session_state.user = None
                st.session_state.step = 'start'
                st.rerun()
else:
    st.subheader("Antes de jugar, debes Iniciar Sesión")
    st.write("Si su usuario ya esta registrado y no aparece, por favor espere. Streamlit puede presentar DELAY : ) ")
    st.write("Puede probar recargando la pagina.")
    Sesiones.login_form()
    st.subheader("¿No tienes usuario?, Regístrate")
    if st.button('Registrarse'):
        st.switch_page("pages/03_Formulario de Registro.py")
