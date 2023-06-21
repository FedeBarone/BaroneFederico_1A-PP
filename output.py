import os
#------------------------------------------------------MODULO FUNCIONES DE SALIDA-----------------------------------------------------
def mostrar_menu_principal(lista: list)->str:
    """_summary_
    Muestra un menu de opciones

    Args:
        lista (list): lista a recorrer

    Returns:
        str: retorna la opcion elegida
    """
    if type(lista) == type(list()) and len(lista) > 0:
        print("========================================")
        print("|            MENU PRINCIPAL            |")
        print("========================================")
        for i in range(len(lista)):
            print(f"|{lista[i]:38s}|")
            print("========================================")
        opcion = input("Ingrese una opcion: ")
        return opcion
    

def salir_del_menu()-> None:
    """_summary_
    Pregunta y valida con s o con n si el usuario quiere salir o no del menu
    Returns:
        _type_: retorna si se eligió s o n
    """
    while True:
        salir = input("Desea salir del menu?[s/n]")
        if salir.isalpha():
            if not (salir != 's' and salir != 'n'):
                break
            else:
                print(
                    "'s' para salir o 'n' para salir del programa")
        else:
            print("No se pueden ingresar numeros")
    return salir


def mostrar_campos(lista, elemento_aux: str, key: str, key_dos: str, key_tres: str)-> None:#3
    """_summary_
    Muestra los campos de una lista de diccionarios
    Args:
        lista (_type_): lista a recorrer
        elemento_aux (str): elemento a comparar
        key (str): campo a comparar con el elemento que viene por parametro
        key_dos (str): campo a imprimir
        key_tres (str): segundo campo a imprimir
    """
    print("=============================================")
    for elemento in lista:
        if elemento_aux == elemento[key]:
            print(f"Nombre: {elemento[key_dos]} | Precio: {elemento[key_tres]}")# 3
    print("=============================================")

def mostrar_campo(lista, elemento_aux: str, key: str, key_dos: str, titulo: str)-> None:#3
    """_summary_
    Muestra el campo de una lista de diccionarios
    Args:
        lista (_type_): lista a recorrer
        elemento_aux (str): elemento a comparar
        key (str): campo a comparar con el elemento que viene por parametro
        key_dos (str): campo a imprimir
        key_tres (str): segundo campo a imprimir
    """
    print("=============================================")
    for elemento in lista:
        if elemento_aux in elemento[key]:
            print(f"{titulo}: {elemento[key_dos]}")# 3
    print("=============================================")

def mostrar_contador_dato(diccionario: dict, titulo: str, titulo_dos: str)-> None:#2
    """_summary_
    Muestra la cantidad de datos que tiene los valores de una key
    Args:
        diccionario (dict): diccionario que contiene la key en la que se van a contar los datos
        titulo (str): nombre de la key 
        titulo_dos (str): el nombre de la cantidad de datos
    """
    for key in diccionario:
        cantidad = diccionario[key]
        print(f"{titulo}: " + key)
        print(f"{titulo_dos}: ", cantidad)
        print("======================================================")
    

def mostrar_campos_cada_marca(marcas,lista ,key: str, key_dos: str, key_tres: str)-> None:#3
    """_summary_
    Muestra por cada marca el nombre y precio del insumo o los insumos que pertenecen a la cara en especifico
    Args:
        lista (_type_): lista a recorrer
        key (str): campo de la lista a verificar
        key_dos (str): campo a mostrar
        key_tres (str): campo a mostrar
    """
    for marca in marcas:
        print("Marca: " +marca)
        for elemento in lista:
            if marca == elemento[key]:
                print(f"Nombre: {elemento[key_dos]} Precio: {elemento[key_tres]}")# 3
        print("=====================================================")


def imprimir_dato(dato: str)-> None: #1.2
    """_summary_
    Muestra un dato

    Args:
        dato (str): dato a mostrar
    """
    if type(dato) == type(str()):
        print(dato)

def mostrar_lista_strings(lista:list, key: str, titulo:str)->None:
    """_summary_
    Muestra una lista de strings
    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista a mostrar
        titulo (str): el nombre del campo
    """
    print("+==========================================================================================+")
    print(f"|                                    {titulo}                                       |")
    print("+==========================================================================================+")
    for elemento in lista:
        print(f"|{elemento[key]:90s}|")
        print("--------------------------------------------------------------------------------------------")