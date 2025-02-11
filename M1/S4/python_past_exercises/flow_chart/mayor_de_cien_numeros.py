i = 1
mayor = 0
while i <= 100:
    print(f"Ingrese el nuemero {i} de 100")
    n = int(input())
    if n > mayor:
        mayor = n
    i+=1
print(f"El mayor es {mayor}")