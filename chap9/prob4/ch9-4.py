class Critter:
    total=0
    def __init__(self, name):
        print("A critter has been born!")
        Critter.total+=1
    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)
# main
print("Accessing the class attribute Critter.total:", Critter.total)
print("\nCreating critters.")
crit1=Critter("critter 1")
crit2=Critter("critter 2")
crit3=Critter("critter 3")
Critter.status()
print("\nAccessing the class attribute through an object:", Critter.total)
