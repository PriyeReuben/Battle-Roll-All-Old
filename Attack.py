from Dice import Dice as d
from Enemy import Enemy as e
from Weapon import Weapon as w
from Characters import Characters as c

class Attack:
    name=""
    ac=0
    profBonus=0
    abilityMod=0
    advantage =0
    critRange=0


    def __init__(self):
        self.name = w.name
        self.ac = c.ac
        self.profBonus = e.profBonus
        self.abilityMod = e.abilityMod
        self.weaponBonus = w.magic_constant
        self.advantage = 0
        self.critRange = 0

    def display(self):
        print(" Name: "+ str(self.name) +"\n",
              "To hit: "+ str(self.ac) +"\n",
              "Ability Modifier: "+ str(self.abilityMod) +"\n",
              "Proficiency Bonus: "+ str(self.profBonus))

    def getName(self):
        return self.name

    def damage(self,x,y,z,c):
        damagePoints=d.rolls(x*c, y, z)
        #print(damagePoints)
        return damagePoints



    def attack(self, toHit):#ac, profBonus, abilityBonus, advantage, damDiceNum, damDiceSize, critMult
        #d20=d.Dice.rolls(1,20,e.Enemy.getProfBonus(self)+e.Enemy.getAbilityMod(self))
        d20 = d.rolls(1, 20)
        self.profBonus = str(e.getProfBonus(self))
        print("Proficiency Bonus: "+ self.profBonus)

        self.abilityMod = str(e.getAbilityMod(self))
        print("Ability Modifier: "+ self.abilityMod)
        #print("Ability Modifier: {}".format(e.getAbilityMod(self)))
        print("D20: {}".format(d20))

        total=0
        if d20==1:
            total="critical miss!"

        elif d20 == 20:
            total="critical hit!"
        else:
            total= d20 + e.getProfBonus(self) + e.getAbilityMod(self)
            if total<toHit:
                print("Miss!")
            else:
                print("Hit!")
        print("Total: {}".format(total))

def main():
    atk = Attack()
    atk.display()
    atk.ac = 40
    atk.display()
main()








