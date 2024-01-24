#!/usr/bin/python3
"""documentatin for all the stuff"""


def append_write(filename="", text=""):
    '''Append a string to the end of a text file (UTF8) and return the number of characters added'''
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
