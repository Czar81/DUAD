i = 1
total = 0
while i <= 3:
    print(f"Ingrese el {i} de 3")
    n = int(input())
    if n == 30:
        print("Correcto")
        break
    else:
        total += n
        i += 1
else:
    if total == 30:
        print("Correcto")
    else:
        print("Incorrecto")