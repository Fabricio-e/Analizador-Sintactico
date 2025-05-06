# lexer.py
import ply.lex as lex

# Definición de tokens
token_list = (
    'NUM',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'LBRACKET',
    'RBRACKET',
    'IF',       # Opcional
    'ELSE',     # Opcional
    'WHILE'     # Opcional
)

# Patrones para tokens básicos
t_ADD     = r'\+'
t_SUB     = r'-'
t_MUL     = r'\*'
t_DIV     = r'/'
t_LBRACKET  = r'\('
t_RBRACKET  = r'\)'

# Funciones para procesar tokens
def t_NUM(t):
    r'\d+(\.\d+)?'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

# Caracteres a ignorar
t_skip  = ' \t'

# Manejo de errores
def t_bad_char(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear instancia del lexer
my_lexer = lex.lex()

if __name__ == '__main__':
    test_input = "3 + 4 * (10 - 2.5) if x"
    my_lexer.input(test_input)
    while True:
        current_token = my_lexer.token()
        if not current_token:
            break
        print(current_token)