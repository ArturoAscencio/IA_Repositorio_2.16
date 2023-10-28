pip install ply

import ply.yacc as yacc

# Definici�n de tokens (previamente definidos en el an�lisis l�xico)
tokens = [
    'NUMBER',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
]

# Reglas de gram�tica ambigua
def p_expression(p):
    """
    expression : expression PLUS expression
               | expression TIMES expression
               | LPAREN expression RPAREN
               | NUMBER
    """
    p[0] = ('expression', p[1:])  # Almacena el �rbol de an�lisis

# Manejo de errores sint�cticos
def p_error(p):
    print(f"Error sint�ctico en l�nea {p.lineno}: Token inesperado '{p.value}'")

# Crear el analizador sint�ctico
parser = yacc.yacc()

# Funci�n para analizar expresiones y mostrar �rboles de an�lisis
def analyze_expression(expression):
    parsed = parser.parse(expression)
    print(f"An�lisis de la expresi�n: {expression}")
    print(parsed)

# Ejemplos de expresiones ambiguas
expression1 = "2 + 3 * 4"
expression2 = "(2 + 3) * 4"

analyze_expression(expression1)
analyze_expression(expression2)
