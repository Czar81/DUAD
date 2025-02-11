list_a = ["first_name", "last_name", "role"]
list_b = ["Ian", "Zuniga", "Future Software Engineer"]
employees = {}
for i in range(0, len(list_a)):
    employees[list_a[i]] = list_b[i]
print(employees)