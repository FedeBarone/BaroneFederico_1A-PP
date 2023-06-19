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

while True:
    os.system("cls")
    match mostrar_menu_principal(lista_menu_principal):
        case '1':
            lista_archivo = cargar_datos_desde_archivo("insumos.csv")
            normalizar_datos_numericos(lista_archivo, "precio", "id")
            cargar_lista = True
        case '2':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                listar_cantidad_por_marca(lista_archivo)
        case '3':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                listar_insumos_por_marca(lista_archivo, "marca", "nombre", "precio")
        case '4':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                buscar_insumo_por_característica("Ingrese una caracteristica: ", lista_archivo)
        case '5':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                listar_insumos_ordenados(lista_archivo, "marca", "precio")
        case '6':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                realizar_compras(lista_archivo)
        case '7':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                guardar_en_formato_JSON("alimentos.json", lista_archivo)
        case '8':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                leer_desde_formato_JSON("alimentos.json")
        case '9':
            if not cargar_lista:
                print("Debe cargar el archivo!")
            else:
                actualizar_precios(lista_archivo) 
        case '10':
            lista_marcas = cargar_marcas_txt("marcas.txt")
            lista_productos = agregar_producto(lista_marcas, lista_archivo, "id")
            lista_archivo.extend(lista_productos)
        case '11':
            opcion = input("Ingrese A para expoartar csv o B para json: ")
            if opcion == 'A':
                exportar_a_csv("prueba.csv", lista_archivo)
            elif opcion == 'B':
                exportar_a_json("prueba.json", lista_archivo)
        case '12':
            salir = salir_del_menu()
            if salir == 's':
                break

    os.system("pause")
