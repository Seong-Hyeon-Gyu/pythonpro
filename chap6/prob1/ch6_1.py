inventory = ["sword","armor","shield","healing potion"]
print("Your items:")
for item in inventory:
    print(item)
conti = input("\nPress the enter key to continue.")
if conti == "":
    print("You have", len(inventory), "items in your possession.")
conti = input("\nPress the enter key to continue.")
if conti == "":
    if "healing potion" in inventory:
        print("You will live to fight another day.")
itemindex = int(input("\nEnter the index number for an item in inventory: "))
print("At index", itemindex, "is", inventory[itemindex])
bn = int(input("\nEnter the index number to begin a slice: "))
en = int(input("Enter the insex number to end the slice: "))
print("inventory[", bn, ":", en, "] \t\t", inventory[bn:en])
conti = input("\nPress the enter key to continue.")
if conti == "":
    chest = ["gold", "gems"]
    print("You find a chest. It contains:\n", chest[:])
    print("You add the contents of the chest to your inventory.")
    inventory += chest
    print("Your inventory is now:\n", inventory[:])
conti = input("\nPress the enter key to continue.")
if conti == "":
    print("You trade our sword for a crossbow.")
    inventory[0] = "crossbow"
    print("Your inventory is now:\n", inventory[:])
conti = input("\nPress the enter key to continue.")
if conti == "":
    print("You use your gold an gems to buy on orb of future telling.")
    inventory[4:6] = ["orb of future telling"]
    print("Your inventory is now:\n", inventory[:])
conti = input("\nPress the enter key to continue.")
if conti == "":
    print("In a great battle, your shield is destroyed.")
    del inventory[2]
    print("Your inventory is now:\n", inventory[:])
conti = input("\nPress the enter key to continue.")
if conti =="":
    print("Your crossbow and armor are stolen by thieves.")
    del inventory[0:2]
    print("Your inventory is now:\n", inventory[:])
