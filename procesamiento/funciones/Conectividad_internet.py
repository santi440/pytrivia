#Importamos desde pathlib el metodo Path y el modulo csv
from pathlib import Path
import csv

def create_modified_file(original,new):
        """
        Genera un nuevo archivo CSV con una columna adicional indicando si el individuo 
        posee conectividad a internet, basado en un archivo CSV de origen.

        Args:
             original (str): Una direccion del archivo que contiene los datos de los tipos de conectividad en las provincias argentinas que funcionara como origen de los datos.
             new : Una direccion del archivo donde se creara el nuevo archivo resultante

        Returns:
                None

        Raises:
                FileNotFoundError: Si el archivo de origen no se encuentra.
        """
        # En este diccionario se guardan las provincias que no tienen una representacion directa
        correcciones = {
        "CABA": "Ciudad Autónoma de Buenos Aires",
        "TIERRA DEL FUEGO": "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
        "SANTIAGO DEL ESTERO": "Santiago del Estero",
        "CORDOBA": "Córdoba",
        "TUCUMAN":"Tucumán",
        "RIO NEGRO":"Río Negro",
        "ENTRE RIOS":"Entre Ríos",
        "NEUQUEN": "Neuquén"
    }
        # Función para aplicar las correcciones
        def corregir_provincia(provincia):
                """Si el nombre de provincia esta en correcciones devuelvo el valor, sino devuelvo su version con la primera letra de cada palabra mayuscula"""
                return correcciones.get(provincia, provincia.capitalize().title())
        

        #Trabajamos sobre nuestros dos archivos a la par 
        with open(original,'r',encoding='utf-8') as in_file, open(new,'w',encoding='utf-8',newline="") as out_file:
                csv_reader = csv.reader(in_file)
                csv_writer = csv.writer(out_file)
                header = next(csv_reader)
                
                #agregamos la nueva columna
                header.append("posee_conectividad")
                csv_writer.writerow(header)
                
                for line in csv_reader:
                        for pos in range(4,13):
                                if(line[pos] == '--'):
                                        line[pos] = 'NO'
                        #Si todos los tipos son 'NO' en posee_conectividad se escribe 'NO', caso contrario se escribe 'SI'               
                        line.append('SI') if ('SI' in line) else line.append('NO')
                        
                        #Modifico el nombre de la provincia antes de escribir
                        line[0] = corregir_provincia(line[0])
                        csv_writer.writerow(line)