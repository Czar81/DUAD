def print_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"The arguments of the function {func.__name__} are {args} {kwargs}")
        return func(*args, **kwargs) 

    return wrapper

@print_arguments
def sum(a, b):
    print(a+b)


@print_arguments
def sum_strings(text_a, text_b):
    print(f"{text_a} {text_b}")


sum(3, 5)
sum_strings("Hello", "world!")