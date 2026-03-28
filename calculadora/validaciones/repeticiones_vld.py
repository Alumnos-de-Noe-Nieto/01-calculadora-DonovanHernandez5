# NIVEL 3: VALIDACION DE REPETICION2#
def validar_repeticiones_vld(cadena: str) -> bool:
    # Definimos los patrones no repetibles
    # Estos símbolos son únicos en cualquier número romano válido.
    patrones_prohibidos = ["VV", "LL", "DD"]
    # Verificamos la existencia de estos patrones en la cadena
    for patron in patrones_prohibidos:
        if patron in cadena:
            # Si se encuentra una repetición, la cadena es inválida
            return False
    # Retorna si no se encontro ninguna repeticion
    return all(patron not in cadena for patron in patrones_prohibidos)
    raise NotImplementedError()
