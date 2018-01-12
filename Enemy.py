import Dice as dice
class Enemy():
    ac = 0
    profBonus = 0
    abilityMod = 0
    advantage=0

    def __init__(self):
        self.ac = 0
        self.profBonus = 0
        self.abiltyMod=0

#Setters
    def setAC(x):
        Enemy.ac = x

    def setAbilityMod(x):
        Enemy.abilityMod = x

    def setProfBonus(x):
        Enemy.profBonus = x


# getters
    def getAC(self):
        return Enemy.ac

    def getProfBonus(self):
        return Enemy.profBonus

    def getAbilityMod(self):
            return Enemy.abilityMod


