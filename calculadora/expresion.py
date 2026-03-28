"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    # Llama a parsear_expresion para obtener los tokens
    tokens = parsear_expresion(expresion)
    
    # Filtra tokens de espacio
    tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']
    
    # Si la expresión estaba vacía retornar que esta vacio
    if not tokens_limpios:
        raise ExpresionInvalida("La expresión está vacía")
        
    # Inicializamos el resultado con el primer número romano
    # Por el parser sabemos que el primer token es un numero romano
    # Usamos el conversor
    resultado = romano_a_entero(tokens_limpios[0].valor)
    
    
    i = 1
    while i < len(tokens_limpios):
        operador = tokens_limpios[i]
        siguiente_numero = tokens_limpios[i+1]
        # Convertimos el siguiente número romano a entero
        valor_siguiente = romano_a_entero(siguiente_numero.valor)
        # Operacion
        if operador.tipo == "SUMA":
            resultado += valor_siguiente
        elif operador.tipo == "RESTA":
            resultado -= valor_siguiente  
        i += 2  # Saltamos al siguiente par 
        
    # Valida que el resultado sea positivo (> 0)
    # Los romanos no tenían el número 0 ni los números negativos
    if resultado <= 0:
        raise ExpresionInvalida("El resultado de la operación debe ser mayor a cero")
    return resultado
    raise NotImplementedError()
