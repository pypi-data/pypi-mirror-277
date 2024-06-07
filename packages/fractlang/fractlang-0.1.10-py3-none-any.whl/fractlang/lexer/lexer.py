from ply import lex
from colorama import Fore, Style

# List of token names
tokens = (
    'INTEGER',
    'EQUALS',
    'PLUS_EQUALS',
    'LPAREN',
    'RPAREN',
    'COMMENT',
    'NEWLINE',
    'IDENTIFIER',
    'KEYWORD',
    'TYPE',
    'STRING',
    'BOOL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_PLUS_EQUALS = r'\.plusEquals'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ignore_COMMENT = r'\#.*'
t_ignore_NEWLINE = r'\n'
t_ignore = ' \t'

# A regular expression rule with some action code
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'group':
        t.type = 'KEYWORD'
    elif t.value in ('int', 'str', 'bool'):
        t.type = 'TYPE'
    elif t.value in ('True', 'False'):
        t.type = 'BOOL'
        t.value = True if t.value == 'True' else False
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
