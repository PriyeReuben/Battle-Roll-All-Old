class Weapon:
    name=""
    type=""
    damage_dice=[]
    special_dice=[]
    magic_constant=0
    special_constant=0

    def __init__(self, name, type, damage_dice, special_dice, magic_constant, special_constant):
        self.name = name
        self.type = type
        self.damage_dice = damage_dice
        self.special_dice = special_dice
        self.magic_constant = magic_constant
        self.special_constant = special_constant

w1 = Weapon("Dagger", "slashing", [1,4], [], 0, 0)

def workhorse():
    from Dice import Dice
    d = Dice()
    roll =(d.rolls(1,20))
    if roll == 20:
        print(str(roll) + "\nCritical hit!")
        damage = d.rolls(w1.damage_dice[0]*5, w1.damage_dice[1])
        print(str(damage) + " point(s) of " + w1.type + " damage.")

    elif roll >= 15:
        print(roll)
        print("You hit with a " + w1.name + "!")
        damage = d.rolls(w1.damage_dice[0], w1.damage_dice[1])
        print(str(damage) + " point(s) of " + w1.type+" damage.")
    else:
        print(roll)
        print("You missed!")

