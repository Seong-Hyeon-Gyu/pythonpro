print("\t\t Trust Fund Buddy\n")
print("Totals your monthly spending so that your frust fund doesn's run out(and you're forced to get a real job).\n")
print("Plase enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.\n\n")
car = int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staf (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = int(input("Computer Games: "))
total = car+rent+jet+gifts+food+staff+guru+games
print("\nGrand Total:", total)