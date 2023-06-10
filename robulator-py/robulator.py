from ply import lex
from ply import yacc

tokens = (
    'NUMBER',
    'PLUS',
)

t_ignore_SPACE = r' \t'

t_PLUS  = r'\+'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex.lex()

calc = input("Enter your calculation here:\n")

lexer.input(calc)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)