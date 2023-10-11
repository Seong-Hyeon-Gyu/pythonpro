geek = {"404" : "clueless.", "Uninstalled" : "being fired."}
while 1:
    print("\n\tGeek Translator\n")
    print("\t0 - Quit\n\t1 - Look Up a Geek Term\n\t2 - Add a Geek Term\n\t3 - Reefine a Geek Term\n\t4 - Delete a Geek Term\n")
    choice = int(input("Choice: "))
    if choice == 0:
        break
    elif choice == 1:
        gw = input("\nWhat term do you want me to translate?: ")
        if gw in geek:
            print(gw, "means", geek[gw])
        else:
            print("I have no idea what", gw, "is")
    elif choice == 2:
        gw = input("\nWhat term do you want me to add?: ")
        gl = input("What"+ gw+ "means?: ")
        geek[gw] = gl
    elif choice == 3:
        gw = input("\nWhat term do you want me to redefine?: ")
        if gw in geek:
            gl = input("redefine: ")
            geek.get(gw, gl)
        else:
            print(gw, "is not in geek")
    elif choice == 4:
        gw = input("\nWhat term do you wnat mt to delete?: ")
        if gw in geek:
            del geek[gw]
        else:
            print("I can not found", gw)
    else:
        print("Try again")
