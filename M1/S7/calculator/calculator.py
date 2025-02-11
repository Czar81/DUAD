import random  


def calculator():
    number_one = random.randrange(1, 10)
    continue_process = 1
    while continue_process != 0:
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Borrar resultado")
        option_menu = input_menu("Seleccione una opcion: ")
        number_two = input_number("Ingrese un numero para la operacion: ") 
        if option_menu == 1:
            result = sum_int(number_one,number_two)
        elif option_menu == 2:
            result = subtraction_int(number_one,number_two)
        elif option_menu == 3:
            result = multiplication_int(number_one,number_two)
        elif option_menu == 4:
            result = division_int(number_one,number_two)
        else:
            result = delate_result()
        print(result)
        number_one = result 
  

def input_menu(option_menu):
    menu_input = int(input(option_menu))
    try:
        if menu_input < 1 or menu_input > 5:
            raise IndexError
        else:
            return menu_input
    except IndexError:
        print("Ha introducido un valor fuera del rango establecido")


def input_number(number):
    try:
        return int(input(number)) 
    except ValueError as error:
        print(f"Ha introducido un valor no valido {error}")
        

def sum_int(number_one ,number_two):
    return number_one + number_two


def subtraction_int(number_one, number_two):
    return number_one - number_two


def multiplication_int(number_one, number_two): 
    return number_one * number_two


def division_int(number_one, number_two):
    return number_one / number_two


def delate_result():
    return random.randrange(1, 10)


def main():
    try:
        calculator()
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")


if __name__ == "__main__":
    main()