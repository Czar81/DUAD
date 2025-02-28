from datetime import date

class User:
    def __init__(self, date_birth):
        self.date_birth = date_birth
    

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_birth.year - (
            (today.month, today.day) < 
            (self.date_birth.month, self.date_birth.day))
        return age

def is_adult(func):
    def wrapper(user):
        if user.age >= 18:
            print("Is an adult")
            return func(user)
        else:
            print("Is not an adult")
    return wrapper


@is_adult
def login(user):
    pass

my_user = User(date(2007, 6, 19))
login(my_user)