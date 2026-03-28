# NIVEL 1: ALFABETO
def validar_simbolos(cadena: str) -> bool:
    #Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.
    # Eliminamos espacios en los extremos
    # Con strip los espacios de los lados no afectan
    cadena_limpia = cadena.strip()
    # Cadenas vacias
    if len(cadena_limpia) == 0:
        return False
    # 3. Definición del alfabeto permitido (Σ)
    alfabeto_romano = "IVXLCDM"
    # Validación carácter por carácter
    for caracter in cadena_limpia:
        if caracter not in alfabeto_romano:
            # En cuanto encuentra ALGO que no sea romano (letra minúscula,
            # número, símbolo o espacio intermedio), rechaza la cadena.
            return False
    # Regresar cadena valida
    return all(caracter in alfabeto_romano for caracter in cadena_limpia)
    raise NotImplementedError()
