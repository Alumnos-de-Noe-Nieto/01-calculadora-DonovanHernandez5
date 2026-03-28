"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""

def validar_orden_descendente(cadena: str) -> bool:
    VALORES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    
    i = 0
    while i < len(cadena) - 1:
        # Extraemos el par actual para ver si es una sustracción
        par = cadena[i : i+2]
        
        if par in SUSTRACCIONES_VALIDAS:
            # PISTA: Verifica que no haya repeticiones antes (ej: IIV)
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            
            # Aqui se verifica que después de la sustracción se continua correctamente
            # Comparamos el valor del símbolo restado  con el siguiente valor si existe
            if i + 2 < len(cadena):
                if VALORES[cadena[i+1]] <= VALORES[cadena[i+2]]:
                    return False
            
            # Se avanzan dos posiciones porque es par
            i += 2
        else:
            if VALORES[cadena[i]] < VALORES[cadena[i+1]]:
                return False
            i += 1
            
    return True
    raise NotImplementedError()
