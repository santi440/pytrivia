from pathlib import Path
import csv

def aeropuertos_en_capital():
    """
    Mostrar los aeropuertos en las capitales de cada provincia
    
    Returns: None
    """
    airports = Path('datasets') / "ar-airports.csv"
    argentina = Path('datasets') / "ar.csv"
    
    with open(argentina, 'r', encoding="utf-8") as file :
        capitals = {}
        csv_reader = csv.DictReader(file) 
        for line in csv_reader:
            if(line["capital"] == 'primary' or line["capital"] == 'admin'):
                capitals[line["city"]]= []
       
                
    with open(airports,'r',encoding= 'utf-8')as file:
        csv_reader = csv.DictReader(file) 
        for line in csv_reader:
            muni = line["municipality"].replace("Neuquen", "Neuquén").split(" / ")
            for elem in muni:
                if(elem in capitals.keys()):
                    capitals[elem].append(line["name"])         
      
    for i in capitals.keys():
        print(f"{i}:")
        for airport in capitals[i]:
            print("     " + airport)
    