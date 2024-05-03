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
            
def __filtrar_provincias_por_poblacion(ecuacion, censo):
    """
    Filtra las provincias según la ecuación proporcionada y los datos del censo.

    Args:
        ecuacion (str): La ecuación para comparar con la población de cada provincia.
        censo (str): Una direccion del archivo que contiene los datos del censo.

    Returns:
        dict: Un diccionario que contiene las provincias que cumplen con la condición proporcionada.
    """
    with open(censo, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        
        #avanzo una posicion para no considerar el header
        next(reader)
        #avanzo una posicion para no considerar el total del pais
        next(reader)
        
        poblacion_filtrada = {}
        #Leo y filtro las provincias de Argentina según la ecuacion que recibo por parametro
        for line in reader:
            if eval(ecuacion + line[1]):
                #Guardo en el diccionario nombre de provincia y un subdiccionario con 3 listas, en principio vacias
                poblacion_filtrada[line[0]] = {
                                "aeropuertos": [],
                                "lagos": [],
                                "tipos_conectividad": []
                                }
    return poblacion_filtrada

def __agregar_lagos_a_provincias(lagos, provincias):
    """
    Agrega lagos a las provincias correspondientes.

    Args:
        lagos (str): Una direccion del archivo que contiene los datos de los lagos.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los lagos.
    """
    with open(lagos, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            ubicacion = line[1].split(" / ")
        
            for prov in ubicacion: 
                if prov in provincias:
                    provincias[prov]["lagos"].append(line[0])

def __agregar_conectividad_a_provincias(conectividad, provincias):
    """
    Agrega información de conectividad a las provincias correspondientes.

    Args:
        conectividad (str): Una direccion del archivo que contiene los datos de conectividad.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los datos de conectividad.
    """
    with open(conectividad, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        
        #Me quedo con los datos del encabezado para comprobar los tipos de conexión posibles
        header = next(reader)
        
        for line in reader:
            ubicacion = line[0]
        
            if ubicacion in provincias:
                #Desde el 4 al 12 estan los campos de conectividad
                for i in range(4, 13):
                    if line[i] == "SI" and header[i] not in provincias[ubicacion]["tipos_conectividad"]:
                        provincias[ubicacion]["tipos_conectividad"].append(header[i])
                    
def __agregar_aeropuertos_a_provincias(aeropuertos, provincias):
    """
    Agrega información de aeropuertos a las provincias correspondientes.

    Args:
        aeropuertos (str): Una direccion del archivo que contiene los datos de los aeropuertos.
        provincias (dict): Un diccionario que contiene las provincias a las que se agregarán los datos de los aeropuertos.
    """
    with open(aeropuertos, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        
        for line in reader:
            #En la columna 23 del dataset custom esta el campo prov_name y en el 3 el nombre del aeropuerto
            if (line[23] in provincias):
                provincias[line[23]]["aeropuertos"].append(line[3])

def filtrar_segun_poblacion(censo,aeropuertos,lagos,conectividad):
    """
    Muestra información sobre provincias basada en la cantidad de gente proporcionada por el usuario y el signo
    ('>' o '<') para comparar con la población de cada provincia.
    
    Args: 
        censo (str): Una direccion del archivo que contiene los datos del censo.
        aeropuertos (str): Una direccion del archivo que contiene los datos de los aeropuertos.
        lagos (str): Una direccion del archivo que contiene los datos de los lagos.
        conectividad (str): Una direccion del archivo que contiene los datos de los tipos de conectividad en las provincias argentinas.
    
    Returns:
        dict: Un diccionario que contiene los lagos,los tipos de conectividad y aeropuertos sobre provincias que cumplen con la condición proporcionada.
    """
    ecuacion = __pedir_datos_usuario()
    
    provincias = __filtrar_provincias_por_poblacion(ecuacion, censo)
    
    __agregar_aeropuertos_a_provincias(aeropuertos, provincias)
    
    __agregar_lagos_a_provincias(lagos, provincias)
    
    __agregar_conectividad_a_provincias(conectividad, provincias)
    
    return provincias

if __name__ == "__main__":
    censo = Path('datasets_custom') / "Censo_Modificado.csv"
    aeropuertos = Path('datasets_custom') / "ar-airports-custom.csv"
    lagos = Path('datasets_custom') / "lagos_arg_custom.csv"
    conectividad = Path('datasets_custom') / "Conectividad_Internet.csv"

    provinces = filtrar_segun_poblacion(censo,aeropuertos,lagos,conectividad)
    
    for key, value in provinces.items():
        print("Provincia:", key)
        for sub_key, sub_value in value.items():
            print("  ", sub_key, ":", sub_value)