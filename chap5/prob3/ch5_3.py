import random
print("Guess the word!!!\nIn this game, the program select a word at random, and the player's objective is to guess the chosen word.\n")
words = ('difficult','banana','apple','python','daegu','catholic','university')
pw = random.choice(words)
cp = list(pw)
bk = list(pw)
lenbk = len(pw)
print("Length of the selected word:", lenbk)
attempts = 6
i = 0
while lenbk != 0:
    bk[i] = '_'
    i += 1
    lenbk -= 1
lenbk = len(pw)
while attempts > 0:
    print("remaining attempts:",attempts)
    print("Current guessed word: ", end='')
    for letter in bk:
        print(letter, end='')
    cr = input("\nGuess a letter: ")
    j=0
    count = 0
    while lenbk != 0:
        if pw[j]==cr:
            bk[j] = cr
        else:
            count += 1
        j += 1
        lenbk -= 1
    lenbk = len(pw)
    if count == len(pw):
        attempts -= 1
    if bk == cp:
        print("Congratulation! you guessed the word:", pw)
        exit()
print("Incorrect guess.\nYou've used up all your attempts. the correct word was", pw)
