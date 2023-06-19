#------------------------------------------------------MODULO FUNCIONES BUSQUEDA---------------------------------------------------------
def buscar_elemento_en_lista(lista, elemento_a_buscar: str)-> bool:#3BIEN
    """_summary_
    Verifica si un elemento se encuentra disponible o no en una lista, si lo encuentra rompe con la iteracion

    Args:
        lista(list) lista a recorrer
        elemento_a_buscar(str) elemento a buscar en la lista

    Returns:
        _type_: true si el elemento esta o false si no esta
    """
    if type(lista) == type(list()) and type(elemento_a_buscar) == type(str()) and len(lista) > 0:
        flag_elemento_a_buscar = False
        for elemento in lista:
            if elemento_a_buscar == elemento:
                flag_elemento_a_buscar = True
                break
        return flag_elemento_a_buscar
    

def quitar_repetidos(lista: list, key: str) -> list:#2BIEN
    """_summary_
    Elimina los elementos repetidos de una lista
    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista

    Returns:
        list: retorna una nueva lista sin repetidos
    """
    if type(lista) == type(list()) and type(key) == type(str()) and len(lista) > 0:
        lista_filtrada = []
        for elemento in lista:
                if not buscar_elemento_en_lista(lista_filtrada, elemento[key]):
                    lista_filtrada.append(elemento[key])

        return lista_filtrada
    
