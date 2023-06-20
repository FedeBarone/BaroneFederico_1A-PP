from insumos_copy import *
from input_copy import*
from calculos_copy import*
from ordenamientos_copy import*
#------------------------------------------------------MODULO DE INFORMES----------------------------------------------------------------
def cargar_datos_desde_archivo(path: str)-> list: #1
    """_summary_
    Carga los datos del archivo insumos csv

    Args:
        path (str): ruta del archivo a leer

    Returns:
        list: devuelve una lista de diccionarios
    """
    print("Archivo cargado correctamente!")
    return leer_csv(path)

def listar_cantidad_por_marca(lista: str): #2
    """_summary_
    Muestra la cantidad de insumos que tiene cada marca
    Args:
        lista (str): lista a recorrer
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_filtrada = quitar_repetidos(lista, "marca")
        diccionario = contar_dato(lista_filtrada, lista, "marca")
        mostrar_contador_dato(diccionario, "Marca", "Cantidad isumos")

def listar_insumos_por_marca(lista: list, key_uno: str, key_dos: str, key_tres: str)-> None: #3
    """_summary_
    Muestra por cada marca el nombre y precio del insumo o los insumos que pertenecen a la marca en especifico

    Args:
        lista (list): lista a recorrer
        key_uno (str): campo de la lista
        key_dos (str): campo de la lista
        key_tres (str): campo de la lista
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(key_uno) == type(str()) and type(key_dos) == type(str()) and type(key_tres) == type(str()):
        lista_filtrada = quitar_repetidos(lista, key_uno)
        mostrar_campos_cada_marca(lista_filtrada,lista, key_uno, key_dos, key_tres)

def buscar_insumo_por_característica(texto: str, lista: str)-> None: #4
    """_summary_
    Pide al usuario una caracteristica y muestra el nombre de todos los insumos que tiene dicha caracteristica
    Args:
        lista (list): lista a recorrer
        texto (str): el texto que se ingresa para pedir la caracteristica
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(texto) == type(str()):
        patron_caracteristicas = imprimir_patron_caracteristicas()
        mostrar_lista_strings(lista, "caracteristicas", "Caracteristicas")
        caracteristica = ingresar_cadena_valida_con_o_sin_patron(texto, patron_caracteristicas, True)
        mostrar_campo(lista, caracteristica, "caracteristicas", "nombre", "Nombre")

def listar_insumos_ordenados(lista: list, key_uno: str, key_dos: str): #5
    """_summary_
    Ordena los insumos por doble criterio ,la marca de forma ascendente y, ante marcas iguales, por precio descendente. Y muestra los
    insumos con todos sus datos
    Args:
        lista (list): lista a recorrer
        key_uno (str): campo a comparar
        key_dos (str): campo a comparar
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(key_uno) == type(str()) and type(key_dos) == type(str()):
        ordenar_lista_dict(lista, key_uno, key_dos)
        mostrar_insumos(lista)

def realizar_compras(lista: list)-> None: #6
    """_summary_
    Realiza la compra de un producto y la guarda en un archivo txt
    Args:
        lista (list): lista a recorrer
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_productos = []
        acum_total = 0
        seguir = 's'
        
        patron_marca = imprimir_patron_marca()
        patron_producto = imprimir_patron_producto()

        while seguir == 's':
            diccionario_producto = {}

            mostrar_marcas(lista)
            marca = ingresar_cadena_valida_con_o_sin_patron("Ingrese marca: ", patron_marca, True)
            mostrar_campos(lista, marca, "marca", "nombre", "precio")
            producto = ingresar_cadena_valida_con_o_sin_patron("Ingrese producto: ", patron_producto, True)
            while not producto_esta_en_la_marca(lista, producto, marca):
                print("El producto seleccionado esta en la lista, pero no coincide con la marca seleccionada")
                print("Reingrese un producto que pertenezca a la marca!")
                producto = ingresar_cadena_valida_con_o_sin_patron("Ingrese producto: ", patron_producto, True)
            acum = acumular_precio_insumos(lista, marca, "marca", producto, "nombre", "precio")
            cantidad = pedir_entero_valido("Ingrese la cantidad de productos: ", "Error, eso no es un numero entero")
            subtotal = acum * cantidad
            subtotal = float(subtotal)
            diccionario_producto = {
                "producto": producto, 
                "cantidad": cantidad, 
                "subtotal": subtotal
            }
            lista_productos.append(diccionario_producto)
            acum_total += subtotal
            print("Compra cargada!")
            seguir = input("Desea seguir ingresando datos: [s/n]")
            while not validar_seguir_opcion(seguir):
                print("dato inválido. Ingrese 's' para continuar o 'n' para salir.")
                seguir = input("Desea seguir ingresando datos: [s/n]")

        if seguir == "n":
                imprimir_dato(f"El total de la compra es: {acum_total}")
                generar_factura_producto_txt("factura_de_compra.txt", lista_productos, "producto", "cantidad", "subtotal", acum_total)

def generar_factura_producto_txt(path: str, lista: list, key_uno: str, key_dos: str, key_tres: str, total: float)-> None:
    """_summary_
    Genera la factura de la compra en un archivo txt
    Args:
        path (str): ruta a guardar el archivo
        lista (list): lista a recorrer
        key_uno (str): campo de la lista
        key_dos (str): campo de la lista
        key_tres (str): campo de la lista
        total (float): el total de la compra
    """
    if type(lista) == type(list()) and len(lista) > 0:
        file = open(path, "a")
        for producto in lista:
            file.write(f"Producto: {producto[key_uno]}\n")
            file.write(f"Cantidad: {producto[key_dos]}\n")
            file.write(f"Subtotal: {producto[key_tres]:.2f}\n")
        file.write(f"TOTAL: {total}\n\n")
        file.close()
        print("Factura generada exitosamente!")

def guardar_en_formato_JSON(path: str, lista: list)-> None: #7
    """_summary_
    Guarda un archivo en formato json
    Args:
        path (str): ruta donde se va a generar el archivo
        lista (list): lista a recorrer
    """
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        guardar_json(path, lista)

def leer_desde_formato_JSON(path: str): #8
    """_summary_
    Se encarga de leer un archivo json
    Args:
        path (str): ruta del archivo a leer
    """
    if type(path) == type(str()):
        print(leer_json(path))

def actualizar_precios(lista: list)-> None: #9
    """_summary_
    Crea una lista de diccionarios igual que el de la original, con el agregado de un 8.4% al campo precio.
    El resultado de esa operacion es un objeto iterable que se castea a list y se guarda en el archivo "insumos_copia.csv

    Args:
        lista (list): lista a recorrer
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista = list(map(lambda insumo: {
        "id": insumo["id"],
        "nombre": insumo["nombre"],
        "marca": insumo["marca"],
        "precio": float(insumo["precio"]) + (float(insumo["precio"]) * 0.084),
        "caracteristicas": insumo["caracteristicas"]
        }, lista))
        guardar_csv("insumos_copia.csv", lista)