from ply import lex
from ply import yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'LBRA',
    'RBRA',
)

t_ignore_SPACE = r'[ \t]'

t_PLUS  = r'\+'
t_MINUS  = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LBRA = r'\('
t_RBRA = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

calc = input("Enter your calculation here:\n")

lexer.input(calc)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)