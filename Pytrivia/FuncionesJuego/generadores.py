def generar_pregunta_aeropuertos(df):
    fila = df.sample().iloc[0]
    opciones = df[df['type'] == fila['type']].sample(3)
    opciones = opciones.append(fila)
    opciones = opciones.sample(frac=1)  # Mezclar las opciones
    return fila['name'], opciones

def generar_pregunta_lagos(df):
    fila = df.sample().iloc[0]
    opciones = df[df['size'] == fila['size']].sample(3)
    opciones = opciones.append(fila)
    opciones = opciones.sample(frac=1)  # Mezclar las opciones
    return fila['name'], opciones

def generar_pregunta_conectividad(df):
    fila = df.sample().iloc[0]
    opciones = df[df['connectivity_type'] == fila['connectivity_type']].sample(3)
    opciones = opciones.append(fila)
    opciones = opciones.sample(frac=1)  # Mezclar las opciones
    return fila['city'], opciones

def generar_pregunta_censo(df):
    fila = df.sample().iloc[0]
    opciones = df[df['population'] == fila['population']].sample(3)
    opciones = opciones.append(fila)
    opciones = opciones.sample(frac=1)  # Mezclar las opciones
    return fila['jurisdiction'], opciones
