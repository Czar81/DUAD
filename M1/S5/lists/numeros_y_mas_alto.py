mayor = 0
list_numbers = []
number = 0
for i in range(10):   
 print(f"Ingrese un valor")    
 number = int(input())
 list_numbers.append(number)
 if number > mayor: 
  mayor = number
print(f"{list_numbers}\nEl mayor es: {mayor}")

