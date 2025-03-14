def reversed_string(text):
    if not isinstance(text, str):
        raise TypeError
    return text[::-1]
