scores = [("Larry", 1500), ("Moe", 1000)]
while 1:
    print("\n\tHigh Scores Keeper\n")
    print("\t0 - Quit\n\t1 - List Scores\n\t2 - Add a score\n")
    choice = int(input("Chlice: "))
    if choice == 0:
        break
    elif choice == 1:
        print("\nHigh Scores\n")
        scores.sort()
        print("NAME\tSCORE")
        for entry in scores:
            name, score = entry
            print(name, "\t", score)
    elif choice == 2:
        name = input("\nWhat is the player's name?: ")
        score = int(input("What score did the player get?: "))
        entry = (name, score)
        scores.append(entry)
    else:
        print("Try again")
