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

def p_expression(p):
    '''expression : expression PLUS component
        | expression MINUS component'''
    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]

def p_expression_comp(p):
    'expression : component'
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

def p_factor(p):
    '''factor : value
    | LBRA expression RBRA'''
    if p[1] == "(":
        p[0] = (p[2])
    else:
        p[0] = p[1]

def p_component(p):
    '''component : component MULT factor
        | component DIV factor'''
    if p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]

def p_component_factor(p):
    'component : factor'
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

