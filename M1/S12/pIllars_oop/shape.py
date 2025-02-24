from abc import ABC, abstractmethod
import math


class Shape():
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
    def calculate_perimeter(self, side):
        result = side * 4
        self.print_result("perimeter", result) 


    def calculate_area(self,side):
        result = side*side
        self.print_result("area", result) 


class Rectangle(Shape):
    def calculate_perimeter(self, base, side):
        result = (base*2)+(side*2)
        self.print_result("perimeter", result) 
    

    def calculate_area(self, base, side):
        result = (base*2)+(side*2)
        self.print_result("area", result) 


def __input_menu_option():
    try:
        option = int(input("Enter an option: "))
        if option > 7  or option < 1:
            raise ValueError
        else:
            return option
    except ValueError as error:
        print(f"Error, value must be between 1 and 7: {error}")


def __input_numbers(text):
    try:
        amount = int(input(text))
        if amount < 0:
            raise ValueError
        else:
            return amount
    except ValueError as error:
        print(f"Error, invalid value, must be a positive number: {error}")


def menu():
    while True:
        print("""----------------------------
1. Circle Area
2. Circle Perimeter
3. Square Area
4. Square Perimeter
5. Rectangle Area
6. Rectangle Perimeter
7. Exit
----------------------------""")
        option = __input_menu_option()
        if 1 == option:
            circle_area = Circle()
            radio = __input_numbers("Enter the radio: ")
            circle_area.calculate_area(radio)
        elif 2 == option:
            circle_perimeter = Circle()
            radio = __input_numbers("Enter the radio: ")
            circle_perimeter.calculate_perimeter(radio)
        elif 3 == option:
            square_area = Square()
            side = __input_numbers("Enter the side: ")
            square_area.calculate_area(side)
        elif 4 == option:
            square_perimeter = Square()
            side = __input_numbers("Enter the side: ")
            square_perimeter.calculate_perimeter(side)
        elif 5 == option:
            rectangle_area = Rectangle()
            base = __input_numbers("Enter the base: ")
            side = __input_numbers("Enter the side: ")
            rectangle_area.calculate_area(base, side)
        elif 6 == option:
            rectangle_perimeter = Rectangle()
            base = __input_numbers("Enter the base: ")
            side = __input_numbers("Enter the side: ")
            rectangle_perimeter.calculate_perimeter(base, side)        
        elif 7 == option:
            print("Thanks for using")
            break



def main():
    menu()


if __name__ == "__main__":
    main()