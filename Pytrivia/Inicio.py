import streamlit as st
from FuncionesSesion import Sesiones

if 'email' not in st.session_state:
    st.session_state.email = None

if(Sesiones.is_user_logged_in()):
    user = Sesiones.get_logged_in_user()
    user = user['Usuario'].values[0]
    st.title(f"Bienvenido de nuevo a Pytrivia, {user} ")
else:
    st.title("Bienvenido a Pytrivia")
    
st.header("Descripción del Juego")
st.write("""
    PyTrivia es juego de preguntas y respuestas diseñado para poner a prueba tus conocimientos
    en una variedad de temas relacionados con datos de nuestro país junto con un sistema de puntaje ideal para competir contra otros jugadores.
    """)

st.header("Datos Necesarios para Comenzar")
if(Sesiones.is_user_logged_in()):
    st.write(f"""
        Para empezar a jugar, dirígete a la sección de Juego.
        """)
else:
    st.write(f"""
        Anetes de comenzar necesitas Registrarte o Iniciar Sesion en la sección de Registro.
        Luego, dirígete a la sección de Juego.
        """)

st.header("Instrucciones Básicas")
st.write(f"""
    1. Regístrate en la sección de Registro.
    2. Navega a la página Juego haciendo click aquí o usando el menú de la izquierda.
    3. Selecciona una categoría de preguntas.
    4. Ajusta la dificultad según tu preferencia.
    5. Responde las preguntas que se presenten y acumula puntos.
    6. Revisa tu puntuación al final de cada partida en la sección de Estadisticas.
    """)

st.header("Funcionamiento del Parámetro Dificultad")
st.write("""
    En PyTrivia, podés ajustar la dificultad del juego según tu nivel de conocimiento:
    - **Fácil:** Se proporciona una pista detallada.  
    - **Media:** Se proporciona una pista general.  
    - **Alta:** No se proporciona ninguna pista.
    
    La dificultad afecta tanto la complejidad de las preguntas como la cantidad de puntos que podés ganar.
    Además, podés elejir la temática de las preguntas:
         - **Aeropuertos**
         - **Lagos**
         - **Conectividad**
         - **Último Censo (2022)**

    El parámetro de dificultad en la temática de Conectividad funciona de manera diferente:
    - **Fácil:** Tienes 5 minutos para responder.  
    - **Media:** Tienes 3 minutos para responder.    
    - **Alta:** Tienes 1 minuto para responder.
    """)

st.header("Detalles Adicionales")
st.write("""
    - Revisa el ranking para ver cómo te comparas con otros jugadores.
    """)



# Configurar el menú de la aplicación
st.sidebar.title("Menú")
selected = st.sidebar.selectbox("Ir a", ["Inicio", "Jugar Trivia", "Ranking", "Iniciar Sesion", "Datos", "Estadisticas"])

if selected == "Jugar Trivia":
    st.switch_page("pages/02_Juego.py")
elif selected == "Ranking":
    st.switch_page("pages/05_Ranking.py")
elif selected == "Iniciar Sesion":
    st.switch_page("pages/03_Formulario de Registro.py")
elif selected == "Datos":
    st.switch_page("pages/01_Datos.py")
elif selected == "Estadisticas":
    st.switch_page("pages/06_Estadisticas.py")