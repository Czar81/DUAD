i = 1
sum = 0
print("Ingrese un numero")
n = int(input())
while i <= n:
    if i == n:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
    sum += i
    i += 1
print(sum)