#!/usr/bin/python3
import types
import sys

def print_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <module_file>".format(sys.argv[0]))

    module_file = sys.argv[1]

    try:
        with open(module_file, 'rb') as file:
            magic = file.read(4)
            timestamp = file.read(4)
            code = file.read()

        module = types.ModuleType("hidden_4")
        exec(code, module.__dict__)

        print_names(module)

    except Exception as e:
        sys.exit("Error: {}".format(e))
