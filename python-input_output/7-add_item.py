#!/usr/bin/python3
"""documentatin for all the stuff"""


import sys
from os import path
from json import dump, load
from pathlib import Path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item():
    """documentatin for all the stuff"""
    
    filename = "add_item.json"
    my_list = []

    if Path(filename).is_file():
        my_list = load_from_json_file(filename)

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_item()
