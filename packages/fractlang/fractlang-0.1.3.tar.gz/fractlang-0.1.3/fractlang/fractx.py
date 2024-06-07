import os
import shutil
import sys
from parser.log_parser import compile_fractlang
import subprocess
import pkg_resources

def get_package_version():
    try:
        version = pkg_resources.get_distribution("nama-paket").version
    except pkg_resources.DistributionNotFound:
        version = None
    return version

def main():
    if len(sys.argv) < 2:
        print("Usage: fractx compile [-run] <file_path>")
        return

    command = sys.argv[1]

    if command == '-v':
        version = get_package_version()
        if version:
            print(f"Fractlang version {version}")
        else:
            print("Fractlang version not found.")
        return

    if len(sys.argv) < 3:
        print("Please provide the path to the .fractx file.")
        return

    file_path = os.path.abspath(sys.argv[2])
    file_dir = os.path.dirname(file_path)
    compiled_dir = os.path.join(file_dir, 'fractcompiled')

    if command == 'compile':
        if not os.path.exists(compiled_dir):
            os.makedirs(compiled_dir)

        if not file_path.endswith('.fractx'):
            print("No file includes or named end with .fractx")
            return

        compile_fractlang(file_path)
        compiled_file_path = os.path.join(compiled_dir, os.path.basename(file_path).replace('.fractx', '.py'))
        shutil.move(file_path.replace('.fractx', '.py'), compiled_file_path)
        
        print(f"File has been compiled and moved to {compiled_file_path}")

        if len(sys.argv) == 4 and sys.argv[3] == '-run':
            run_compiled_file(compiled_file_path)

    else:
        print("Invalid argument. Usage: fractx compile [-run] <file_path>")

def run_compiled_file(compiled_file_path):
    with open(compiled_file_path, 'r') as f:
        code = compile(f.read(), compiled_file_path, 'exec')
        exec(code)

if __name__ == "__main__":
    main()
