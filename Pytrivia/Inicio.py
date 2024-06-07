import streamlit as st
from pathlib import Path

print(Path.cwd())
st.header('Pytrivia')

st.subheader('Integrantes')
st.write('Federico Kesselman 23786/4')
st.write('Ignacio Battaglino 24595/3')
st.write('Santiago Marcos 23345/0')
st.write('Bautista Rosli 23539/9')

st.title("Bienvenido a PyTrivia")
    
st.header("Descripción del Juego")
st.write("""
    PyTrivia es juego de preguntas y respuestas diseñado para poner a prueba tus conocimientos
    en una amplia variedad de temas junto con un sistema de puntaje ideal para competir contra otros jugadores.
    """)

st.header("Datos Necesarios para Comenzar")
st.write(f"""
    Para empezar a jugar, solo necesitas:
    - Registrarte en la sección de {st.page_link("pages/03_Formulario_de_Registro.py", label = "Formulario de Registro")}.
    """)

st.header("Instrucciones Básicas")
st.write(f"""
    1. Regístrate en la sección de {st.page_link("pages/03_Formulario_de_Registro.py", label = "Formulario de Registro")}.
    2. Navega a la página {st.page_link("pages/02_Juego.py", label = "Juego")} haciendo click aquí o usando el menú de la izquierda.
    3. Selecciona una categoría de preguntas.
    4. Ajusta la dificultad según tu preferencia.
    5. Responde las preguntas que se presenten y acumula puntos.
    6. Revisa tu puntuación al final de cada partida en la sección de {st.page_link("pages/06_Estadisticas.py", label = "Estadísticas")}.
    """)

st.header("Funcionamiento del Parámetro Dificultad")
st.write("""
    En PyTrivia, podés ajustar la dificultad del juego según tu nivel de conocimiento:
    - **Fácil**: Preguntas más sencillas para un calentamiento.
    - **Intermedio**: Preguntas de dificultad media para jugadores con conocimientos generales.
    - **Difícil**: Preguntas desafiantes para expertos.
    
    La dificultad afecta tanto la complejidad de las preguntas como la cantidad de puntos que podés ganar.
    """)

st.header("Detalles Adicionales")
st.write("""
    - Revisa el ranking para ver cómo te comparas con otros jugadores.
    """)

# Configurar el menú de la aplicación
st.sidebar.title("Menú")
st.sidebar("Ir a", ["Inicio", "Jugar Trivia", "Ranking", "Perfil", "Configuración"])