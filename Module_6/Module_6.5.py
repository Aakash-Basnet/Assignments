numbers=[]

def evenlist(numbers):
    numbers2 = []
    for i in numbers:
        if i%2==0:
            numbers2.append(i)
    return numbers2

for i in range(10000):

    a=input("enter the numbers: ")
    if a=="":
        break
    else:
        numbers.append(int(a))

print(f'this is the original list: {numbers}')
a=evenlist(numbers)

print(f'this is the list after removing the odds: {a}')