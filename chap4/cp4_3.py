import random
print("\t\tWelcome to 'Guess My Number'!\n")
print("I'm thinking of a number between 1 and 100.\nTry to guess it in as few attempts as possible.\n")
gn = random.randrange(1,100)
trise = 0
num = 0
while num != gn:
    trise += 1
    num = int(input("Take a guess: "))
    if num > gn:
        print("Lower...")
    elif num < gn:
        print("Higher...")
    else:
        print("You guessed it! The number was ", gn, "\nAnd it only took you ", trise, "tries!")
