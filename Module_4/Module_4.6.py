import random
total=int(input("input the numbers to be generated"))
inside_circle=0
count=total

while count>0:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2 + y**2 < 1:
        inside_circle+=1
    count-=1
pi=4*inside_circle/total

print(f'approximate value of Pi is : {pi}')