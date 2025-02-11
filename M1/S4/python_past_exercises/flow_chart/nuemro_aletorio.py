import random
secret_number = random.randrange(1,10)
input_number = 0
print(secret_number)

while input_number != secret_number:
    print("Introdusca un numero del 1 al 10 para adivinar el numero secreto")
    input_number = int(input())
    if input_number == secret_number:
        print(f"{secret_number} era el numero secreto")
    else:
        print("Ese no es el numero secreto")