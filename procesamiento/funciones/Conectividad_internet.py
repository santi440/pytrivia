#Importamos desde pathlib el metodo Path y el modulo csv
from pathlib import Path
import csv

def create_modified_file():
        """
        Genera un nuevo archivo CSV con una columna adicional indicando si el individuo 
        posee conectividad a internet, basado en un archivo CSV de origen.

        Args:
                None

        Returns:
                None

        Raises:
                FileNotFoundError: Si el archivo de origen no se encuentra.
        """
        #Creamos las rutas del archivo de origen y el nuevo que vamos a crear
        original = Path('..','datasets') / "Conectividad_Internet.csv"
        new = Path('..','datasets_custom') / "Conectividad_Internet.csv"

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
                        #Si todos los tipos son 'SI' en posee_conectividad se escribe 'SI', caso contrario se escribe 'NO'               
                        line.append('NO') if ('NO' in line) else line.append('SI')    
                        csv_writer.writerow(line)