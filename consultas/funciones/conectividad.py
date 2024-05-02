import csv
from pathlib import Path

# Defino la ruta del archivo a abrir
file_route = Path('..','datasets_custom')/'Conectividad_Internet.csv'

def connectivity_type_quantities (): #Inciso 10
    """
    Lee un archivo CSV que contiene información sobre los diferentes tipos de conectividad en varias localidades.
    La función cuenta la cantidad de cada tipo de conectividad que está presente en el archivo.
    La función imprime por consola la cantidad de cada tipo de conectividad presente en el archivo.
    """
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

    # Imprimo el diccionario con todas las cantidades de cada tipo de conectividad
    for connectivity_type, quantity in connectivity_quantities.items():
        print(f'{connectivity_type}: {quantity}')



def provinces_optical_fiber() : 
    """
    Lee un archivo CSV que contiene información sobre la disponibilidad de fibra óptica en diferentes localidades de las provincias.
    La función identifica las provincias donde todas las localidades tienen fibra óptica.
    La función imprime por consola el nombre de las provincias donde todas las localidades tienen fibra óptica.
    """
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
                # Si ya guardé la provincia, reviso si la misma tiene fibra óptica, si lo tiene, reviso si la nueva que leo tambíen posee fibra óptica
                # En caso de tener fibra óptica esta nueva lectura, hago un continue para seguir leyendo las próximas líneas
                if optical_fiber == 'SI':
                    continue
                else:
                    # Si no posee fibra óptica, actualizo el valor
                    provinces_cities[province] = optical_fiber
        print('Provincias cuya totalidad de localidades posee fibra óptica : ')
        for key in provinces_cities:
            # Recorro las provincias guardadas e imprimo aquellas que tienen fibra óptica en la totalidad de sus localidades
            if(provinces_cities[key] == 'SI'):
                print(f'    {key}')



def province_capital_connectivity():
    """
    Lee dos archivos CSV para obtener información sobre las provincias argentinas y su conectividad a Internet.
    del primer archivo toma los datos sobre las capitales de las provincias y del segundo archivo toma información sobre la conectividad de las localidades.
    La función identifica cuales son las capitales de las provincias y verifica si tienen información sobre coenctividad. Luego imprime un resumen de la información.
    """
    # Ruta del archivo que contiene información sobre las capitales y provincias
    file_capital = Path('..', 'datasets') / 'ar.csv'
    # Lista para almacenar las provincias
    provinces = []
    # Diccionario para almacenar las ciudades de cada provincia
    provinces_cities = {}
    # Lista para almacenar las ciudades capitales
    capital_cities = []

    # Abro el primer archivo para tomar la información sobre capitales y provincias
    with open(file_capital, 'r', encoding='UTF-8') as csv_ar:
        # Leo el archivo CSV como un diccionario para acceder a su contenido de manera más sencilla
        ar_reader = csv.DictReader(csv_ar)
        # Itero sobre cada fila del archivo
        for row in ar_reader:
            # Obtengo los datos de la fila
            city = row['city']
            capital = row['capital']
            province = row['admin_name']

            # Corrijo nombres de provincias y ciudades si es necesario (por correlación con el siguiente archivo)
            if province == 'Buenos Aires, Ciudad Autónoma de':
                province = 'Ciudad Autónoma de Buenos Aires'
                city = 'Ciudad Autónoma de Buenos Aires'

            if (city == 'Catamarca'):
                city = 'San Fernando del Valle de Catamarca'

            # Agrego la ciudad capital a la lista si es capital
            if capital in ['primary', 'admin']:
                capital_cities.append(city)

                # Agrego la provincia a la lista si no lo está
                if province not in provinces:
                    provinces.append(province)
                    # Inicializo la lista dentro de la clave del diccionario (la provincia contiene su ciudad capital)
                    provinces_cities[province] = [city]

    # Abro el segundo archivo para agregar información sobre conectividad
    with open(file_route, 'r', encoding='UTF-8') as csv_conec:
        conec_reader = csv.DictReader(csv_conec) # De igual manera que el anterior,lo leo como un diccionario
        # Itero sobre cada fila del archivo
        for row in conec_reader:
            province = row['Provincia']
            city = row['Localidad']
            connectivity = row['posee_conectividad']

            # Corrijo nombres por correlación con los datos tomados del anterior archivo
            if city == 'San Miguel de Tucumán (Est. Tucumán)':
                city = 'San Miguel de Tucumán'
            if(city == 'San Salvador de Jujuy (Est. Jujuy)'):
                city = 'San Salvador de Jujuy'

            if(province == 'Ciudad Autónoma de Buenos Aires' and len(provinces_cities[province]) == 1):
                city = 'Ciudad Autónoma de Buenos Aires' # Utilizo len debido a que en este dateset, la localidad 'Ciudad Autonoma de buenos aires' no existe como tal

            # Verifico si la ciudad es una capital y si la provincia está en la lista
            if (city in provinces_cities[province]) :
                # Agrego la información de conectividad si es válida
                provinces_cities[province].append(connectivity if connectivity in ('SI','NO') else 'Conectividad Desconocida')
    
    # Imprimo la información de las provincias y sus capitales
    for province, cities in provinces_cities.items():
        # Obtengo la ciudad capital
        capital_city = cities[0]
        # Obtengo la información de conectividad
        connectivity_info = cities[1]
        # Imprimo el nombre de la provincia
        print(f'Provincia: {province}')
        # Imprimo la capital de la provincia
        print(f'    Capital: {capital_city}')
        # Imprimo la información de conectividad
        print(f'    Conectividad: {connectivity_info} \n')