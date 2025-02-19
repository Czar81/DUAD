class BusClass:
    def __init__(self, max_passengers):
        self.passengers = []
        self.max_passengers = max_passengers
        pass


    def add_passengers(self, person):
        if len(self.passengers) >= self.max_passengers:
            print("The bus is full")
        else:
            self.passengers.append(person)
            print(f"{person.name} (ID: {person.id}) are on bus")
            
        
    def remove_passengers(self):
        if len(self.passengers) > 0:
            remove_passenger = self.passengers.pop(0)
            print(f"{remove_passenger.name} (ID: {remove_passenger.id}) got off the bus")
        else:
            print("There are not passengers on the bus")
        

class People:
    def __init__(self, name, id):
        self.name = name
        self.id = id


def validate_option_menu():
    try:
        while True:
            option = int(input("Enter 1 to add a passanger, 2 to remove a passanger and 3 to close the program\n"))
            if option <= 3 or option >= 1:
                return option
            else:
                raise ValueError
    except ValueError as error:
        print(f"Invalid option must be between 1 and 3: {error}")


def main():
    Bus = BusClass(int(input("Enter the maximum of passangers of the bus\n")))
    while True:
        option = validate_option_menu()

        if option == 1:
            name = input("Enter the name of the passenger\n")
            id = input("Enter the id of the passenger\n")
            person = People(name, id)
            Bus.add_passengers(person)
        elif option == 2:
            Bus.remove_passengers()
        elif option == 3:
            print("Thanks for using the program")
            break


if __name__ == "__main__":
    main()