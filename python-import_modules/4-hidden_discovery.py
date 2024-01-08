#!/usr/bin/python3
import dis
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <module_file>".format(sys.argv[0]))

    module_file = sys.argv[1]

    try:
        with open(module_file, 'rb') as file:
            code = file.read()

        bytecode = dis.Bytecode(code)
        names = set()

        for instruction in bytecode:
            if instruction.opname == 'LOAD_GLOBAL' and not instruction.argrepr.startswith('__'):
                names.add(instruction.argrepr)

        for name in sorted(names):
            print(name)

    except Exception as e:
        sys.exit("Error: {}".format(e))
