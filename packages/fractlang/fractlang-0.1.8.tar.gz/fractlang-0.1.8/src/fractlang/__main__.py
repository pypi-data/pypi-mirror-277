import sys
from colorama import Fore, Style

def read_frx_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"{Fore.RED}File not found!{Style.RESET_ALL}"

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print(f"{Fore.RED}Usage: fractx run <file_name.frx>{Style.RESET_ALL}")
        return

    file_name = sys.argv[2]
    if not file_name.endswith(".frx"):
        print(f"{Fore.RED}File must have .frx extension{Style.RESET_ALL}")
        return

    file_content = read_frx_file(file_name)
    print(f"{Fore.GREEN}{file_content}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
