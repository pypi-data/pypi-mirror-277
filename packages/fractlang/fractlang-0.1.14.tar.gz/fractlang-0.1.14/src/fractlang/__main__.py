# __main__.py
import sys
from colorama import Fore, Style
from lexer.lexer import lexer
from parser.parser import parser

def read_frx_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        parser.parse(content, lexer=lexer)
    except FileNotFoundError:
        print(f"{Fore.RED}File not found!{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print(f"{Fore.RED}Usage: fractx run <file_name.frx>{Style.RESET_ALL}")
        return

    file_name = sys.argv[2]
    if not file_name.endswith(".frx"):
        print(f"{Fore.RED}File must have .frx extension{Style.RESET_ALL}")
        return

    read_frx_file(file_name)

if __name__ == "__main__":
    main()
