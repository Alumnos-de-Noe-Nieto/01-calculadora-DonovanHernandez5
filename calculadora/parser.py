# PARSER #
from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.
    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """
    tipo: str
    valor: str
    posicion: int
def evaluar_expresion(expresion: str) -> list[Token]:
    # Retorna [] si la expresion es vacio
    # Usamos .strip() para que '   ' también se considere vacío
    if not expresion.strip():
        return []
    try:
        # Obtener los tokens
        tokens = tokenizar_expresion(expresion)
        # Validar la estructura
        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
        return tokens
    except ExpresionInvalida as e:
        raise e
    raise NotImplementedError()
def tokenizar_expresion(expresion: str) -> list[Token]:
    tokens = []
    i = 0
    alfabeto_romano = "IVXLCDM"
    while i < len(expresion):
        char = expresion[i]
        if char == ' ':
            tokens.append(Token("ESPACIO", " ", i))
            i += 1
        elif char == '+':
            tokens.append(Token("SUMA", "+", i))
            i += 1
        elif char == '-':
            tokens.append(Token("RESTA", "-", i))
            i += 1
        elif char in alfabeto_romano:
            inicio = i
            # Avanzar mientras sean caracteres romanos
            while i < len(expresion) and expresion[i] in alfabeto_romano:
                i += 1
            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))
        else:
            raise ExpresionInvalida(f"Carácter inválido '{char}' en posición {i}")
    return tokens
    raise NotImplementedError()
def validar_estructura_tokens(tokens: list[Token]) -> bool:
    # Filtrar espacios para validar solo la lógica aritmética
    tokens_limpios = [t for t in tokens if t.tipo != 'ESPACIO']
    # Validaciones básicas de longitud y paridad
    if not tokens_limpios:
        return True # Una lista vacía es válida según el nivel 7.1
    if len(tokens_limpios) < 3 or len(tokens_limpios) % 2 == 0:
        return False
    # Validar alternar tipo
    for i, token in enumerate(tokens_limpios):
        if i % 2 == 0: # Posiciones 0, 2, 4...
            if token.tipo != "ROMANO":
                return False
        else: # Posiciones 1, 3, 5...
            if token.tipo not in ["SUMA", "RESTA"]:
                return False
    return True
    raise NotImplementedError()
