class Critter:
    def __init__(self, name):
        print("A new critter has been born!")
        self.name=name
    def talk(self):
        print("\nHi, I'm", self.name)
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if new_name=="":
            print("A critter's name can't be empty string.")
        else:
            self._name=new_name
            print("Name change successful.")
    name=property(get_name, set_name)
# main
crit=Critter("Poochie")
crit.talk()
print("\nMy critter's name is: ", end='')
print(crit.get_name())
print("\nAttempting to change my critter's name.")
crit.set_name("")
print("\nAttempting to change my critter's name again")
crit.set_name("Randolph")
crit.talk()
