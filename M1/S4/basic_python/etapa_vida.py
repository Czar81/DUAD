print("Ingrese su nombre")
name = input()
print("Ingrese su apellido")
last_name = input()
print("Ingrese su edad")
age = int(input())
print(f"{name} {last_name} ")
if age >= 60:
    print("Es un audulto mayor")
elif age > 21 and age < 60:
    print("Es un audulto")
elif age >= 18 and age <= 21:
    print("Es un audulto joven")
elif age > 12 and age < 18:
    print("Es un adolecente")
elif age == 12:
    print("Es un preadolecente")
elif age > 1 and age < 12:
    print("Es un niño")
elif age <= 1:
    print("Es un bebe")
else:
    print("Error, valor no valido")