def look_for_numbers(func):
    def wrapper(*args):
        try: 
            for argument in args:
                if isinstance(argument,(int,float, complex)):
                    pass
                else:
                    raise ValueError
            func(*args)
        except ValueError as error:
            print(f"Argument must be a number: {error}")
    return wrapper


@look_for_numbers
def sum(a, b, c):
    #Functionality
    pass

@look_for_numbers
def multiply(a, b, c):
    #Functionality
    pass

sum(32, "23",  90.2)
multiply(0.22, "3.14", 89)