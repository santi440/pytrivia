import pandas as pd
import random
import numpy as np
from pathlib import Path
from unidecode import unidecode

# Función para verificar puntos
def check_points(answers, diff):
    points = 0
    for answer in answers:
        if unidecode(answer[0].lower().replace(" ", "")) == unidecode(str(answer[1]).lower().replace(" ", "")):
            points += 1
    cant=points
    if diff == 'Media':
        points = points * 1.5
    elif diff == 'Alta':
        points = points * 2
    return cant, points

# Función para generar pistas
def generate_hint(answer, difficulty):
    numeric_types = (int, float, np.int64, np.longlong)
    if difficulty == "Fácil":
        if isinstance(answer, numeric_types):
            return f"La respuesta está entre {answer - 5} y {answer + 5}"
        elif isinstance(answer, str) or isinstance(answer, bool):
            answer_str = str(answer)
            return f"La respuesta comienza con '{answer_str[0]}' y termina con '{answer_str[-1]}'"
    elif difficulty == "Media":
        if isinstance(answer, numeric_types):
            return f"La respuesta está entre {answer - 10} y {answer + 10}"
        elif isinstance(answer, str) or isinstance(answer, bool):
            answer_str = str(answer)
            return f"La respuesta comienza con '{answer_str[0]}'"
    return None

# Función para generar preguntas de aeropuertos
def generar_pregunta_aeropuertos(row):
    question = f"Complete la opcion faltante de los siguientes datos de un aeropuerto\n"
    
    # Definir atributos disponibles para completar y mostrar
    completable = ("Municipio","Nombre","Provincia","Elevación")
    showable = ("Municipio","Nombre","Provincia","Elevación")
    
    # Seleccionar aleatoriamente el atributo a completar y los mostrados
    complete = random.choice(completable)
    shown = random.sample(showable, 3)
    
    # Asegurar que el atributo a completar no esté entre los mostrados
    while complete in shown:
        complete = random.choice (completable)
    
    options = {
        "Municipio": "municipality",
        "Nombre": "name",
        "Provincia": "prov_name",
        "Elevación": "elevation_name",
        "Código IATA": "iata_code"
    }
    
    for key in shown:
        question+= f"- {key}: {row[options[key]]}\n"
    
    question+= f"- {complete}: ???????"
        
    correct_answer = row[options[complete]]
    
    return question, correct_answer

# Función para generar preguntas de lagos
def generar_pregunta_lagos(row):
    
    question = f"Complete la opcion faltante de los siguientes datos de un lago\n"
    
    # Definir atributos disponibles para completar y mostrar
    completable = ("Nombre","Provincia")
    showable = ("Nombre","Provincia","Superficie (En km²)","Profundidad Maxima (en metros)")
    
    # Seleccionar aleatoriamente el atributo a completar y los mostrados
    complete = random.choice(completable)
    shown = random.sample(showable, 3)
    
    # Asegurar que el atributo a completar no esté entre los mostrados
    while complete in shown:
        shown = random.sample (showable, 3)
    
    options = {
        "Nombre": "Nombre",
        "Provincia": "Ubicación",
        "Superficie (En km²)": "Superficie (km²)",
        "Profundidad Maxima (en metros)": "Profundidad máxima (m)"
    }
    
    for key in shown:
        question+= f"- {key}: {row[options[key]]}\n"

    question+= f"- {complete}: ???????"
    
    correct_answer = row[options[complete]]
    
    return question, correct_answer

# Función para generar preguntas de conectividad
def generar_pregunta_conectividad(row):
    question = f"Complete con SI o NO la opcion faltante de la siguiente localidad:\n"
    
    # Definir atributos disponibles para completar y mostrar
    completable = ("Tiene ADSL?", "Tiene CABLEMODEM?", "Tiene DIALUP?", "Tiene FIBRAOPTICA?", 
               "Tiene SATELITAL?", "Tiene WIRELESS?", "Tiene TELEFONIAFIJA?", "Tiene 3G?", "Tiene 4G?")

    showable = ("Provincia","Partido","Localidad")
    
    # Seleccionar aleatoriamente el atributo a completar y los mostrados
    complete = random.choice(completable)
    shown = showable
    
    options = {
    "Tiene ADSL?": "ADSL",
    "Tiene CABLEMODEM?": "CABLEMODEM",
    "Tiene DIALUP?": "DIALUP",
    "Tiene FIBRAOPTICA?": "FIBRAOPTICA",
    "Tiene SATELITAL?": "SATELITAL",
    "Tiene WIRELESS?": "WIRELESS",
    "Tiene TELEFONIAFIJA?": "TELEFONIAFIJA",
    "Tiene 3G?": "3G",
    "Tiene 4G?": "4G"
}

    for key in shown:
        question+= f"- {key}: {row[key]}\n"

    question+= f"- {complete}: ???????"
    
    correct_answer = row[options[complete]]
    
    return question, correct_answer

# Función para generar preguntas del censo 2022
def generar_pregunta_censo(row):
    question = f"Cual es la provincia que cumple con los siguientes datos?\n"
    
    # Definir atributos disponibles para completar y mostrar
    showable = ("Total de población","Población en situación de calle(²)","Porcentaje de población en situación de calle","Mujeres Total de población","Varones Total de población")
    
    # Seleccionar aleatoriamente el atributo a completar y los mostrados
    complete = "Jurisdicción"
    shown = random.sample(showable, 3)
    
    for key in shown:
        question+= f"- {key}: {row[key]}\n"
    
    question+= f"- Provincia: ???????"
        
    correct_answer = row[complete]
    
    return question, correct_answer

# Función para generar preguntas basado en la tematica
def generateQuestions(theme):
    base_path = Path(__file__).resolve().parent.parent.parent / 'datasets_custom'
    if theme == "Aeropuertos":
        df = pd.read_csv(base_path / 'ar-airports-custom.csv')
        return [generar_pregunta_aeropuertos(df.sample(n=1).iloc[0]) for _ in range(5)]
    elif theme == "Lagos":
        df = pd.read_csv(base_path / 'lagos_arg_custom.csv')
        return [generar_pregunta_lagos(df.sample(n=1).iloc[0]) for _ in range(5)]
    elif theme == "Conectividad":
        df = pd.read_csv(base_path / 'Conectividad_Internet.csv')
        return [generar_pregunta_conectividad(df.sample(n=1).iloc[0]) for _ in range(5)]
    elif theme == "Censo 2022":
        df = pd.read_csv(base_path / 'Censo_Modificado.csv')
        return [generar_pregunta_censo(df.sample(n=1).iloc[0]) for _ in range(5)]
    return []


if __name__ == "__main__":
    
    print ("hola")

    preguntas=generateQuestions ("Censo 2022")
    
    if preguntas:
        for i, pregunta in enumerate(preguntas, start=1):
            print(f"Pregunta {i}: {pregunta[0]}")
    else:
        print("No se generaron preguntas.")
    
    
