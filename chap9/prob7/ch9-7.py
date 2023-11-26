class Critter:
    moodlevel = 3
    def __init__(self, name):
        self.name = name
    def talk(self):
        Critter.moodlevel-=1
        if (Critter.moodlevel<1):
            Critter.moodlevel+=1
        if (Critter.moodlevel==1):
            print("\nI'm ", self.name, "I feel mad now.\n")
        elif (Critter.moodlevel==2):
            print("\nI'm ", self.name, "I feel frustrated now\n")
        elif (Critter.moodlevel==3):
            print("\nI'm ", self.name, "I feel soso now\n")
        elif (Critter.moodlevel==4):
            print("\nI'm ", self.name, "I feel happy now\n")
    def feed(self):
        print("\nYami!")
        Critter.moodlevel+=1
        if (Critter.moodlevel>4):
            Critter.moodlevel=4
    def play(self):
        print("\nWheee!")
        Critter.moodlevel+=2
        if (Critter.moodlevel>4):
            Critter.moodlevel=4
# main
name=input("What do you wnat to name your critter?: ")
crit = Critter(name)
while 1:
    print("\n\t\tCritter Caretaker\n")
    print("0 - Quit\n1 - Listen to your critter\n2 - Feed your critter\n3 - Play with your critter\n")
    choice=int(input("Choice: "))
    if (choice==0):
        exit()
    elif (choice==1):
        crit.talk()
    elif (choice==2):
        crit.feed()
    elif (choice==3):
        crit.play()
    else:
        choice=int(input("\nChoice: "))
