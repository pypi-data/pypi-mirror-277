import sys
from colorama import Fore, Style

# Menambahkan jalur folder 'lexer' ke sys.path
sys.path.append('./lexer')

# Mengimpor lexer dari modul lexer
from lexer import lexer

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
