import json
import os
import re
from busquedas import*
from output import*
from input import*
import random
#------------------------------------------------------MODULO FUNCIONES DE INSUMOS-------------------------------------------------------
def normalizar_datos_numericos(lista: list, key: str, key_dos: str)-> list:
    """_summary_
    Recorre una lista y convierte al tipo de dato correcto las keys que representan datos numéricos

    Args:
        lista (list): lista a recorrer
    """
    if len(lista) > 0:
        normalizado = False
        for elemento in lista:
            if not(type(elemento[key]) == type(float())) or type(elemento[key_dos]) == type(int()):
                elemento[key] = float(elemento[key])
                elemento[key_dos] = int(elemento[key_dos])
                normalizado = True
        if normalizado:
            print("Normalizado!")
        else:
            print("No normalizado!")
    else:
        print("La lista esta vacia")


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

    return lista

def mostrar_insumo(insumo: dict):
    """_summary_
    Muestra el valor de los campos de un insumo
    Args:
        insumo (dict): diccionario que contiene todas las keys
    """
    print(f"|{int(insumo['id']):<2d}| {insumo['nombre']:^32s}| {insumo['marca']:^23s}| {float(insumo['precio']):^6.2f}| {insumo['caracteristicas']:^89s}|")

def mostrar_marca(insumo: dict):
    """_summary_
    Muestra el valor del campo 'marca'

    Args:
        insumo (dict): diccionario de insumos
    """
    print(f"Marca: {insumo['marca']}")

def mostrar_insumos(lista: list):
    """_summary_
    Muestra todos los insumos
    Args:
        lista (list): _description_
    """
    print("+================================================================================================================================================================+")
    print("|ID              NOMBRE                        MARCA           PRECIO                               CARACTERISTICAS                                              |")
    print("+================================================================================================================================================================+")
    for i in range(len(lista)):
        mostrar_insumo(lista[i])
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def imprimir_lista_ingreso_productos(lista: list, key_uno: str, key_dos: str):
    for i in range(len(lista)):
        print("===============================")
        producto = lista[i]
        print(f"|{i+1}| {producto[key_uno]} {producto[key_dos]}")
        print("===============================")

def producto_esta_en_la_marca(lista: list, producto: str, marca: str):
    """_summary_
    Verifica que un producto pertenezca a la marca y no que simplemente este en la lista
    Args:
        lista (list): lista a recorrer
        producto (str): producto a verificar si pertenece
        marca (str): marca a verificar si pertenece

    Returns:
        _type_: true si el producto pertenece a la marca o falso sino pertence
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(producto) == type(str()) and type(marca) == type(str()):
        esta = False
        for insumo in lista:
            if insumo["nombre"] == producto and insumo["marca"] == marca:
                esta = True
                break
        return esta
    
def filtrar_insumos_por_marca_y_producto(lista_insumos, marca, producto):
    lista_ingreso_productos = []
    for insumo in lista_insumos:
        if marca == insumo["marca"] and producto == insumo["nombre"]:
            lista_ingreso_productos.append(insumo)
    return lista_ingreso_productos


def mostrar_marcas(lista: list):
    """_summary_
    Muestra todos los valores del campo 'marca' sin repe
    Args:
        lista (list): lista a recorrer
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_sin_repe = set(map(lambda marca: marca["marca"], lista))
        for elemento in lista_sin_repe:
            print(elemento)

def guardar_json(path: str, lista: list)-> None:#BIEN
    """_summary_
        Guarda en un archivo json los insumos que contienen la palabra "alimento"
    Args:
        path (str): nombre de la ruta en donde se va a generar el archivo
        lista (list): lista a recorrer
    """
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        print("archivo generado!")
        alimentos = []
        insumos = {}
        for insumo in lista:
            if re.match("(Alimento)", insumo["nombre"]):
                if not buscar_elemento_en_lista(alimentos, insumo):
                    alimentos.append(insumo)
                    insumos = {"insumos": alimentos}
        with open(path, "w") as file:
            json.dump(insumos, file, indent = 4)

def leer_json(path: str)-> dict:# BIEN
    """_summary_
    lee un archivo json con los productos que contiene la palabra "Alimento"
    Args:
        path (str): nombre de la ruta del archivo a leer

    Returns:
        dict: retorna el diccionario con los productos 
    """
    if type(path) == type(str()):
        try:
            with open(path, "r") as file:
                dicciconario = json.load(file)
                print("archivo leido!")
        except FileNotFoundError:
                    print("No hay ningun archivo para leer")
    return dicciconario

def guardar_csv(path: str, lista: list):#9  BIEN
    """_summary_
    Guarda y actualiza los valores del campo precio en el archivo "insumos.csv" con un aumento del 8.4%
    Args:
        path (str): ruta del archivo "insumos_copia.csv"
        lista (list): lista a recorrer
    """
    if type(path) == type(str()) and type(lista) == type(list()) and len(lista) > 0:
        print("archivo generado!")
        with open(path, 'w', encoding='utf-8') as file:
            file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
            for linea in lista:
                file.write(f"{linea['id']},{linea['nombre']},{linea['marca']},${linea['precio']:.2f},{linea['caracteristicas']}\n")

def imprimir_patron_caracteristicas() -> str:#BIEN
    #Muestra el patron para que solo se pueden ingresar estas caracteristicas y retorna el patron
    patron_caracteristicas = """^Sabor delicioso$|^Nutricion equilibrada$|^Contiene vitaminas y minerales$|^Alta calidad$|
                                |^Proteinas de primera$|^Promueve un pelaje saludable$|^Duradero$|^Ideal para masticadores agresivos$|
                                |^Control de olores$|^Facil de limpiar$|^Extensible$|^Mango ergonomico$|^Cinta reflectante$|
                                |^Material suave$|^Lavable a maquina$|^Comoda y acogedora$|^Juguete interactivo$|^Movimientos impredecibles$|
                                |^Mantiene a los gatos activos$|^10 galones$|^Filtro incorporado$|^Ideal para peces tropicales$|
                                |^Ingredientes naturales$|^Alta digestibilidad$|^Para todas las etapas de vida$|^Control de tirones$|
                                |^Ajustable$|^Comoda para el perro y el dueño$|^Formula equilibrada$|^Control de peso$|
                                |^Promueve la salud urinaria$|^Disenio elegante$|^Material duradero$|^Facil de limpiar$|
                                |^Resistente a la masticacion$|^Ayuda a la higiene dental $|^Sistema todo en uno$|^Bandeja removible$|
                                |^Facil de mantener$|^Ingredientes naturales$|^Sin granos$|^Para razas pequenias$|
                                |^Aprobada por aerolineas$|^Comoda y segura$|^Ventilacion adecuada $|^Juguete interactivo$|
                                |^Atrae la atencion de los gatos$|^Horas de diversion$|^Proteinas de calidad$|
                                |^Facil eliminacion de desechos$|^Practico y conveniente $|^Resistente al agua$|
                                |^Ideal para actividades al aire libre$|^Comoda para el perro y el duenio$|^Elevada$|^Duradera$|
                                |^Facil de limpiar$|^Ingredientes naturales$|^Promueve la salud digestiva$|^Resistente$|
                                |^Ideal para juegos de lanzamiento $|^Plegable$|^Facil de transportar$|^Espacioso$|
                                |^Ingredientes de calidad$|^Sin conservantes artificiales$|^Salud digestiva$|
                                |^Area de juego y descanso$|^Poste para rascar$|^Incluye juguetes colgantes $|
                                |^Dispensador de alimentos$|^Mantiene a los perros entretenidos$|^Antideslizante$|
                                |^Facil de limpiar$|^Duradero$|^Formula especifica para razas$|^Salud digestiva$|^Pelo brillante$|
                                |^Ajustable$|^Cierre de seguridad$|^Disenio atractivo$|^Comodo$|^Control de tirones$|
                                |^Salud optima$|^Rellenable con catnip$|^Estimula el instinto de caza$|
                                |^Capacidad de 1 galon$|^Mantiene el agua fresca $|^Elimina nudos y pelo suelto$|
                                |^Ideal para perros de pelo largo$|^Texturas variadas$|^Estimula el juego activo$|^Suave y seguro$|
                                |^Elimina el pelo muerto$|^Promueve un pelaje saludable$|^Ecologica$|^Sin polvo$|
                                |^Control de olores eficiente$|^Disenio moderno$|^Comoda y ajustable$|^Ideal para climas frios$|
                                |^Variedad de sabores$|^Alta calidad nutricional$|^Para peces tropicales$|
                                |^Aprobada por aerolineas$|^Puerta con cierre seguro$|^Ventilacion adecuada$|
                                |^Incluye bola y rascador$|^Estimula el juego y el rascado$|^Remueve el pelo suelto$|
                                |^Facil de limpiar$|^Para pelo corto o largo$|^Resistente a la masticacion$|
                                |^Promueve la salud dental$|^Diversion duradera$|^Ingredientes de calidad$|
                                |^Promueve una digestion saludable$|^Reflectante$|^Mango acolchado$|^Resistente y duradera$|
                                |^Material suave y calido$|^Disenio compacto$|^Ideal para espacios pequenios$|
                                |^Resistente$|^Libre de BPA$|^Ideal para juegos de buscar$|^Facil acceso$|^Borde alto$|
                                |^Facil de limpiar$|^Alta proteina$|^Ingredientes naturales$|^Salud digestiva$"""
    return patron_caracteristicas


def imprimir_patron_marca()-> str:#BIEN
    #Muestra el patron para que solo se pueden ingresar estas marcas y retorna el patron
    patron_marca = """^Pedigree$|^Purina ONE$|^Kong$|^Arm & Hammer$|^Flexi$|^Aspen Pet$|^Frolicat$|^Tetra$|^Pro Plan$|^Halti$|
                    |^Science Diet$|^PetFusion$|^Nylabone$|^Purina Tidy Cats$|^Blue Buffalo$|^Sherpa$|^Cat Dancer$|^Iams$|^Litter Genie$|
                    |^Ruffwear$|^Kuranda$|^Wellness$|^Chuckit!$|^MidWest Homes for Pets$|^Nutro$|^GoPetClub$|^Kong Wobbler$|^Bergan$|
                    |^Royal Canin$|^Coastal$|^Rabbitgoo$|^Temperament Pet$|^Gravity Waterer$|^Safari$|^Outward Hound$|^Hertzko$|^Pet Life$|
                    |^AmazonBasics$|^Bergan Turbo Scratcher$|^Nylabone Dura$|^Merrick$|^Max and Neo$|^Frisco$|^West Paw Design$|^Petmate$|
                    |^Wellness CORE$"""
    return patron_marca


def imprimir_patron_producto()-> str:#BIEN
    #Muestra el patron para que solo se pueden ingresar estos productos y retorna el patron
    patron_producto = """^Alimento para perros$|^Alimento para gatos$|^Juguete para perros$|^Arenero para gatos$|^Correa para perros$|
                    |^Cama para perros$|^Juguete para gatos$|^Acuario$|^Cama para gatos$|^Transportadora para gatos$|^Corral para mascotas$|
                    |^Rascador para gatos$|^Juguete interactivo para perros$|^Comedero para mascotas$|^Collar para perros$|
                    |^Arnes para perros$|^Bebedero para mascotas$|^Peine para perros$|^Cepillo para gatos$|^Arena para gatos$|
                    |^Ropa para perros$|^Alimento para peces$|^Transportadora para perros$|^Cepillo para perros$"""
    return patron_producto

def buscar_mayor_id(lista: list, key: str):
    primer_id = lista[0]
    mayor_id = int(primer_id[key])
    for elemento in lista:
        elemento = int(elemento[key])
        if elemento > mayor_id:
            mayor_id = elemento
    return mayor_id

def cargar_marcas_txt(path: str)-> list:
    """_summary_
    Carga las marcas del archivo txt
    Args:
        path (str): ruta de donde se leera el archivo

    Returns:
        _type_: retorna una lista con las marcas del archivo
    """
    marcas = []
    if type(path) == type(str()):
        with open(path, 'r') as file:
            for linea in file:
                linea = linea.replace("\n", "")
                marcas.append(linea)
    return marcas

lista_marcas = cargar_marcas_txt("marcas.txt")

def mostrar_elemento(elemento: str)-> None:
    """_summary_
    Muestra un elemento de una lista

    Args:
        elemento (str): elemento a mostrar
    """
    print(f"{elemento}")

def mostrar_elementos(lista: list)-> None:
    """_summary_
    Muestra todos los elementos de una lista

    Args:
        lista (list): lista a recorrer para mostrar cada elemento que contiene
    """
    for elemento in lista:
        mostrar_elemento(elemento)



# Recuperatorio Laboratorio

# A. Al momento de cargar los datos desde el archivo CSV (en la opción 1 del
# menú), el programa deberá calcular el stock disponible de cada insumo. Para
# ello deberán crear por cada uno, un valor aleatorio entre 0 y 10. Utilizar la ####LISTO
# función map.

# B. Realizar las modificaciones necesarias para que al momento de realizar una
# venta de productos, la misma esté condicionada por el stock disponible, si no
# hay stock disponible el programa debe informarle al usuario y sugerir que
# compre menos cantidad, en caso de que el stock sea superior a cero.

# C. Agregar opción stock por marca: Pedirle al usuario una marca y
# mostrar el stock total de los productos de esa marca.

# D. Agregar opción imprimir bajo stock. Que imprima en un archivo de
# texto en formato csv. Un listado con el nombre de producto y el stock de
# aquellos productos que tengan 2 o menos unidades de stock.

lista_insumos = leer_csv("insumos.csv")

def actualizar_stock(insumo):#A
    insumo['stock'] = random.randint(0, 10)#A
    return insumo#A

lista_mapeada_stock = list(map(actualizar_stock, lista_insumos))#A
print(lista_mapeada_stock)

def realizar_venta(nombre_producto, cantidad):
    insumo = None
    for producto in lista_mapeada_stock:
        if producto['nombre'] == nombre_producto:
            insumo = producto
            break

    if insumo:
        if insumo['stock'] >= cantidad:
            insumo['stock'] -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {insumo['nombre']}")
        else:
            print(f"No hay suficiente stock de {insumo['nombre']} disponible: {insumo['stock']}")
            if insumo['stock'] < cantidad:
                sugerencia = insumo['stock']
            else:
                sugerencia = cantidad

            print(f"Sugerencia: va a comprar{sugerencia} unidades o menos.")
    else:
        print("El producto ingresado no se encuentra en la lista de insumos.")




def mostrar_insumos_lista_mapeada(lista):
    for insumo in lista_mapeada_stock:
        print(insumo["nombre"])



def mostrar_stock_por_marca(lista, marca):
    acum_total = 0
    for insumo in lista:
        if insumo['marca'] == marca:
            acum_total += insumo['stock']
    print(f"stock total de productos de la marca {marca}: {acum_total}")

def imprimir_bajo_stock(lista):
    insumos_bajo_stock = []
    for insumo in lista:
        if insumo['stock'] <= 2:
            insumos_bajo_stock.append(insumo)
    with open('bajo_stock.csv', 'w', encoding='utf-8') as file:
        file.write("NOMBRE, STOCK\n")
        for insumo in insumos_bajo_stock:
            file.write(f"{insumo['nombre']},{insumo['stock']}\n")

def esta_en(lista: list, marca: str, key):
    if type(lista) == type(list()) and len(lista) > 0 and type(marca) == type(str()):
        esta = False
        for insumo in lista:
            if insumo[key] == marca:
                esta = True
                break
        return esta
    

