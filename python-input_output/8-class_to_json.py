#!/usr/bin/python3
"""documentatin for all the stuff"""


def class_to_json(obj):
    """documentatin for all the stuff"""
    if hasattr(obj, '__dict__'):
        serialized_obj = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_obj[key] = value
            elif hasattr(value, '__dict__'):
                serialized_obj[key] = class_to_json(value)
    else:
        serialized_obj = obj

    return serialized_obj
