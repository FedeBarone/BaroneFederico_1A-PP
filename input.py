import re
#------------------------------------------------------MODULO FUNCIONES DE ENTRADA----------------------------------------------------
def es_solo_texto(string: str)-> bool:#6
    """_summary_
        Valida con regex que el dato pasado por parametro sea unicamente de tipo string y se permiten espacios
    Args:
        string (str): cadena a validar

    Returns:
        bool: true si el dato fue validado, false sino se pudo
    """
    if type(string) == type(str()):
        return_aux = False
        if re.match("^[A-Za-z\s]+$", string):
            return_aux = True
        return return_aux


def es_solo_texto_con_algun_caracter(string: str)-> bool:#6
    """_summary_
        Valida con regex que el dato pasado por parametro sea unicamente de tipo string y se permiten espacios con algun que otro caracter
    Args:
        string (str): cadena a validar

    Returns:
        bool: true si el dato fue validado, false sino se pudo
    """
    if type(string) == type(str()):
        return_aux = False
        if re.match("^[A-Za-z\s]+$|^[A-Za-z\s]+&[A-Za-z\s]+$|^[A-Za-z\s]+!$", string):
            return_aux = True
        return return_aux

def ingresar_cadena_valida(texto: str)-> str:
    """_summary_
        Pide un dato que sea unicamente de tipo string

    Args:
        cadena (str): cadena a validar
        texto (str): mensaje a mostrar cuando se va a ingresar el dato

    Returns:
        _type_(str): retorna la cadena validada al ingreso de texto
    """
    if type(texto) == type(str()):
        while True:
            cadena = input(texto)
            if es_solo_texto(cadena):
                return cadena
            else:
                print("No puede ingresar numeros")#6

def es_entero(string: str)-> bool:
    """_summary_
    Valida con regex que el string que se pasa por parametro sea un numero entero
    Args:
        string (str): string a validar

    Returns:
        bool: true si el dato fue validado, false sino se pudo
    """
    if type(string) == type(str()):
        return_aux = False
        if re.match("^[0-9]+$", string):
            return_aux = True
        return return_aux

def pedir_entero_valido(mensaje, mensaje_error):
    """_summary_
    Pide un entero positivo mayor a 0
    Args:
        entero_string (str): _description_
        mensaje (_type_): _description_
        mensaje_error (_type_): _description_

    Returns:
        _type_: _description_
    """
    if type(mensaje) == type(str()) and type(mensaje_error) == type(str()):
        while True:
            entero_string = input(mensaje)
            if es_entero(entero_string):
                int(entero_string)
                if int(entero_string) > 0:
                    return int(entero_string)
                else:
                    print("No es un numero positivo mayor a 0")
            else:
                print(mensaje_error)

def pedir_entero_valido_con_patron(mensaje, mensaje_error):
    """_summary_
    Pide un entero positivo mayor a 0
    Args:
        entero_string (str): _description_
        mensaje (_type_): _description_
        mensaje_error (_type_): _description_

    Returns:
        _type_: _description_
    """
    if type(mensaje) == type(str()) and type(mensaje_error) == type(str()):
        while True:
            entero_string = input(mensaje)
            if es_entero(entero_string):
                if re.match("^[12]$", entero_string):
                    return int(entero_string)
                else:
                    print("patron incorrecto")
            else:
                print(mensaje_error)

def ingresar_cadena_valida_con_o_sin_patron(mensaje: str, patron: str,
                                            con_patron: bool = True)-> str:
    """_summary_
        Pide un dato que sea unicamente de tipo string y como opcional valida que tenga un patron especifico

    Args:
        cadena (str): cadena a validar
        mensaje (str): mensaje a mostrar cuando se va a ingresar el dato
        patron (str): expresion regular que se encarga de validar un patron especifico
        con_patron (bool, optional): si la variable con_patron es True el dato se valida con patron, sino se deja la validacion comun

    Returns:
        _type_(str): retorna la cadena validada al ingreso de texto, como opcional puede retornar la cadena validada al ingreso de
        solo texto y un patron en especifico
    """
    if type(mensaje) == type(str()) and type(patron) == type(str()) and type(con_patron) == type(bool()):
        while True:
            if con_patron:
                cadena = input(mensaje)
                if es_solo_texto(cadena):
                    if re.match(patron, cadena):
                        return cadena
                    else:
                        print("Ese dato no esta en la lista")
                else:
                    print("No puede ingresar numeros")#6
            else:
                cadena = input(mensaje)
                if es_solo_texto(cadena):
                    return cadena
                else:
                    print("No puede ingresar numeros")#6

def ingresar_cadena_valida_con_o_sin_patron_dos(mensaje: str, patron: str,
                                            con_patron: bool = True)-> str:
    """_summary_
        Pide un dato que sea unicamente de tipo string y como opcional valida que tenga un patron especifico

    Args:
        cadena (str): cadena a validar
        mensaje (str): mensaje a mostrar cuando se va a ingresar el dato
        patron (str): expresion regular que se encarga de validar un patron especifico
        con_patron (bool, optional): si la variable con_patron es True el dato se valida con patron, sino se deja la validacion comun

    Returns:
        _type_(str): retorna la cadena validada al ingreso de texto, como opcional puede retornar la cadena validada al ingreso de
        solo texto y un patron en especifico
    """
    if type(mensaje) == type(str()) and type(patron) == type(str()) and type(con_patron) == type(bool()):
        while True:
            if con_patron:
                cadena = input(mensaje)
                if es_solo_texto_con_algun_caracter(cadena):
                    if re.match(patron, cadena):
                        return cadena
                    else:
                        print("Ese dato no esta en la lista")
                else:
                    print("No puede ingresar numeros")#6
            else:
                cadena = input(mensaje)
                if es_solo_texto(cadena):
                    return cadena
                else:
                    print("No puede ingresar numeros")#6
    
def validar_seguir_opcion(opcion: str)-> str:
    """_summary_
    Valida que la opcion de un bucle while sea s o n
    Args:
        opcion (str): la opcion de seguir

    Returns:
        str: el patron que se debe cumplir
    """
    if type(opcion) == type(str()):
        patron = re.match("^[sn]$", opcion)
        return patron
