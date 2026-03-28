# NIVEL 2: VALIDACION DE REPETICIONES#

def validar_repeticiones_icxm(cadena: str) -> bool:
    # Definimos la lista de patrones inválidos
    # Si cualquiera de estos existe, la cadena es incorrecta.
    patrones_invalidos = ["IIII", "XXXX", "CCCC", "MMMM"]
    # Recorremos cada patrón y verificamos si esta en la cadena
    for patron in patrones_invalidos:
        if patron in cadena:
            # Si encontramos el patrón, retornamos False inmediatamente
            return False
    # Si terminamos de revisar y ninguno estaba presente, es válida
    return all(patron not in cadena for patron in patrones_invalidos)
    raise NotImplementedError()
