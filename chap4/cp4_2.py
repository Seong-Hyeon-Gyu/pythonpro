import random
hehp = random.randrange(50,100)
monhp = random.randrange(50,100)
print("hero HP: ", hehp, "monster HP: ", monhp)
phase = 0
while hehp > 0 and monhp > 0:
    phase += 1
    hat = random.randrange(-10,20)
    mat = random.randrange(-10,20)
    if hat>0:
        hst = "success"
        if hat>0:
            monhp -= hat
    else:
        hst = "fail"
    if mat>0:
        mst = "siccess"
        if mat>0:
            hehp -= mat
    else:
        mst = "fail"
    print("hero(HP:", hehp, ", attck:", hat, ") ", hst, " <-> monster(HP:", monhp, ", attck:", mat, ") ", mst)
print("Total phase: ", phase)
if hehp > monhp:
    print("Hero Win!!!!")
else:
    print("Monster win!!!!")
