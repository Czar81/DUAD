class BankAccount():
    balance = 0
        
    def add_money(self, money):
        self.balance += money
        print("Money was add succesful")


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance


    def withdraw(self, money):
        if (self.balance - money) >= self.min_balance:
            self.balance -= money
            print("Withdraw succesful")
        else:
            print("Can not do the withdraw, balance under minimun balance ")


def __input_amount(text):
    while True:
        try:
            amount = int(input(text))
            if amount < 0:
                raise ValueError
            else:
                return amount
        except ValueError as error:
            print(f"Error, invalid value, must be a positive number: {error}")


def __input_menu():
    while True:
        try:
            option = int(input("Enter an option: "))
            if option > 3  or option < 1:
                raise ValueError
            else:
                return option
        except ValueError as error:
            print(f"Error, value must be between 1 and 3: {error}")


def __menu():
    account = SavingsAccount(__input_amount("Enter the minimun balace: "))
    while True:
        print("""-----------------------
1. Add money
2. Withdraw
3. Exit
-----------------------""")
        option = __input_menu()

        if 1 == option:
            account.add_money(__input_amount("Enter amount of money: "))
        elif 2 == option:
            account.withdraw(__input_amount("Enter the amount to withdraw: "))
        elif 3 == option:
            print("Thanks for using")
            break


def main():
    __menu()


if __name__ == "__main__":
    main()
