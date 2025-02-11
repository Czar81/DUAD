mayor = 0
for i in range(3):
    print(f"Ingrese un valor")
    number_input = int(input())
    if number_input > mayor:
        mayor = number_input
print(f"El mayor es: {mayor}")