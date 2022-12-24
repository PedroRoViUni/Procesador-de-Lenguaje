import sys
import ply.lex as lex

tokens = (
    'NEWH',
    'FALSE',
    'TRUE',
    'ID',
    'NUM',
    'ACCE',
    'SUBIR',
    'BAJAR',
    'PARAR',
    'SI',
    'CALE',
    'AIRE',
    'PERS',
    'ROCI',
    'ALAR',
    'LUM',
    'TEM',
    'PRE',
    'GAS',
    'FUE',
    'HUM',
    'AND',
    'OR',
    'LLAVEI',
    'LLAVED',
    'PCOMA',
    'COMA',
    'PARENI',
    'PAREND',
    'IGUAL',
    'MENOR',
    'MAYOR',
    'CORCHI',
    'CORCHD',
    'GUION',
    'IGUALC',
    'DISTIN',
)

t_NEWH   =r'(n|N)ew (h|H)ogar'
t_FALSE  =r'(f|F)alse' 
t_TRUE   =r'(t|T)rue' 
t_ID     =r'[a-z]+[0-9]+'          
t_NUM    =r'[1-9][0-9]+' 
t_ACCE   =r'accesos:' 
t_SUBIR  =r'subir' 
t_BAJAR  =r'bajar' 
t_PARAR  =r'parar' 
t_SI     =r'si|if'
t_CALE   =r'cale' 
t_AIRE   =r'aire' 
t_PERS   =r'pers' 
t_ROCI   =r'roci' 
t_ALAR   =r'alar' 
t_LUM    =r'lum' 
t_TEM    =r'tem' 
t_PRE    =r'pre' 
t_GAS    =r'gas' 
t_FUE    =r'fue' 
t_HUM    =r'hum' 
t_AND    =r'and' 
t_OR     =r'or' 
t_LLAVEI = r'{' 
t_LLAVED = r'}' 
t_PCOMA  = r';' 
t_COMA   = r',' 
t_PARENI = r'\(' 
t_PAREND = r'\)' 
t_IGUAL  = r'=' 
t_MENOR  = r'<' 
t_MAYOR  = r'>' 
t_CORCHI = r'\[' 
t_CORCHD = r'\]' 
t_GUION  = r'-'
t_IGUALC = r'=='
t_DISTIN = r'!='

t_ignore  = '[ \t\r]+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# Error handling rule
def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()
def main(argv):
    
    input_stream = open(argv[1],"r")
    lexer.input(input_stream.read())
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

if __name__ == '__main__'   : main(sys.argv)