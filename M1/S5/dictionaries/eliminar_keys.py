list_keys = ["access_level", "age"]
employee = {"name": "John", 
            "email": "john@ecorp.com", 
            "access_level": 5, 
            "age": 28}
for i in list_keys:
    employee.pop(i)
print(employee)