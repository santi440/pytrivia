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
    Cuenta el tiempo restante del temporizador y lo muestra en la interfaz de Streamlit.
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

def load_dataframe(theme):
    """
    Carga el DataFrame adecuado basado en el tema seleccionado.

    Parameters:
    - theme: Tema de las preguntas.

    Returns:
    - DataFrame: DataFrame cargado con los datos del tema correspondiente.
    """
    base_path = Path(__file__).resolve().parent.parent.parent / 'datasets_custom'
    file_paths = {
        "Aeropuertos": 'ar-airports-custom.csv',
        "Lagos": 'lagos_arg_custom.csv',
        "Conectividad": 'Conectividad_Internet.csv',
        "Censo 2022": 'Censo_Modificado.csv'
    }
    df = pd.read_csv(base_path / file_paths[theme])
    return df

def filter_dataframe(df, theme):
    """
    Filtra las filas que tienen valores NaN en las columnas relevantes basadas en el tema.

    Parameters:
    - df: DataFrame a filtrar.
    - theme: Tema de las preguntas.

    Returns:
    - DataFrame: DataFrame filtrado.
    """
    columns_to_check = {
        "Aeropuertos": ["municipality", "name", "prov_name", "elevation_name", "iata_code"],
        "Lagos": ["Nombre", "Ubicación", "Superficie (km²)", "Profundidad máxima (m)"],
        "Conectividad": [],
        "Censo 2022": [
            "Total de población",
            "Población en situación de calle(²)",
            "Porcentaje de población en situación de calle",
            "Mujeres Total de población",
            "Varones Total de población"
        ]
    }
    if theme == "Lagos":
        df['Nombre'] = df['Nombre'].str[5:]
    return df.dropna(subset=columns_to_check[theme])

def get_random_row(df, used_rows):
    """
    Obtiene una fila aleatoria del DataFrame que no se haya usado antes.

    Parameters:
    - df: DataFrame del cual obtener la fila.
    - used_rows: Lista de filas usadas previamente.

    Returns:
    - Series: Fila seleccionada aleatoriamente.
    """
    row = df.sample(n=1).iloc[0]
    while row.name in used_rows:
        row = df.sample(n=1).iloc[0]
    used_rows.append(row.name)
    return row

def generate_question(row, theme):
    """
    Genera una pregunta basada en la fila y el tema proporcionados.

    Parameters:
    - row: Fila del DataFrame con los datos para la pregunta.
    - theme: Tema de las preguntas.

    Returns:
    - Tuple: (Pregunta, Respuesta correcta).
    """
    match theme:
        case "Aeropuertos":
            return generar_pregunta_aeropuertos(row)
        case "Lagos":
            return generar_pregunta_lagos(row)
        case "Conectividad":
            return generar_pregunta_conectividad(row)
        case "Censo 2022":
            return generar_pregunta_censo(row)

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
    shown = ["Nombre", "Provincia", "Superficie (En km²)", "Profundidad Maxima (en metros)"]
    complete = random.choice(completable)
    shown.remove(complete)

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
    showable = ["Provincia", "Partido", "Localidad"]
    complete = random.choice(completable)

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

    for key in showable:
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
    showable = [
        "Total de población",
        "Población en situación de calle(²)",
        "Porcentaje de población en situación de calle",
        "Mujeres Total de población",
        "Varones Total de población"
    ]
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
    df = load_dataframe(theme)
    df = filter_dataframe(df, theme)
    questions_and_answers = []
    used_rows = []

    for _ in range(5):
        row = get_random_row(df, used_rows)
        question, answer = generate_question(row, theme)
        questions_and_answers.append((question, answer))

    if theme == "Conectividad":
        difficulty = st.session_state.difficulty
        match difficulty:
            case 'Fácil':
                amount = 5
            case 'Media':
                amount = 3
            case 'Alta':
                amount = 1
        set_timer(amount)

    return questions_and_answers
