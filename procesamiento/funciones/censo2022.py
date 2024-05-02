import csv
#se importan las librerías a utilizar por este módulo

def create_modified_file(file_route,new_file_route):
    """
    La funcion recibe como parámetro las rutas de los archivos que utilizará para leer y crear
    Lee el archivo 'c2022_tp_c_resumen_adaptado.csv', toma sus datos y los pasa al nuevo archivo generado 
    agregando la columna 'Porcentaje de población en situación de calle' con sus respectivos datos numéricos.
    """

    #Se utiliza la sentencia "with" para manejar los archivos, aclarando el modo de abrirlos y su codificacion
    with open(file_route,'r', encoding = 'UTF-8') as base, open(new_file_route,'w', encoding = 'UTF-8',newline="") as new:
            reader_csv = csv.reader(base)
            writer_csv = csv.writer(new)

            header = []
            header = next(reader_csv)
            header.append('Porcentaje de población en situación de calle')
            writer_csv.writerow(header) #Paso el header (primera línea) al nuevo archivo agregando el título de la nueva columna
            
            for line in reader_csv:
                #Recorro todas las lineas del archivo viejo y las paso modificadas al nuevo
                modified_line = list(map(lambda value : 0 if value in ['///','-'] else value, line))
                #Se reemplazan los caracteres "///" y "-" que puedan existir dentro del dataset por el valor 0
                percentage =  (int(modified_line[4]) / int(modified_line[1])) * 100 if int(modified_line[4]) != 0 else 0
                #Se agrega el porcentaje de personas en situación de calle (datos de la nueva columna)
                modified_line.append(percentage)
                #Corrijo como figura la provincia "Río Negro" por correlación con los demás datasets 
                if modified_line[0] == 'Rio Negro':
                     modified_line[0] = 'Río Negro'
                writer_csv.writerow(modified_line)
                #Escribo los datos modificados en el nuevo archivo