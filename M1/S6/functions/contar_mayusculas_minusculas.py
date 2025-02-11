def upper_lower(text):
    upper_count = 0
    lower_count = 0
    for i in (range(0, len(text))):
        tmp_char = text[i]
        if tmp_char.isupper():
            upper_count += 1
        else:
            lower_count += 1
    print(f"Tiene {upper_count} y {lower_count} minusculas")


print("Ingrese el texto")
text_input = input()
upper_lower(text_input)