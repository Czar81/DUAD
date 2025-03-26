from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    def print_result(self, request, result):
        print(f"""----------------------------
The result of {request} is {result}""")


class Circle(Shape):
    def calculate_perimeter(self, radio):
        result = math.pi*radio*2
        self.print_result("perimeter", result) 
    

    def calculate_area(self, radio):
        result = math.pi*radio*radio
        self.print_result("area", result) 


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        result = self.side * 4
        self.print_result("perimeter", result)

    def calculate_area(self):
        result = self.side * self.side
        self.print_result("area", result)


class Rectangle(Shape):
    def __init__(self, base, side):
        self.base = base
        self.side = side

    def calculate_perimeter(self):
        result = (self.base * 2) + (self.side * 2)
        self.print_result("perimeter", result)

    def calculate_area(self):
        result = self.base * self.side
        self.print_result("area", result)


def __input_submenu_option():
    while True:
        try:
            option = int(input("Enter an option: "))
            if option > 3 or option < 1:
                raise ValueError
            else:
                return option
        except ValueError as error:
            print(f"Error, value must be between 1 and 3: {error}")


def __input_menu_option():
    while True:
        try:
            option = int(input("Enter an option: "))
            if option > 4 or option < 1:
                raise ValueError
            else:
                return option
        except ValueError as error:
            print(f"Error, value must be between 1 and 4: {error}")


def __input_numbers(text):
    while True:
        try:
            amount = float(input(text))
            if amount < 0:
                raise ValueError
            else:
                return amount
        except ValueError as error:
            print(f"Error, invalid value, must be a positive number: {error}")


def submenu(shape_object):
    while True:
        print("""----------------------------
1. Perimeter
2. Area
3. Get back
----------------------------""")
        option_submenu = __input_submenu_option()
        if option_submenu == 1:
            shape_object.calculate_perimeter()
        elif option_submenu == 2:
            shape_object.calculate_area()
        elif option_submenu == 3:
            return


def menu_main():
    while True:
        print("""----------------------------
1. Circle 
2. Square 
3. Rectangle 
4. Exit
----------------------------""")
        option_main = __input_menu_option()

        if option_main == 1:
            radio = __input_numbers("Enter the radius: ")
            circle = Circle(radio)
            submenu(circle)
        elif option_main == 2:
            side = __input_numbers("Enter the side: ")
            square = Square(side)
            submenu(square)
        elif option_main == 3:
            base = __input_numbers("Enter the base: ")
            side = __input_numbers("Enter the side: ")
            rectangle = Rectangle(base, side)
            submenu(rectangle)
        elif option_main == 4:
            print("Thanks for using")
            break


if __name__ == "__main__":
    menu_main()
