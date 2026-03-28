"""
Nivel 2: Validación de repeticiones I/X/C/M.

Los símbolos I, X, C y M pueden repetirse hasta 3 veces consecutivas.
Ejemplos válidos: III, XXX, CCC, MMM
Ejemplos inválidos: IIII, XXXX, CCCC, MMMM
"""

def validar_repeticiones_icxm(cadena: str) -> bool:
    # Definimos la lista de patrones inválidos 
    # Si cualquiera de estos existe, la cadena es incorrecta.
    patrones_invalidos = ["IIII", "XXXX", "CCCC", "MMMM"]

    # Recorremos cada patrón y verificamos si esta en la cadena
    for patron in patrones_invalidos:
        if patron in cadena:
            # Si encontramos el patrón, retornamos False inmediatamente
            return False
    # 3. Si terminamos de revisar y ninguno estaba presente, es válida
    return True
    raise NotImplementedError()
