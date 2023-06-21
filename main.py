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

# Requerimientos extra
# 10. El programa deberá permitir agregar un nuevo producto a la lista (mediante una
# nueva opción de menú).

# Al momento de ingresar la marca del producto se deberá mostrar por pantalla un
# listado con todas las marcas disponibles. Las mismas serán cargadas al programa
# desde

# 11. Agregar una opción para guardar todos los datos actualizados (incluyendo las altas).
# El usuario elegirá el tipo de formato de exportación: csv o json.

# 12. Salir del programa



import os
from output import *
from informes import *
from insumos import *

lista_menu_principal = [
    "1- Cargar datos desde archivo", "2- Listar cantidad por marca", "3- Listar insumos por marca",
    "4- Buscar insumo por característica", "5- Listar insumos ordenados", "6- Realizar compras",
    "7- Guardar en formato JSON", "8- Leer desde formato JSON", "9- Actualizar precios", 
    "10- Agregar nuevo producto a la lista ", "11- Guardar datos actualizados", "12- Salir del programa"
]
cargar_lista = False
flag_lista_producto = False

while True:
    os.system("cls")
    match mostrar_menu_principal(lista_menu_principal):
        case '1':
            if cargar_lista:
                print("Ya se ha cargado el archivo csv")
            else:
                lista_archivo = cargar_datos_desde_archivo("insumos.csv")
                normalizar_datos_numericos(lista_archivo, "precio", "id")
            cargar_lista = True
        case '2':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    listar_cantidad_por_marca(lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")    
        case '3':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    listar_insumos_por_marca(lista_archivo, "marca", "nombre", "precio")
                except NameError:
                    print("Cargue el archivo por favor")
        case '4':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    buscar_insumo_por_característica("Ingrese una caracteristica: ", lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")
        case '5':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    listar_insumos_ordenados(lista_archivo, "marca", "precio")
                except NameError:
                    print("Cargue el archivo por favor")
        case '6':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    realizar_compras(lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")
        case '7':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    guardar_en_formato_JSON("alimentos.json", lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")
        case '8':
                leer_desde_formato_JSON("alimentos.json")
        case '9':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    actualizar_precios(lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")
        case '10':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                try:
                    lista_producto = agregar_producto(lista_archivo)
                    lista_archivo.extend(lista_producto)
                    flag_lista_producto = True
                except NameError:
                    print("Cargue el archivo por favor")
        case '11':
            if not cargar_lista:
                if not flag_lista_producto:
                    print("Debe cargar el archivo o agregar un producto para exportar!")
            else:
                try:
                    opcion = input("Ingrese 'a' para exportar CSV o 'b' para exportar JSON: ")
                    while not re.match("^[ab]$", opcion):
                        print("Opcion invalida. Por favor, ingrese 'a' o 'b'.")
                        opcion = input("Ingrese 'a' para exportar CSV o 'b' para exportar JSON: ")
                    if opcion == 'a':
                        exportar_a_csv("prueba.csv", lista_archivo)
                    elif opcion == 'b':
                        exportar_a_json("prueba.json", lista_archivo)
                except NameError:
                    print("Cargue el archivo por favor")
        case '12':
            salir = salir_del_menu()
            if salir == 's':
                break

    os.system("pause")
