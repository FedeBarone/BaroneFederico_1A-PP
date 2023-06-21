#------------------------------------------------------MODULO FUNCIONES ORDENAMIENTO----------------------------------------------------
def ordenar_lista_dict(lista: list, key: str,  key_dos: str):
    """_summary_
    Ordena una lista de diccionarios por doble criterio
    Args:
        lista (list): lista a recorrer y ordenar
        key (str): campo de la lista a comparar
        key_dos (str): campo de la lista a comparar
    """
    tam = len(lista)
    for i in range(tam -1):
        for j in range(i + 1, tam):
            if lista[i][key] == lista[j][key] and lista[i][key_dos] < lista[j][key_dos] or lista[i][key] > lista[j][key]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenar_lista_dict_dos(lista: list, key: str,  key_dos: str):
    """_summary_
    Ordena una lista de diccionarios por doble criterio(ascendente y si hay igualdad descendente)
    Args:
        lista (list): lista a recorrer y ordenar
        key (str): campo de la lista a comparar
        key_dos (str): campo de la lista a comparar
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i]["marca"] > lista[j]["marca"] or (lista[i]["marca"] == lista[j]["marca"] and lista[i]["precio"] < lista[j]["precio"]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux