#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], (int, float)):
                print("{:d}".format(int(my_list[i])), end="")
                count += 1
        print()
        return count
    except (ValueError, TypeError):
        print()
        return count
