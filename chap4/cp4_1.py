import random
print("I sense your energy. Your true emotions are coming across my screen.")
print("Your are...")
print("\t\t-----------\n\t\t|         |\n\t\t| O    O  |\n\t\t|   <     |\n\t\t|         |")
mood = random.randrange(0,2)
if mood == 0:
    print("\t\t| .     . |\n\t\t|  '...'  |\n\t\t-----------")
elif mood == 1:
    print("\t\t|   ...   |\n\t\t| .'   '. |\n\t\t-----------")
elif mood == 2:
    print("\t\t| ....... |\n\t\t|         |\n\t\t-----------")
else:
    print("Illegal mood vlue!")
print("...today.")
