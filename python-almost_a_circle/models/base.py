#!/usr/bin/python3
"""Base documentation"""

class Base:
    """this stuff is througly documented"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id