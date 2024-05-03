from pathlib import Path
import csv

def lakes_filter(lakes):
    """
    Filtra los lagos de Argentina por tamaño según la superficie que ocupan.

    Muestra los nombres de los lagos que corresponden al tamaño ingresado por el usuario.
    
    Args: 
        lakes: Una direccion del archivo donde se encuentran los datos de los lagos argentinos.
    
    Returns:
        None
    """
    while (True):
        tam = input("Ingrese el tamaño del lago según la superficie que ocupa ('chico', 'medio', 'grande'): ")
        
        #Hasta que el usuario no ingrese un valor válido no sale
        if(tam == 'chico' or tam == 'medio' or tam == 'grande'):
            break
        else:
            print("valor no válido")
            
    #declaro un constante en donde esta la columna sub_tamaño y el nombre del lago        
    sub_tamaño = 5
    nombre_lago = 0
    
    with open(lakes, 'r', encoding="utf-8") as file :
        csv_reader = csv.reader(file)
        for line in csv_reader:
            if line[sub_tamaño] == tam:
                print(line[nombre_lago], end= " ")

if __name__ == "__main__":
    root = Path('datasets_custom') / "lagos_arg_custom.csv"
    lakes_filter(root)
    