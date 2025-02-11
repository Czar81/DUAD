i = 0
mujeres = 0
hombres = 0
while i <= 6:
    print("Ingrese el sexo de la persona. 1 para mujer, 2 para hombre")
    sexo = int(input())
    if sexo == 1:
        mujeres += 1
    elif sexo == 2:
        hombres += 1
    else:
        print("Error, valor no valido")
    i+=1
porcentaje_mujeres = (mujeres / 6) * 100
porcentaje_hombres = (hombres / 6) * 100
print( f"Porcentaje de mujeres: {porcentaje_mujeres} % \nPorcentaje de hombres: {porcentaje_hombres} %")