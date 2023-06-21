#===========================================|Federico Barone 1-A [Primer_parcial]|=======================================================#
#=======================================Administración de Insumos de una Tienda de Mascotas==============================================#

# Se solicita desarrollar un programa para administrar los insumos de una
# tienda de mascotas. Para ello, se dispone de un archivo CSV con el
# siguiente formato:

# ID,         NOMBRE,           MARCA,     PRECIO,                         CARACTERISTICAS
# 1,   Alimento para perros,  Pedigree,    $12.99,    Sabor delicioso~Nutrición equilibrada~Contiene vitaminas y minerales

# El programa debe ofrecer un menú con las siguientes opciones:

# 1. Cargar datos desde archivo: Esta opción permite cargar el contenido
# del archivo "Insumos.csv" en una colección, teniendo en cuenta que
# las características de los insumos deben estar en un tipo de colección
# integrada.

# 2. Listar cantidad por marca: Muestra todas las marcas y la cantidad
# de insumos correspondientes a cada una.

# 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# precio de los insumos correspondientes.

# 4. Buscar insumo por característica: El usuario ingresa una
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.

# 5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# y la primera característica de todos los productos, ordenados por
# marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# descendente.

# 6. Realizar compras: Permite realizar compras de productos. El usuario
# ingresa una marca y se muestran todos los productos disponibles de
# esa marca. Luego, el usuario elige un producto y la cantidad deseada.
# Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo
# TXT con la factura de la compra, incluyendo cantidad, producto,
# subtotal y el total de la compra.

# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".

# 8. Leer desde formato JSON: Permite mostrar un listado de los insumos
# guardados en el archivo JSON generado en la opción anterior.

# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".

# 10. Salir del programa

# Requerimientos extra
# 1. El programa deberá permitir agregar un nuevo producto a la lista (mediante una
# nueva opción de menú).

# Al momento de ingresar la marca del producto se deberá mostrar por pantalla un
# listado con todas las marcas disponibles. Las mismas serán cargadas al programa
# desde el archivo marcas.txt.

# En cuanto a las características, se podrán agregar un mínimo de una y un máximo
# de 3.

# 2. Agregar una opción para guardar todos los datos actualizados (incluyendo las altas).
# El usuario elegirá el tipo de formato de exportación: csv o json.


# import os
# import re
# from busquedas import buscar_elemento_en_lista
# import json

def leer_csv(path: str)-> list:
    """_summary_
   Lee un archivo csv y crea una lista de diccionarios a partir de los datos del archivo
    Args:
        path (str): ruta del archivo a leer

    Returns:
        list: retorna una lista de diccionarios
    """
    lista = []
    with open(path, 'r', encoding='utf-8') as file:
        file = file.readlines()
        file.pop(0)
        diccionario = {}
        for linea in file:
            linea = linea.replace("\n", "")
            lista_str = linea.split(",")
            diccionario = {
                "id": lista_str[0],
                "nombre": lista_str[1],
                "marca": lista_str[2],
                "precio": lista_str[3].replace("$", ""),
                "caracteristicas": lista_str[4]
            }
            lista.append(diccionario)
    return lista#punto 1


lista_insumos = leer_csv("insumos.csv")#FUNCIONA PERFECTO

# #listar cantidad por marca punto 2
# print("#############################################################################################")
# lista_marcas = []
# for insumo in lista_insumos:
#     lista_marcas.append(insumo["marca"])

# contador = {}
# for marca in lista_marcas:
#     contador[marca] = 0

# for insumo in lista_insumos:
#     contador[insumo["marca"]]+=1

# for marca in contador:
#     contador[marca]
#     print(f"{'Marca'}: " + marca)
#     print(f"{'Cantidad insumos'}: ", contador[marca])
#     print("======================================================")#FUNCIONA PERFECTO
# print("\n")
#lista_filtrada = quitar_repetidos(lista, "marca")
#diccionario = contar_dato(lista_filtrada, lista, "marca")
# #mostrar_contador_dato(diccionario, "Marca", "Cantidad isumos")


# # 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# # precio de los insumos correspondientes.
# marcas = []
# for insumo in lista_insumos:
#     if not insumo["marca"] in marcas:
#         marcas.append(insumo["marca"])

# print("===============================================================================")
# for marca in marcas:
#     print(f"Marca: {marca}")
#     for insumo in lista_insumos:
#         if marca == insumo["marca"]:
#             print(f"{insumo['nombre']} {insumo['precio']}")####### funciona bien
#     print("===============================================================================")#FUNCIONA PERFECTO
#print("\n")

# # # 4. Buscar insumo por característica: El usuario ingresa una
# # # característica (por ejemplo, "Sin Granos") y se listarán todos los
# # # insumos que poseen dicha característica.
# def producto_esta_en_la_marca(lista: list, producto):
#         esta = False
#         for insumo in lista:
#             if producto in insumo["caracteristicas"]:
#                 esta = True
#                 break
#         return esta

# for insumo in lista_insumos:
#     print(insumo["caracteristicas"])
#     print("======================================================================")#FUNCIONA PERFECTO
# print("\n")

# caracteristica = input("Ingrese caracteristica: ")

# while not producto_esta_en_la_marca(lista_insumos, caracteristica):
#     caracteristica = input("Esa caracteristica no esta en la lista: ")

# for insumo in lista_insumos:
#     if caracteristica in insumo["caracteristicas"]:####### funciona bien pero hay modificarle un par de cosas
#         print(insumo["nombre"])


# # 5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# # y la primera característica de todos los productos, ordenados por
# # marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# # descendente.

# tam = len(lista_insumos)
# for i in range(tam - 1):
#     for j in range(i + 1, tam):
#         if lista_insumos[i]["marca"] > lista_insumos[j]["marca"] or (lista_insumos[i]["marca"] == lista_insumos[j]["marca"] and lista_insumos[i]["precio"] < lista_insumos[j]["precio"]):
#             aux = lista_insumos[i]
#             lista_insumos[i] = lista_insumos[j]
#             lista_insumos[j] = aux

# for i in lista_insumos:
#     print(i)####### #FUNCIONA PERFECTO

# 6. Realizar compras: Permite realizar compras de productos. El usuario
# ingresa una marca y se muestran todos los productos disponibles de
# esa marca. Luego, el usuario elige un producto y la cantidad deseada.
# Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo
# TXT con la factura de la compra, incluyendo cantidad, producto,
# subtotal y el total de la compra.

# def producto_esta(lista, producto):
#     flag = False
#     for insumo in lista:
#         if producto == insumo["nombre"]:
#             flag = True
#             break
#     return flag

# id_compra = 0
# try:
#     with open("punto6prueba.txt", "r") as archivo:
#         for linea in archivo:
#             if "ID COMPRA:" in linea:
#                 id_compra = linea.split("ID COMPRA:")[1].strip()
#                 print(id_compra)           
# except FileNotFoundError:
#     print("Debe generar un archivo")

# #==========================================================================================
# marcas = []
# lista_marca_producto = []
# seguir = "s"
# lista_productos = []

# acum_total = 0

# id_compra = int(id_compra)

# while seguir == "s":
#     diccionario = {}
#     acum = 0

#     for insumo in lista_insumos:
#         marcas.append(insumo["marca"])

#     for marca in marcas:
#         print(marca)

#     marca = input("Ingrese marca: ")

#     for insumo in lista_insumos:
#         if marca == insumo["marca"]:
#             print(f"{insumo['nombre']} {insumo['precio']}")

#     producto = input("Ingrese producto: ")

#     while not producto_esta(lista_insumos, producto):
#         producto = input("Ingrese producto de nuevo: ")

#     for insumo in lista_insumos:
#         if marca == insumo["marca"] and producto == insumo["nombre"]:
#             lista_marca_producto.append(insumo)

#     if len(lista_marca_producto) > 1:
#         print("La marca pedigree tiene dos productos con el mismo nombre. Seleccione uno: ")
#         for i in range(len(lista_marca_producto)):
#             producto = lista_marca_producto[i]
#             print(f"{i+1}. {producto['nombre']} - {producto['precio']}")

#         indice_producto_elegido = int(input("Ingrese el número del producto seleccionado: ")) - 1

#         producto_elegido = lista_marca_producto[indice_producto_elegido]

#     elif len(lista_marca_producto) == 1:
#         producto_elegido = lista_marca_producto[0]

#     else:
#         print("No se encontró el producto seleccionado.")

#     acum += float(producto_elegido["precio"])

#     cantidad_producto = int(input("Ingrese cantidad de productos: "))

#     subtotal = acum * cantidad_producto

#     diccionario = {
#         "producto": producto_elegido["nombre"],
#         "cantidad_producto": cantidad_producto,
#         "subtotal": subtotal
#     }

#     lista_productos.append(diccionario)
#     acum_total += subtotal
#     seguir = input("Desea seguir ingresando datos? [s/n]")

#     if seguir == "n":
#         id_compra += 1
#         print(acum_total)

#         with open("punto6prueba.txt", "a") as archivo:
#             archivo.write("===================================================\n")
#             archivo.write(f"ID COMPRA: {id_compra}\n")
#             for producto in lista_productos:
#                 archivo.write("===================================================\n")
#                 archivo.write(f"Producto: {producto['producto']}\n")
#                 archivo.write("===================================================\n")
#                 archivo.write(f"Cantidad: {producto['cantidad_producto']}\n")
#                 archivo.write("===================================================\n")
#                 archivo.write(f"Subtotal: {producto['subtotal']}\n")
#             archivo.write("===================================================\n")
#             archivo.write(f"TOTAL: {str(acum_total)}\n")
#             archivo.write("===================================================\n")


def producto_esta(lista, producto):
    flag = False
    for insumo in lista:
        if producto.lower() in insumo["nombre"].lower():
            flag = True
            break
    return flag


def marca_esta(lista, marca):
    flag = False
    for insumo in lista:
        if marca.lower() in insumo["marca"].lower():
            flag = True
            break
    return flag


def buscar_ultimo_id(lista):
    flag = False
    ultimo_id = None
    for elemento in lista:
        if elemento > ultimo_id or flag == False:
            ultimo_id = elemento
            flag = True
    return ultimo_id

id_compra = 0
try:
    with open("punto6prueba.txt", "r") as archivo:
        for linea in archivo:
            if "ID COMPRA:" in linea:
                id_compra = linea.split("ID COMPRA:")[1].strip()
                print(id_compra)           
except FileNotFoundError:
    print("Debe generar un archivo")

# #==========================================================================================
marcas = []
seguir = "s"
lista_productos = []

acum_total = 0

id_compra = int(id_compra)

while seguir == "s":
    diccionario = {}
    acum = 0

    for insumo in lista_insumos:
        marcas.append(insumo["marca"])

    for marca in marcas:
        print(marca)

    marca = input("Ingrese marca: ").lower()

    while not marca_esta(lista_insumos, marca):
        marca = input("Ingrese marca: ").lower()

    for insumo in lista_insumos:
        if marca.lower() in insumo["marca"].lower():
            print(f"{insumo['nombre']} {insumo['precio']}")

    producto = input("Ingrese producto: ").lower()

    while not producto_esta(lista_insumos, producto):
        producto = input("Ingrese producto de nuevo: ").lower()

#     # ==================================================VERIFICACION ALIMENTO PERRO PEDIGREE========================================
    alimentos_perro_pedigree = []

    for insumo in lista_insumos:
        if marca.lower() in insumo["marca"].lower() and producto.lower() in insumo["nombre"].lower():
            alimentos_perro_pedigree.append(insumo)
    print(alimentos_perro_pedigree)

    if len(alimentos_perro_pedigree) > 1:
        print("La marca pedigree tiene dos productos con el mismo nombre. Seleccione uno: ")
        for i in range(len(alimentos_perro_pedigree)):
            producto = alimentos_perro_pedigree[i]
            print(f"{i+1}. {producto['nombre']} - {producto['precio']}")

        indice_producto_elegido = int(input("Ingrese el número del producto seleccionado: ")) - 1

        producto_elegido = alimentos_perro_pedigree[indice_producto_elegido]

    elif len(alimentos_perro_pedigree) == 1:
        producto_elegido = alimentos_perro_pedigree[0]

    else:
        print("No se encontró el producto seleccionado.")

    acum += float(producto_elegido["precio"])

    # ========================================================================================
    cantidad_producto = int(input("Ingrese cantidad de productos: "))

    subtotal = acum * cantidad_producto

    diccionario = {
        "producto": producto_elegido["nombre"],
        "cantidad_producto": cantidad_producto,
        "subtotal": subtotal
    }

    lista_productos.append(diccionario)
    acum_total += subtotal
    print(lista_productos)
    print(acum_total)
    seguir = input("Desea seguir ingresando datos? [s/n]")

    if seguir == "n":
        id_compra += 1
        print(acum_total)

        with open("punto6prueba.txt", "a") as archivo:
            archivo.write("===================================================\n")
            archivo.write(f"ID COMPRA: {id_compra}\n")
            for producto in lista_productos:
                archivo.write("===================================================\n")
                archivo.write(f"Producto: {producto['producto']}\n")
                archivo.write("===================================================\n")
                archivo.write(f"Cantidad: {producto['cantidad_producto']}\n")
                archivo.write("===================================================\n")
                archivo.write(f"Subtotal: {producto['subtotal']}\n")
            archivo.write("===================================================\n")
            archivo.write(f"TOTAL: {str(acum_total)}\n")
            archivo.write("===================================================\n")



# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".
# with open("ninja.json", "w") as file:
#     for insumo in lista_insumos:
#         insumos = {}
#         lista_alimentos = []
#         if re.match("(Alimento)", insumo["nombre"]):
#             lista_alimentos.append(insumo["nombre"])
#     print("archivo generado!")
#     insumos = {"insumos": lista_alimentos}
#     with open("copia_alimento.json", "w", encoding='utf-8') as file:
#         json.dump(insumos, file, indent = 4)

# alimentos = []
# insumos = {}
# for insumo in lista_insumos:
#     if re.match("(Alimento)", insumo["nombre"]):
#         if not buscar_elemento_en_lista(alimentos, insumo):
#             alimentos.append(insumo)
#             insumos = {"insumos": alimentos}
# with open("copia_alimentos.json", "w") as file:
#     json.dump(insumos, file, indent = 4)

# # 8. Leer desde formato JSON: Permite mostrar un listado de los insumos
# # guardados en el archivo JSON generado en la opción anterior.
# with open("copia_alimentos.json", "r") as file:
#     diccionario = json.load(file)
# print(diccionario)


# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".

# lista = list(map(lambda insumo: {
#     "id": insumo["id"],
#     "nombre": insumo["nombre"],
#     "marca": insumo["marca"],
#     "precio": float(insumo["precio"]) + (float(insumo["precio"]) * 0.084),
#     "caracteristicas": insumo["caracteristicas"]
#     }, lista_insumos))


# with open("insu.csv", 'w', encoding='utf-8') as file:
#     file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
#     for linea in lista:
#         file.write(f"{linea['id']},{linea['nombre']},{linea['marca']},${linea['precio']:.2f},{linea['caracteristicas']}\n")

































# lista_menu_principal = [
#     "1- Cargar datos desde archivo", "2- Listar cantidad por marca", "3- Listar insumos por marca",
#     "4- Buscar insumo por característica", "5- Listar insumos ordenados", "6- Realizar compras",
#     "7- Guardar en formato JSON", "8- Leer desde formato JSON", "9- Actualizar precios", 
#     "10- Agregar nuevo producto a la lista ", "11- Guardar datos actualizados", "12- Salir del programa"
# ]
# cargar_lista = False

# while True:
#     os.system("cls")
#     match mostrar_menu_principal(lista_menu_principal):
#         case '1':
#             lista_archivo = cargar_datos_desde_archivo("insumos.csv")
#             normalizar_datos_numericos(lista_archivo, "precio", "id")
#             cargar_lista = True
#         case '2':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 listar_cantidad_por_marca(lista_archivo)
#         case '3':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 listar_insumos_por_marca(lista_archivo, "marca", "nombre", "precio")
#         case '4':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 buscar_insumo_por_característica("Ingrese una caracteristica: ", lista_archivo)
#         case '5':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 listar_insumos_ordenados(lista_archivo, "marca", "precio")
#         case '6':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 realizar_compras(lista_archivo)
#         case '7':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 guardar_en_formato_JSON("alimentos.json", lista_archivo)
#         case '8':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 leer_desde_formato_JSON("alimentos.json")
#         case '9':
#             if not cargar_lista:
#                 print("Debe cargar el archivo!")
#             else:
#                 actualizar_precios(lista_archivo) 
#         case '10':
#             lista_marcas = cargar_marcas_txt("marcas.txt")
#             lista_productos = agregar_producto(lista_marcas, lista_archivo, "id")
#             lista_archivo.extend(lista_productos)
#         case '11':
#             opcion = input("Ingrese A para expoartar csv o B para json: ")
#             if opcion == 'A':
#                 exportar_a_csv("prueba.csv", lista_archivo)
#             elif opcion == 'B':
#                 exportar_a_json("prueba.json", lista_archivo)
#         case '12':
#             salir = salir_del_menu()
#             if salir == 's':
#                 break

#     os.system("pause")
