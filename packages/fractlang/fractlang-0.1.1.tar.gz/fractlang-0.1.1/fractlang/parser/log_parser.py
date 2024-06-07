import re

variables = {}

def compile_fractlang(file_path):
    with open(file_path, 'r') as file:
        fractlang_code = file.read()
    execute_fractlang(fractlang_code)

def execute_fractlang(code):
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('explicit int'):
            handle_declaration(line)
        elif line.startswith('log('):
            handle_log(line)
        else:
            handle_expression(line)

def handle_declaration(line):
    match = re.match(r'explicit int (\w+) = (\d+)', line)
    if match:
        var_name = match.group(1)
        var_value = int(match.group(2))
        variables[var_name] = var_value
        print(f"Declared {var_name} with value {var_value}")

def handle_log(line):
    if 'explicit.auto' in line:
        total = sum(variables.values())
        print(f"Log (explicit.auto): {total}")
    else:
        expr = line[4:-1]  # Remove 'log(' and ')'
        result = eval(expr, {}, variables)
        print(f"Log: {result}")

def handle_expression(line):
    if line:
        result = eval(line, {}, variables)
        print(f"Expression result: {result}")
