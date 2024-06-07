import sys
from colorama import Fore, Style
from ply import lex

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
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_PLUS_EQUALS = r'\.plusEquals'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore_COMMENT = r'\#.*'
t_ignore_NEWLINE = r'\n'

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

def read_frx_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        lexer.input(content)
        tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)
        return tokens
    except FileNotFoundError:
        return [(f"{Fore.RED}File not found!{Style.RESET_ALL}",)]

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print(f"{Fore.RED}Usage: fractx run <file_name.frx>{Style.RESET_ALL}")
        return

    file_name = sys.argv[2]
    if not file_name.endswith(".frx"):
        print(f"{Fore.RED}File must have .frx extension{Style.RESET_ALL}")
        return

    tokens = read_frx_file(file_name)
    for tok in tokens:
        if isinstance(tok, tuple):
            print(f"{Fore.GREEN}{tok[1]}{Style.RESET_ALL}")
        else:
            print(tok)

if __name__ == "__main__":
    main()
