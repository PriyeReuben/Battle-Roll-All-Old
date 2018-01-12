import random

class Dice:
    size=0
    times=0


    def __init__(self):
        self.size=0
        self.times=0

    def dice(self,a): #size
        num=random.randint(1,a)
        #print(num)
        return num

    def rolls(self,x,y): #times, size
        sum=0
        for i in range(1,x+1):
            sum=sum+self.dice(y)

        return sum

    def advant(someList):
        count=0
        advantageList=[]
        for x in someList:
            d=Dice.dice(20)
            if d>x:
                advantageList.append(d)
            else:
                advantageList.append(x)
        return advantageList

    def disadvant(someList):
        count=0
        disadvantageList=[]
        for x in someList:
            d=Dice.dice(20)
            if d<x:
                disadvantageList.append(d)
            else:
                disadvantageList.append(x)
        return disadvantageList

def workhorse():
    d = Dice
    # print(d.rolls(4 ,10))

    rollsList = []
    for x in range(2):
        rollsList.append(d.rolls(1, 20))

    print("R: " + str(rollsList))

    print("A: " + str(d.advant(rollsList)))

    print("D: " + str(d.disadvant(rollsList)))

    hits = []
    for x in rollsList:
        if x + 7 >= 22:
            hits.append(x)
    print("Rolls that hit vs AC 22: " + str(hits))
def dice5d6():
    d = Dice()
    count = 0
    while True:
        value = d.rolls(8,100)
        count = count + 1
        if value < 100:
            print("Roll Number {}: {}".format(count, value))
        else:
            pass

dice5d6()