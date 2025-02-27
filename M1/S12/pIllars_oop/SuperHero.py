class Flyer:
    def fly(self):
        print("I cab flying through the skies")


class SuperStrength:
    def lift_weight(self, weight):
        print(f"I'm lifting {weight} kg")


class Superhero(Flyer, SuperStrength): 
    def __init__(self, name, strength):
        self.name = name
        self.lift_weight(strength)



superman = Superhero("Superman", 1000)
