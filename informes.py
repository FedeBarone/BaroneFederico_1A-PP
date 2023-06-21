from insumos import *
from input import*
from calculos import*
from ordenamientos import*
import re
#======================================================MODULO DE INFORMES================================================================
#=========================================================INFORME-1======================================================================
def cargar_datos_desde_archivo(path: str)-> list:
    """_summary_
    Carga los datos del archivo insumos csv

    Args:
        path (str): ruta del archivo a leer

    Returns:
        list: devuelve una lista de diccionarios
    """
    print("Archivo cargado correctamente!")
    return leer_csv(path)
#=========================================================INFORME-2======================================================================
def listar_cantidad_por_marca(lista: str):
    """_summary_
    Muestra la cantidad de insumos que tiene cada marca
    Args:
        lista (str): lista a recorrer
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_filtrada = quitar_repetidos(lista, "marca")
        diccionario = contar_dato(lista_filtrada, lista, "marca")
        mostrar_contador_dato(diccionario, "Marca", "Cantidad isumos")
#=========================================================INFORME-3======================================================================
def listar_insumos_por_marca(lista: list, key_uno: str, key_dos: str, key_tres: str)-> None:
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
#=========================================================INFORME-4======================================================================
def buscar_insumo_por_característica(texto: str, lista: str)-> None:
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
#=========================================================INFORME-5======================================================================
def listar_insumos_ordenados(lista: list, key_uno: str, key_dos: str):
    """_summary_
    Ordena los insumos por doble criterio ,la marca de forma ascendente y, ante marcas iguales, por precio descendente. Y muestra los
    insumos con todos sus datos
    Args:
        lista (list): lista a recorrer
        key_uno (str): campo a comparar
        key_dos (str): campo a comparar
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(key_uno) == type(str()) and type(key_dos) == type(str()):
        ordenar_lista_dict_dos(lista, key_uno, key_dos)
        mostrar_insumos(lista)
#=========================================================INFORME-6======================================================================
def realizar_compras(lista: list)-> None:
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
        id_compra = 0

        try:
            with open("factura_de_compra.txt", "r") as archivo:
                for linea in archivo:
                    if "ID COMPRA:" in linea:
                        id_compra = linea.split("ID COMPRA:")[1].strip()
                        print(id_compra)           
        except FileNotFoundError:
            print("Debe generar un archivo")
        
        id_compra = int(id_compra)

        while seguir == 's':
            diccionario_producto = {}
            acum_parcial = 0

            mostrar_marcas(lista)
            marca = ingresar_cadena_valida_con_o_sin_patron_dos("Ingrese marca: ", patron_marca, True)
            mostrar_campos(lista, marca, "marca", "nombre", "precio")
            producto = ingresar_cadena_valida_con_o_sin_patron("Ingrese producto: ", patron_producto, True)
            while not producto_esta_en_la_marca(lista, producto, marca):
                print("El producto seleccionado esta en la lista, pero no coincide con la marca seleccionada")
                print("Reingrese un producto que pertenezca a la marca!")
                producto = ingresar_cadena_valida_con_o_sin_patron("Ingrese producto: ", patron_producto, True)
    
            lista_ingreso_productos = filtrar_insumos_por_marca_y_producto(lista_insumos, marca, producto)

            if len(lista_ingreso_productos) > 1:
                print("La marca seleccionada tiene dos productos con el mismo nombre. Debe elegir uno: ")
                
                imprimir_lista_ingreso_productos(lista_ingreso_productos, "nombre", "precio")

                indice_producto_elegido = pedir_entero_valido_con_patron("Ingrese el número del producto seleccionado: ", 
                                                                        "eso no es un numero")- 1

                producto_elegido = lista_ingreso_productos[indice_producto_elegido]

            elif len(lista_ingreso_productos) == 1:
                producto_elegido = lista_ingreso_productos[0]

            else:
                print("Error...")

            acum_parcial += float(producto_elegido["precio"])

            cantidad = pedir_entero_valido("Ingrese la cantidad de productos: ", "Error, eso no es un numero entero")
            subtotal = acum_parcial * cantidad
            subtotal = float(subtotal)
            diccionario_producto = {
                "producto": producto_elegido["nombre"], 
                "cantidad": cantidad, 
                "subtotal": subtotal
            }
            lista_productos.append(diccionario_producto)
            acum_total += subtotal
            print("Producto cargado!")
            seguir = input("Desea seguir ingresando datos: [s/n]")
            while not validar_seguir_opcion(seguir):
                print("dato invalido. Ingrese 's' para continuar o 'n' para salir.")
                seguir = input("Desea seguir ingresando datos: [s/n]")

        if seguir == "n":
                id_compra += 1
                imprimir_dato(f"El total de la compra es: {acum_total}")
                generar_factura_producto_txt("factura_de_compra.txt", lista_productos, "producto", "cantidad", "subtotal", acum_total, 
                                            id_compra)

def generar_factura_producto_txt(path: str, lista: list, key_uno: str, key_dos: str, key_tres: str, total: float, id_compra: int)-> None:
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
        with open(path, "a") as archivo:
                archivo.write("===================================================\n")
                archivo.write(f"ID COMPRA: {id_compra}\n")
                for producto in lista:
                    archivo.write("===================================================\n")
                    archivo.write(f"Producto: {producto[key_uno]}\n")
                    archivo.write("===================================================\n")
                    archivo.write(f"Cantidad: {producto[key_dos]}\n")
                    archivo.write("===================================================\n")
                    archivo.write(f"Subtotal: {producto[key_tres]:.2f}\n")
                archivo.write("===================================================\n")
                archivo.write(f"TOTAL: {total:.2f}\n")
                archivo.write("===================================================\n")
                print("Factura generada exitosamente!")
#=========================================================INFORME-7======================================================================
def guardar_en_formato_JSON(path: str, lista: list)-> None: #7
    """_summary_
    Guarda un archivo en formato json
    Args:
        path (str): ruta donde se va a generar el archivo
        lista (list): lista a recorrer
    """
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        guardar_json(path, lista)
#=========================================================INFORME-8======================================================================
def leer_desde_formato_JSON(path: str): #8
    """_summary_
    Se encarga de leer un archivo json
    Args:
        path (str): ruta del archivo a leer
    """
    if type(path) == type(str()):
        try:
            print(leer_json(path))
        except UnboundLocalError:
            pass
#=========================================================INFORME-9======================================================================
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
#=========================================================INFORME-10(EXTRA)===============================================================
def agregar_producto(lista_i: list)-> list:
    """_summary_
    Agrega un producto a una lista de diccionarios

    Args:
        lista (str): lista a recorrer

    Returns:
        list: devuelve la lista con los productos agregados
    """
    if type(list) == type(list) and len(lista_i) > 0:
        try:
            with open("prueba.json", "r", encoding='utf-8') as file:
                insumos = json.load(file)
                lista_i = insumos["insumos"]
        except FileNotFoundError:
            lista_i = leer_csv("insumos.csv")
            normalizar_datos_numericos(lista_i, "precio", "id")
        
        lista_marcas = cargar_marcas_txt("marcas.txt")

        seguir = 's'
        next_id = buscar_mayor_id(lista_i, "id")+ 1 
        lista_producto = []

        while seguir == 's':
            diccionario_producto = {}
            mostrar_elementos(lista_marcas)
            marca_ingreso = ingresar_cadena_valida_con_o_sin_patron("Ingrese marca: ", "", False)
            while not buscar_elemento_en_lista(lista_marcas, marca_ingreso):
                    print("Esa marca no esta en la lista!")
                    marca_ingreso = input("Reingrese marca: ")

            caracteristica = ingresar_letras_numeros("Ingrese caracteristica", "Error...")

            nombre_producto = ingresar_cadena_valida("Ingrese el nombre del producto: ", "Error...")

            precio = pedir_flotante_valido("Ingrese el precio del prdoucto: ", "Error...")

            diccionario_producto = {
                                "id": next_id,
                                "nombre": nombre_producto,
                                "marca": marca_ingreso,
                                "precio": precio,
                                "caracteristicas": caracteristica   
            }
            lista_producto.append(diccionario_producto)
            next_id = next_id + 1
            seguir = input("\nDesea seguir ingresando?][s/n]")
            while not validar_seguir_opcion(seguir):
                print("dato invalido. Ingrese 's' para continuar o 'n' para salir.")
                seguir = input("\nDesea seguir ingresando?][s/n]")
    return lista_producto
#=========================================================INFORME-11(EXTRA)===============================================================
def exportar_a_csv(path: str, lista: list)-> None:
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        print("archivo generado!")
        with open(path, 'w', encoding='utf-8') as file:
            file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
            for linea in lista:
                file.write(f"{linea['id']},{linea['nombre']},{linea['marca']},${linea['precio']:.2f},{linea['caracteristicas']}\n")

def exportar_a_json(path: str, lista: list)-> None:
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        print("archivo generado!")
        insumos = {"insumos": lista}
        with open(path, "w", encoding='utf-8') as file:
            json.dump(insumos, file, indent = 4)