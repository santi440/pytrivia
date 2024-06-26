import pandas as pd
import random
from pathlib import Path
from unidecode import unidecode
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta
import streamlit as st


def set_timer(amount):
    """
    Establece un temporizador para una cantidad de minutos especificada.

    Parameters:
    - amount: La cantidad de minutos para el temporizador.
    """
    st.session_state.start_time = datetime.now()
    st.session_state.end_time = st.session_state.start_time + timedelta(minutes=amount)


def timer_count():
    """
    Cuenta el tiempo restante del temporizador y muestra en la interfaz de Streamlit.

    Si el tiempo se ha agotado, cambia el estado a 'completed'.
    """
    st_autorefresh(interval=1000)
    if st.session_state.end_time:
        remaining_time = st.session_state.end_time - datetime.now()
        if remaining_time.total_seconds() > 0:
            minutes, seconds = divmod(int(remaining_time.total_seconds()), 60)
            st.write(f"Tiempo restante: {minutes:02d}:{seconds:02d}")
        else:
            st.session_state.step = 'completed'


def check_points(answers, diff):
    """
    Verifica la cantidad de respuestas correctas y calcula los puntos obtenidos según la dificultad.

    Parameters:
    - answers: Lista de tuplas (respuesta dada, respuesta esperada).
    - diff: Dificultad de la pregunta ('Baja', 'Media', 'Alta').

    Returns:
    - Tuple: (Cantidad de respuestas correctas, Puntos obtenidos).
    """
    points = 0
    for answer in answers:
        if unidecode(answer[0].lower().replace(" ", "")) == unidecode(
            str(answer[1]).lower().replace(" ", "")
        ):
            points += 1
    cant = points
    if diff == 'Media':
        points = points * 1.5
    elif diff == 'Alta':
        points = points * 2
    return cant, points


def generate_hint(answer, difficulty):
    """
    Genera una pista basada en la respuesta y la dificultad.

    Parameters:
    - answer: Tupla (respuesta dada, respuesta esperada).
    - difficulty: Dificultad de la pregunta ('Fácil', 'Media').

    Returns:
    - str: Pista generada.
    """

    if difficulty == "Fácil":
        return f"La respuesta comienza con '{answer[0]}' y termina con '{answer[-1]}'"
    else: 
        return f"La respuesta comienza con '{answer[0]}'"


def generar_pregunta_aeropuertos(row):
    """
    Genera una pregunta sobre datos de un aeropuerto para completar.

    Parameters:
    - row: Fila del DataFrame con los datos del aeropuerto.

    Returns:
    - Tuple: (Pregunta, Respuesta correcta).
    """
    question = "Complete la opción faltante de los siguientes datos de un aeropuerto\n"

    completable = ("Municipio", "Provincia")
    shown = ["Municipio", "Nombre", "Provincia", "Elevación"]

    complete = random.choice(completable)
    shown.remove(complete)

    options = {
        "Municipio": "municipality",
        "Nombre": "name",
        "Provincia": "prov_name",
        "Elevación": "elevation_name",
        "Código IATA": "iata_code",
    }

    for key in shown:
        question += f"- {key}: {row[options[key]]}\n"

    question += f"- {complete}: ???????"

    correct_answer = row[options[complete]]

    return question, correct_answer


def generar_pregunta_lagos(row):
    """
    Genera una pregunta sobre datos de un lago para completar.

    Parameters:
    - row: Fila del DataFrame con los datos del lago.

    Returns:
    - Tuple: (Pregunta, Respuesta correcta).
    """
    question = "Complete la opción faltante de los siguientes datos de un lago\n"

    completable = ("Nombre", "Provincia")
    showable = ("Nombre", "Provincia", "Superficie (En km²)", "Profundidad Maxima (en metros)")

    complete = random.choice(completable)
    shown = random.sample(showable, 3)

    while complete in shown:
        shown = random.sample(showable, 3)

    options = {
        "Nombre": "Nombre",
        "Provincia": "Ubicación",
        "Superficie (En km²)": "Superficie (km²)",
        "Profundidad Maxima (en metros)": "Profundidad máxima (m)",
    }

    for key in shown:
        question += f"- {key}: {row[options[key]]}\n"

    question += f"- {complete}: ???????"

    correct_answer = row[options[complete]]

    return question, correct_answer


def generar_pregunta_conectividad(row):
    """
    Genera una pregunta sobre conectividad de una localidad para completar con SI o NO.

    Parameters:
    - row: Fila del DataFrame con los datos de la localidad.

    Returns:
    - Tuple: (Pregunta, Respuesta correcta).
    """
    question = "Complete con SI o NO la opción faltante de la siguiente localidad:\n"

    completable = (
        "Tiene ADSL?",
        "Tiene CABLE MODEM?",
        "Tiene DIALUP?",
        "Tiene FIBRA OPTICA?",
        "Tiene SEÑAL SATELITAL?",
        "Tiene WIFI?",
        "Tiene TELEFONIA FIJA?",
        "Tiene 3G?",
        "Tiene 4G?",
    )

    showable = ("Provincia", "Partido", "Localidad")

    complete = random.choice(completable)
    shown = showable

    options = {
        "Tiene ADSL?": "ADSL",
        "Tiene CABLE MODEM?": "CABLEMODEM",
        "Tiene DIALUP?": "DIALUP",
        "Tiene FIBRA OPTICA?": "FIBRAOPTICA",
        "Tiene SEÑAL SATELITAL?": "SATELITAL",
        "Tiene WIFI?": "WIRELESS",
        "Tiene TELEFONIA FIJA?": "TELEFONIAFIJA",
        "Tiene 3G?": "3G",
        "Tiene 4G?": "4G",
    }

    for key in shown:
        question += f"- {key}: {row[key]}\n"

    question += f"- {complete}:  ¿Si o No?"

    correct_answer = row[options[complete]]

    return question, correct_answer


def generar_pregunta_censo(row):
    """
    Genera una pregunta sobre datos del censo 2022 para completar.

    Parameters:
    - row: Fila del DataFrame con los datos del censo 2022.

    Returns:
    - Tuple: (Pregunta, Respuesta correcta).
    """
    question = "Cual es la provincia que cumple con los siguientes datos?\n"

    showable = (
        "Total de población",
        "Población en situación de calle(²)",
        "Porcentaje de población en situación de calle",
        "Mujeres Total de población",
        "Varones Total de población",
    )

    complete = "Jurisdicción"
    shown = random.sample(showable, 3)

    for key in shown:
        question += f"- {key}: {row[key]}\n"

    question += f"- Provincia: ???????"

    correct_answer = row[complete]

    return question, correct_answer


def generate_questions(theme):
    """
    Genera 5 preguntas basadas en la temática seleccionada.

    Parameters:
    - theme: Tema de las preguntas.

    Returns:
    - List of Tuples: Lista de preguntas y respuestas generadas.
    """
    base_path = Path(__file__).resolve().parent.parent.parent / 'datasets_custom'
    questions_and_answers = []
    used_rows = []

    if theme == "Aeropuertos":
        df = pd.read_csv(base_path / 'ar-airports-custom.csv')
        df = df.dropna(subset=["municipality", "name", "prov_name", "elevation_name", "iata_code"])

        for _ in range(5):
            row = df.sample(n=1).iloc[0]
            while row.name in used_rows:
                row = df.sample(n=1).iloc[0]
            used_rows.append(row.name)
            question, answer = generar_pregunta_aeropuertos(row)
            questions_and_answers.append((question, answer))

    elif theme == "Lagos":
        df = pd.read_csv(base_path / 'lagos_arg_custom.csv')
        df = df.dropna(subset=["Nombre", "Ubicación", "Superficie (km²)", "Profundidad máxima (m)"])

        for _ in range(5):
            row = df.sample(n=1).iloc[0]
            while row.name in used_rows:
                row = df.sample(n=1).iloc[0]
            used_rows.append(row.name)
            question, answer = generar_pregunta_lagos(row)
            questions_and_answers.append((question, answer))

    elif theme == "Conectividad":
        df = pd.read_csv(base_path / 'Conectividad_Internet.csv')
        df = df.dropna()

        for _ in range(5):
            row = df.sample(n=1).iloc[0]
            while row.name in used_rows:
                row = df.sample(n=1).iloc[0]
            used_rows.append(row.name)
            question, answer = generar_pregunta_conectividad(row)
            questions_and_answers.append((question, answer))

        difficulty = st.session_state.difficulty

        match difficulty:
            case 'Fácil':
                amount = 5
            case 'Media':
                amount = 3
            case 'Alta':
                amount = 1
        set_timer(amount)

    elif theme == "Censo 2022":
        df = pd.read_csv(base_path / 'Censo_Modificado.csv')
        df = df.dropna(subset=[
            "Total de población",
            "Población en situación de calle(²)",
            "Porcentaje de población en situación de calle",
            "Mujeres Total de población",
            "Varones Total de población",
        ])

        for _ in range(5):
            row = df.sample(n=1).iloc[0]
            while row.name in used_rows:
                row = df.sample(n=1).iloc[0]
            used_rows.append(row.name)
            question, answer = generar_pregunta_censo(row)
            questions_and_answers.append((question, answer))

    return questions_and_answers
