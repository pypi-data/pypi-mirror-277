import sys

def read_frx_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found!"

def main():
    if len(sys.argv) < 3 or sys.argv[1] != "run":
        print("Usage: fractx run <file_name.frx>")
        return

    file_name = sys.argv[2]
    if not file_name.endswith(".frx"):
        print("File must have .frx extension")
        return

    file_content = read_frx_file(file_name)
    print(file_content)

if __name__ == "__main__":
    main()
