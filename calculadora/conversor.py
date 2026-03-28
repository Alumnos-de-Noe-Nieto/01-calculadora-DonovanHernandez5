"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("La cadena contiene símbolos inválidos")
    # Limpiar cadena para las sig validaciones
    cadena = cadena.strip()
    
    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("Error de repetición en símbolos I/X/C/M")
    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("Error de repetición en símbolos V/L/D")
    if not validar_restas(cadena):
        raise ExpresionInvalida("La expresión contiene restas inválidas")
    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("El orden de los símbolos es incorrecto")
    # Convertir de romano a decimal
    VALORES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(cadena)):
        valor_actual = VALORES[cadena[i]] 
        # Si no es el último carácter y el valor actual es MENOR al siguiente, RESTAMOS
        if i + 1 < len(cadena) and valor_actual < VALORES[cadena[i+1]]:
            total -= valor_actual
        else:
            # En cualquier otro caso (es el último o es mayor/igual), SUMAMOS
            total += valor_actual     
    return total
    raise NotImplementedError()
