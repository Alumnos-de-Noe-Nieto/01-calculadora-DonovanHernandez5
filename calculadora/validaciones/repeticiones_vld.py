"""
Nivel 3: Validación de repeticiones V/L/D.

Los símbolos V, L y D NO pueden repetirse.
Ejemplos válidos: V, L, D, MCMXCIV
Ejemplos inválidos: VV, LL, DD
"""

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
    return True
    raise NotImplementedError()
