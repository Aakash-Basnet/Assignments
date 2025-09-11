import random

def diceroll():
    a=random.randint(1,6)
    return a
for i in range (10000):
    b=diceroll()
    if b==6:
        print (b)
        break
    else:
        print(b)
