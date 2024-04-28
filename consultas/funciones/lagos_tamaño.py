from pathlib import Path
import csv

def lakes_filter():
    """
    Filtra los lagos de Argentina por tamaño según la superficie que ocupan.

    Muestra los nombres de los lagos que corresponden al tamaño ingresado por el usuario.
    
    Returns:
        None
    """
    lakes = Path('datasets') / "lagos_arg.csv"

    while (True):
        tam = input("Ingrese el tamaño del lago según la superficie que ocupa ('chico', 'medio', 'grande')")
        if(tam == 'chico' or tam == 'medio' or tam == 'grande'):
            break
        else:
            print("valor no válido")

    with open(lakes, 'r', encoding="utf-8") as file :
        csv_reader = csv.reader(file)
        lagos = list(csv_reader)

    tam = "chico"
    filtrado = filter(lambda x: x[6] == tam, lagos)

    for elem in filtrado:
        print(elem[1], end= " ")