import random
print("Welcome to Word Jumble!\nUnscramble the letters to make a word.")
words=('defficult','banana','apple','python','daegu','catholic','university')
ci = random.choice(words)
rd = list(ci)
random.shuffle(rd)
print("Jumbled word:", end='')
for letter in rd:
    print(letter, end='')
print('\n')
a=input("Your guess: ")
if a == ci:
    print("That's right")
else:
    print("Sorry, that's not correct. The word was:", end='')
    for letter in ci:
        print(letter,end='')
    print('\n')
