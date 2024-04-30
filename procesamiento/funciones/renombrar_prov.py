def renombar_prov(cadena):
    """
    Elimina la palabra 'Province' de una cadena. Sirve para que los datasets sean homogeneos entre ellos.
    Parametro:
    cadena (string): la cadena de la cual se quiere eliminar 'Province'.
    Retorna la cadena modificada.  
    """
    cadena = cadena.replace('Province', '').strip()
    return cadena