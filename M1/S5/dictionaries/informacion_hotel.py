hotel_data = {}
habitaciones = []

print("Ingrese el nombre")
hotel_data['nombre'] = input()
print("Ingrese el numero de estrellas")
hotel_data['numero_estrellas'] = int(input())

print("Ingrese el numero de habicion")
habitaciones.append(int(input()))
print("Ingrese el piso de habicion")
habitaciones.append(int(input()))
print("Ingrese el precio por noche")
habitaciones.append(int(input()))
hotel_data['habitaciones'] = habitaciones
print(hotel_data)