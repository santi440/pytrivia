def degrees_to_decimal(string_degrees):
    """
    Convierte coordenadas en formato de grados, minutos y segundos, en decimal.

     Args: 
        String con las coordenadas. Formato GG°MM'SS"<orientación>

     Returns: 
        Flotante con coordenadas en formato decimal.
    """

    # elimina caracteres espaciales dejando numeros y punto cardinal 
    special_characters = ('°', "'", '"')
    for character in special_characters:
        if character in string_degrees:
            string_degrees = string_degrees.replace(character, ' ') 
    
    # separa string en lista
    string_degrees = string_degrees.split(' ')
    
    # toma valores de la lista
    degrees = int(string_degrees[0])
    minutes = int(string_degrees[1]) / 60
    seconds = int(string_degrees[2]) / 3600
    compass = (string_degrees[3])
    
    decimal = degrees + minutes + seconds
    
    # si es sur / oeste el valor es negativo
    if compass == 'S' or compass == 'O':
        decimal = -decimal

    return float(decimal)