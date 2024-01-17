#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Lorem ipsum dolor sit amet. Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? Non autem hoc: igitur ne illud quidem.")
        Lorem ipsum dolor sit amet.
        
        Quonam modo?
        
        Utrum igitur tibi litteram videor an totas paginas commovere?
        
        Non autem hoc: igitur ne illud quidem.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in separators:
            lines.append(current_line.strip())
            lines.append("")  # Add an empty line
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    print("\n".join(lines))
