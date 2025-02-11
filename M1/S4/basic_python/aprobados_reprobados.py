print("Ingrese la cantidad de notas")
cantidad_notas = int(input())
contador = 1
cantidad_notas_aprobadas = 0
cantidad_notas_reprobadas = 0
promedio = 0.0
promedio_aprobadas = 0.0
promedio_reprobadas = 0.0

while contador <= cantidad_notas:
    print(f"Ingrese la nota #{contador}")
    nota = int(input())
    if nota >= 70:
        cantidad_notas_aprobadas += 1
        promedio_aprobadas += nota
    else:
        cantidad_notas_reprobadas += 1
        promedio_reprobadas += nota
    promedio += nota
    contador += 1
promedio = promedio/cantidad_notas
promedio_aprobadas = promedio_aprobadas/cantidad_notas
promedio_reprobadas = promedio_reprobadas/cantidad_notas

print(f"""Notas Aprobadas: {cantidad_notas_aprobadas} 
Notas  Reprobadas: {cantidad_notas_reprobadas}
Promedio General: {promedio} 
Promedio Notas Aprobadas: {promedio_aprobadas}
Promedio Notas Reprobadas: {promedio_reprobadas}""")