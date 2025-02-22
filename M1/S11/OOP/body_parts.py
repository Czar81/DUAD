class Hand:
    def __init__(self):
        self.wrist = None
        self.palm= None
        self.knuckles= None
        self.fingers= None


class Arm:
    def __init__(self, hand):
        self.shoulder = None
        self.elbow = None
        self.forearm = None
        self.hand = hand


class Foot:
    def __init__(self):
        self.ankle= None
        self.heel= None
        self.fingers= None
        self.instep= None


class Leg:
    def __init__(self, foot):
        self.gluteus= None
        self.thigh= None
        self.knee= None
        self.foot = foot


class Torso:
    def __init__(self):
        self.neck= None
        self.chest= None
        self.abdomen= None
        self.belly_button= None


class Head:
    def __init__(self):
        self.hair= None
        self.eyes= None
        self.ears= None
        self.nose= None
        self.mouth= None


class Human:
    def __init__(self, head, torso, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.torso = torso
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


def main():
    # Hands
    right_hand = Hand()
    left_hand = Hand()
    # Arms
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)
    # Feet
    right_foot = Foot()
    left_foot = Foot()
    # Legs
    right_leg = Leg(right_foot)
    left_leg = Leg(left_foot)
    # Torso
    torso = Torso()
    # Head
    head = Head()
    # Human
    human = Human(head, torso, right_arm, left_arm, right_leg, left_leg)
    print(f"The object {human} is a human")


if __name__ == '__main__':
    main()