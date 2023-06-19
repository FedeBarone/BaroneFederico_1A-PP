#------------------------------------------------------MODULO DE CALCULOS----------------------------------------------------------------
def contar_dato(lista: list, lista_dos: list, key: str):#2
    """_summary_
    Cuenta cuantas veces aparece cada dato especifico en la lista
    Args:
        lista (list): lista a recorrer para inicializar los elementos en 0
        lista_dos (list): lista a recorrer para contar la cantidad de datos que tiene cada valor de la key
        key (str): campo de la lista en el que se va a contar

    Returns:
        _type_: la cantidad de datos de cada valor de la key
    """
    if type(lista) == type(list()) and type(lista_dos) == type(list()) and len(lista) > 0 and len(lista_dos) > 0 and type(key) == type(str()):
        contador = {}
        for elemento in lista:
            contador[elemento] = 0

        for elemento_lista_dos in lista_dos:
            contador[elemento_lista_dos[key]]+=1
            
        return contador
    