import random
sides=int(input("enter the number of sides: "))
def diceroll():
    a=random.randint(1,sides)
    return a
for i in range (10000):
    b=diceroll()
    if b==sides:
        print (b)
        break
    else:
        print(b)
