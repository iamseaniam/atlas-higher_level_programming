#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    arg_plural = "s" if num_args != 1 else ""

    print("{} argument{}:".format(num_args, arg_plural) + ("" if num_args == 0 else ":"))
    
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
