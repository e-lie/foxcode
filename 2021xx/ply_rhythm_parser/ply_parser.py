
from ply import lex
import ply.yacc as yacc

tokens = (
    'LBRACK',
    'RBRACK',
    'NOTE',
    'NOTE_STRONG',
    'STROKE',
    'STROKE_STRONG',
    'REST',
)

t_ignore = ' \t'

# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIV     = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
t_NOTE = r'[a-g]'
t_NOTE_STRONG = r'[A-G]'
t_STROKE = r'[hijkmnoxpqrstuvw]'
t_STROKE_STRONG = r'[HIJKMNOXPQRSTUVW]'
t_REST = r'-'



def t_LBRACK(t):
    r'[0-9]*\['
    # strip bracket char to keep the subdiv number
    if t.value[:-1]:
        t.value = int(t.value[:-1])
    return t

# t_LBRACK = r'[0-9]*\['
t_RBRACK = r'\]'

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_error( t ):
  print("Invalid Token:",t.value[0])
  t.lexer.skip( 1 )

lexer = lex.lex()

# precedence = (
#     ( 'left', 'PLUS', 'MINUS' ),
#     ( 'left', 'TIMES', 'DIV' ),
#     ( 'nonassoc', 'UMINUS' )
# )

# def p_add( p ) :
#     'expr : expr PLUS expr'
#     p[0] = p[1] + p[3]

# def p_sub( p ) :
#     'expr : expr MINUS expr'
#     p[0] = p[1] - p[3]

# def p_expr2uminus( p ) :
#     'expr : MINUS expr %prec UMINUS'
#     p[0] = - p[2]

# def p_mult_div( p ) :
#     '''expr : expr TIMES expr
#             | expr DIV expr'''

#     if p[2] == '*' :
#         p[0] = p[1] * p[3]
#     else :
#         if p[3] == 0 :
#             print("Can't divide by 0")
#             raise ZeroDivisionError('integer division by 0')
#         p[0] = p[1] / p[3]

# def p_expr2NUM( p ) :
#     'expr : NUMBER'
#     p[0] = p[1]

# def p_parens( p ) :
#     'expr : LPAREN expr RPAREN'
#     p[0] = p[2]

# def p_error( p ):
#     print("Syntax error in input!")

# parser = yacc.yacc()

# res = parser.parse("-4*-(3-5)") # the input


# Give the lexer some input
lexer.input("3[x-o-X-O]")

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)