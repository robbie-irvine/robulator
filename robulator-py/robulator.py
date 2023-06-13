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

def p_operation(p):
    '''operation : operation PLUS value
        | operation MINUS value'''
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]

def p_operation_value(p):
    'operation : value'
    p[0] = p[1]

def p_value(p):
    '''value : NUMBER
    | PLUS NUMBER 
    | MINUS NUMBER'''
    if p[1] == "+":
        p[0] = p[2]
    elif p[1] == "-":
        p[0] = -(p[2])
    else:
        p[0] = p[1]

parser = yacc.yacc()

while True:
    try:
        calc = input("Enter your calculation here:\n")
    except EOFError:
        break
    if not calc: continue
    result = parser.parse(calc)
    print(result)

