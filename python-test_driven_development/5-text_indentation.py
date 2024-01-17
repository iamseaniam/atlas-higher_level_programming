#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in separators:
            lines.append(current_line)
            current_line = "\n"
    if current_line:
        lines.append(current_line)

    cleaned_lines = [line.strip() for line in lines]
    print("".join(cleaned_lines))
