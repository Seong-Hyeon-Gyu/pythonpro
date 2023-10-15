import random
words = ["DIFFICULT","BANANA","APPLE","PYTHON","DAEGU","CATHOLIC","UNIVERSITY"]
body = [" ______"," |    |"," |"," |"," |"," |"," |"," |"," |","________"]
change = [" |    O"," |    +"," |   -+"," |   -+-"," |   /"," |   / \ "]
wd = random.choice(words)
nwd = len(wd)
lwd = list(wd)
bw = list(wd)
lw = []
lenwd = nwd
i=0
attempts=0
while lenwd != 0:
    bw[i] = '-'
    i+=1
    lenwd-=1
i=0
while i < len(body):
    print(body[i])
    i+=1
ct = 0
while attempts < 6:
    w = input("\nEnter your guress: ")
    if w in lwd:
        print("\nYes!", w, "is in the word!\n")
    else:
        print("\nNo...", w, "is not in the word...\n")
        if ct ==0:
            body[2]=change[0]
            ct+=1
        elif ct == 1:
            body[3]=change[1]
            ct+=1
        elif ct ==2:
            body[3]=change[2]
            ct+=1
        elif ct ==3:
            body[3]=change[3]
            ct+=1
        elif ct ==4:
            body[4]=change[4]
            ct+=1
        else:
            body[4]=change[5]
    i = 0;
    while i < len(body):
        print(body[i])
        i+=1
    lenwd=nwd
    lw.append(w)
    i=0
    count=0
    while lenwd != 0:
        if wd[i]==w:
            bw[i]=w
        else:
            count += 1
        i+=1
        lenwd-=1
    lenwd = nwd
    if count == nwd:
        attempts += 1
    if bw==wd:
        print("Congratulation! you guessed the word:", wd)
        exit()
    
    print("\n\nYou've used the following letters:\n", lw)
    print("\nSo far, the word is:")
    for letter in bw:
        print(letter,end='')
print("\nIncorrect Guess.\nThe correct word was", wd)
