#!/usr/bin/python3
"""Base Class keeps id or makes one if it doesnt have an id"""


class Base:
    """keeps or makes a new id"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
