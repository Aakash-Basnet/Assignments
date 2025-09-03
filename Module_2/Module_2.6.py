import random
from random import randint
code1=[]
code2=[]
for i in range(3):
    num=randint(0,9)
    code1.append(num)
print(f'Code 1 {code1}')


for i in range(4):
    num=randint(1,6)
    code2.append(num)
print(f'Code 2 {code2}')