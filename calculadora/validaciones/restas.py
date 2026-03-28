"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
"""


def validar_restas(cadena: str) -> bool:
    VALORES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    i = 0
    while i < len(cadena) - 1:
        # Detectamos si hay una intención de resta (Valor actual < Valor siguiente)
        if VALORES[cadena[i]] < VALORES[cadena[i+1]]:
            par = cadena[i : i+2]           
            # Validacion
            if par not in SUSTRACCIONES_VALIDAS:
                return False
            
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            # Si la resta es válida, saltamos ambos caracteres
            i += 2
        else:
            # Si no es una resta, avanzamos normal
            i += 1
            
    return True
    raise NotImplementedError()
