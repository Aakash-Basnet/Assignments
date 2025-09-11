import random
dices=int(input("enter the amount of dice to roll: "))
list1=[]
for i in range(dices):
    list1.append(random.randint(1,6))
print(list1)
sum1=0
for i in list1:
    sum1=sum1+i
print(f'the sum of the {dices} dices rolled randomly is {sum1}')



