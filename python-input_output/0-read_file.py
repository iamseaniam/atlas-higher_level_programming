#!/usr/bin/python3
"""documentatin for all the stuff"""

def read_file(filename=""):
    """documentatin for all the stuff"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
