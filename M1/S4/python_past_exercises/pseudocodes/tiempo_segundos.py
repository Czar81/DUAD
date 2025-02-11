print("Ingrese el tiempo en segundos")
tiempo_segundo = int(input())
if tiempo_segundo < 600:
    tiempo_faltante = 600 - tiempo_segundo
    print(f"Es menor y faltan {tiempo_segundo} para ser 10 minutos")
elif tiempo_segundo == 600:
    print("Valor es igual a 10 minutos")
elif tiempo_segundo > 600:
    print("Valor es mayor a 10 minutos")
else:
    print("Error, valor no valido")