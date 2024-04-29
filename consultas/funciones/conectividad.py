import csv
from pathlib import Path

# Defino la ruta del archivo a abrir
file_route = Path('..','datasets_custom')/'Conectividad_Internet.csv'

def connectivity_type_quantities (): #Inciso 10
    # Abro el archivo CSV en modo lectura
    with open(file_route, 'r', encoding = 'UTF-8') as csv_file:
        #Defino un lector de csv
        reader = csv.reader(csv_file)
    
        # Leo la primera línea del archivo CSV y la divido utilizando splicing correspondiente a los diferentes tipos de conectividad
        first_line = next(reader)
        connectivity_types = first_line[4:13]
    
        # Creo el diccionario connectivity_quantities e inicializo todas las cantidades en 0 a través de una función zip, la cual junta todos los datos en una sola estructura
        # En este caso, creo un diccionario cuyas claves son los tipos de conectividad, y su contenido son las cantidades
        connectivity_quantities = dict(zip(connectivity_types, [0] * len(connectivity_types)))
    
        # Itero sobre cada fila del archivo CSV (empezando desde la segunda fila)
        for row in reader:
            # Itero sobre cada tipo de conectividad en la fila y Actualizo las cantidades si contiene el valor 'SI' en su respectiva columna
            for connectivity_type, value in zip(connectivity_types, row[4:13]):
                if value == 'SI':
                    connectivity_quantities[connectivity_type] += 1

    # Retorno el diccionario con todas las cantidades de cada tipo de conectividad
    return connectivity_quantities



def provinces_optical_fiber() : 
    # Lista para almacenar las provincias únicas, es decir, leerlas sin que se repitan
    provinces = []

    # Diccionario para almacenar las provincias y sus ciudades
    provinces_cities = {}

    # Abro el archivo CSV en modo lectura
    with open(file_route, 'r', encoding= 'UTF-8') as csv_file:
        # Creo un lector CSV que lo interprete como un diccionario en formato clave - valor
        reader = csv.DictReader(csv_file)
    
        # Itero sobre cada fila del archivo CSV y guardo los valores que me interesan en diferentes variables
        for row in reader:
            province = row['Provincia']
            optical_fiber = row['FIBRAOPTICA']
        
            # Verifico si la provincia ya está en la lista de provincias (filtrado de repeticiones)
            if province not in provinces:
                provinces.append(province)
                provinces_cities[province] = optical_fiber
            elif provinces_cities[province] == 'SI':
                if optical_fiber == 'SI':
                    continue
                else:
                    provinces_cities[province] = optical_fiber
        
        for key in provinces_cities:
            if(provinces_cities[key] == 'SI'):
                print(key)



def province_capital_connectivity():
    file_capital = Path('..'/'datasets')/'ar.csv'
    provinces = {}
    with open(file_route, 'r', encoding= 'UTF-8') as csv_conec :
        conec_reader = csv.reader(csv_conec)

    with open(file_capital, 'r', encoding= 'UTF-8') as csv_ar:
        ar_reader = csv.DictReader(csv_ar)
        for row in ar_reader:
            province = row['']

