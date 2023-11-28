class Critter:
    def __init__(self, name, mood_level):
        self.name = name
        self.mood_level = mood_level
    def talk(self):
        print("\nI'm", self.name, "I feel ", end='')
    def feed(self):
        print("\nYami!")
    def play(self):
        print("\nWheee!")
    def setMood(self, level):
        self.mood_level=self.mood_level+level
        if self.mood_level<0:
            self.mood_level=0
        elif self.mood_level>10:
            self.mood_level=10
    def getMood(self):
        return self.mood_level

class food:
    def __init__(self, name):
        self.name=name
    def getLevel(self):
        if self.name=="animal feed":
            return 2
        elif self.name=="fruit":
            return 3
        elif self.name=="steak":
            return 4
def setCritterLevel(critter):
    critter.setMood(food.getLevel())
# main
name=input("What do you wnat to name your critter?: ")
crit = Critter(name, 5)
while 1:
    print("\n\t\tCritter Caretaker\n")
    print("\t0 - Quit\n\t1 - Listen to your critter\n\t2 - Feed your critter\n\t3 - Play with your critter\n")
    choice=int(input("Choice: "))
    if (choice==0):
        exit()
    elif (choice==1):
        level=crit.getMood()
        if level>=0 and level<3:
            mood="mad now"
        elif level>=3 and level<=5:
            mood="frustrated now"
        elif level>5 and level<=7:
            mood="soso now"
        else:
            mood="happy now"
        crit.talk()
        print(mood)
        crit.setMood(-1)
    elif (choice==2):
        print("\nChoose your critter's food\n\n\t0 - animal feed\n\t1 - fruit\n\t2 - steak\n")
        choice=int(input("Choice: "))
        while 1:
            if(choice==0):
                food=food("animal feed")
                setCritterLevel(crit)
                break
            elif(choice==1):
                food=food("fruit")
                setCritterLevel(crit)
                break
            elif(choice==2):
                food=food("steak")
                setCritterLevel(crit)
                break
            else:
                choice=int(input("Choice again: "))
    elif (choice==3):
        crit.play()
        crit.setMood(3)
    else:
        choice=int(input("\nChoice: "))
