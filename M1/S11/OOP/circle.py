import math
class CircleClass:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi*(self.radius**2)

def validate_input_radius():
    try:
        radius = int(input("Enter the radius of the circle"))
        if radius <= 0:
            raise ValueError
    except ValueError as error:
        print(f"Invalid radius: {error}") 


def main():
    radius = validate_input_radius()
    circle = CircleClass(radius)
    print(f"The area of ​​the circle is: {circle.get_area()}")


if __name__ == "__main__":
    main()