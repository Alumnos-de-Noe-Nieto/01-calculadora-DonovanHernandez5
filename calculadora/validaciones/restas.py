# RESTAS VALIDAS #
def validar_restas(cadena: str) -> bool:
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    i = 0
    while i < len(cadena) - 1:
        # Detectamos si hay una intención de resta (Valor actual < Valor siguiente)
        if valores[cadena[i]] < valores[cadena[i+1]]:
            par = cadena[i : i+2]
            # Validacion
            if par not in sustracciones_validas:
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
