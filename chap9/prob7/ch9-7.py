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
        crit.feed()
        crit.setModd(2)
    elif (choice==3):
        crit.play()
        crit.setMood(3)
    else:
        choice=int(input("\nChoice: "))
