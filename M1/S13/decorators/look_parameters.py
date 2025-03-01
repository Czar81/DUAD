def look_for_numbers(func):
    def wrapper(*args, **kwargs):
        try: 
            for argument in args:
                if not isinstance(argument,(int,float, complex)):
                    raise ValueError   
            for argument in kwargs.values():
                if not isinstance(argument,(int,float, complex)):
                    raise ValueError
                
            return func(*args, **kwargs)
        except ValueError as error:
            print(f"{argument} must be a number: {error}")
            return None
    return wrapper


@look_for_numbers
def sum(a, b, c):
    #Functionality
    pass

@look_for_numbers
def multiply(a, b, c):
    #Functionality
    pass

print(sum(32, 23, 90.2))  
print(sum(32, "23", 90.2))  
print(multiply(0.22, 3.14, 89))  
print(multiply(0.22, "3.14", 89)) 