from pathlib import Path
import csv

def aeropuertos_en_capital(airports,argentina):
    """
    Mostrar los aeropuertos en las capitales de cada provincia
    
    Args:
        airports: Una direccion del archivo donde se encuentran aeropuertos.
        argentina: Una direccion del archivo donde se encuentran las capitales argentinas.
        
    Returns: None
    """
    
    with open(argentina, 'r', encoding="utf-8") as file :
        capitals = {}
        csv_reader = csv.DictReader(file) 
        for line in csv_reader:
            
            #Me guardo las capitales que figuren como primary o admin
            if(line["capital"] == 'primary' or line["capital"] == 'admin'):
                #Ciudad Autónoma de Buenos Aires aparece mal en el dataset, de las capitales es la única que no está como debe
                if line["admin_name"] == "Buenos Aires, Ciudad Autónoma de":
                    capitals["Ciudad Autónoma de Buenos Aires"] = []
                else:
                    capitals[line["city"]] = []       
                
    with open(airports,'r',encoding= 'utf-8')as file:
        csv_reader = csv.DictReader(file) 
        for line in csv_reader:
            #Primero reemplazo el campo de municipalidad si es que aparece Neuquén sin tilde (es el único que encontre que le faltaba)
            #y aplico un split para separar los que vengan por "/"
            muni = line["municipality"].replace("Neuquen", "Neuquén").split(" / ")
            for elem in muni:
                if(elem in capitals.keys()):
                    #Si esta en el diccionario de capitales agrego el nombre del aeropuerto
                    capitals[elem].append(line["name"])         
      
    for i in capitals.keys():
        print(f"{i}:")
        for airport in capitals[i]:
            print("     " + airport)
    
if __name__ == "__main__":
    airports = Path('datasets_custom') / "ar-airports-custom.csv"
    argentina = Path('datasets') / "ar.csv"
    aeropuertos_en_capital(airports,argentina)