from pathlib import Path
import csv

def __pedir_datos_usuario():
    """
    Solicita al usuario la cantidad de gente a evaluar y el signo ('>' o '<') para realizar la comparación.

    Returns:
        str: Un String que contiene el valor de la población (int) y el signo ('>' o '<') concatenados.
    """
    while True:
        value = input("Ingrese la cantidad de gente a evaluar (número entero): ")
        if value.isdigit():
            symbol = input("Ingrese '<' si desea evaluar que la provincia tiene más gente, o '>' si desea evaluar menos gente: ")
            if (symbol == '>' or symbol == '<'):
                return value + symbol
            else:
                print("Por favor, ingrese '>' o '<'.")
        else:
            print("Por favor, ingrese un número entero")
            

def __leer_archivo_csv(ruta):
    """
    Lee un archivo CSV y devuelve sus datos.

    Args:
        ruta (str): La ruta del archivo CSV a leer.

    Returns:
        list: Una lista que contiene los datos del archivo CSV, donde cada elemento es una fila del archivo.
    """
    with open(ruta, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def __filtrar_provincias_por_poblacion(ecuacion, datos_censo):
    """
    Filtra las provincias según la ecuación proporcionada y los datos del censo.

    Args:
        ecuacion (str): La ecuación para comparar con la población de cada provincia.
        datos_censo (list): Una lista que contiene los datos del censo, donde cada elemento es una fila.

    Returns:
        dict: Un diccionario que contiene las provincias que cumplen con la condición proporcionada.
    """
    poblacion_filtrada = {}
    for line in datos_censo:
        if eval(ecuacion + line[1]):
            #Guardo en el diccionario nombre de provincia y un subdiccionario con 3 listas, en principio vacias
            poblacion_filtrada[line[0]] = {
                "aeropuertos": [],
                "lagos": [],
                "tipos_conectividad": []
            }
    return poblacion_filtrada

def __agregar_lagos_a_provincias(datos_lagos, provincias):
    """
    Agrega lagos a las provincias correspondientes.

    Args:
        datos_lagos (list): Una lista que contiene los datos de los lagos.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los lagos.
    """
    for line in datos_lagos:
        ubicacion = line[1].split(" / ")
        
        for prov in ubicacion: 
            if prov in provincias:
                provincias[prov]["lagos"].append(line[0])

def __agregar_conectividad_a_provincias(datos_conectividad, header, provincias):
    """
    Agrega información de conectividad a las provincias correspondientes.

    Args:
        datos_conectividad (list): Una lista que contiene los datos de conectividad.
        header (list): Una lista que contiene los encabezados de los datos de conectividad.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los datos de conectividad.
    """
    
    for line in datos_conectividad:
        ubicacion = line[0]
        
        if ubicacion in provincias:
            #Desde el 4 al 12 estan los campos de conectividad
            for i in range(4, 13):
                if line[i] == "SI" and header[i] not in provincias[ubicacion]["tipos_conectividad"]:
                    provincias[ubicacion]["tipos_conectividad"].append(header[i])
                    
def __agregar_aeropuertos_a_provincias(datos_aeropuertos, provincias):
    """
    Agrega información de aeropuertos a las provincias correspondientes.

    Args:
        datos_aeropuertos (list): Una lista que contiene los datos de los aeropuertos.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los datos de los aeropuertos.
    """
    for line in datos_aeropuertos:
            #En la columna 24 del dataset custom esta el campo prov_name y en el 3 el nombre del aeropuerto
            if (line[24] in provincias):
                provincias[line[24]]["aeropuertos"].append(line[3])

def mostrarSegunPoblacion():
    """
    Muestra información sobre provincias basada en la cantidad de gente proporcionada por el usuario y el signo
    ('>' o '<') para comparar con la población de cada provincia.
    
    Returns:
        dict: Un diccionario que contiene los lagos,los tipos de conectividad y aeropuertos sobre provincias que cumplen con la condición proporcionada.
    """
    ecuacion = __pedir_datos_usuario()
    
    censo = Path('..','datasets') / "c2022_tp_c_resumen_adaptado.csv"
    aeropuertos = Path('..','datasets_custom') / "ar-airports.csv"
    lagos = Path('..','datasets') / "lagos_arg.csv"
    conectividad = Path('..','datasets_custom') / "Conectividad_Internet.csv"
    
    datos_censo = __leer_archivo_csv(censo)
    provincias = __filtrar_provincias_por_poblacion(ecuacion, datos_censo[2:])
    
    datos_aeropuertos = __leer_archivo_csv(aeropuertos)
    __agregar_aeropuertos_a_provincias(datos_aeropuertos, provincias)
    
    datos_lagos = __leer_archivo_csv(lagos)
    __agregar_lagos_a_provincias(datos_lagos, provincias)
    
    datos_conectividad = __leer_archivo_csv(conectividad)
    header = datos_conectividad[0]
    datos_conectividad = datos_conectividad[1:]
    __agregar_conectividad_a_provincias(datos_conectividad, header, provincias)
    
    return provincias