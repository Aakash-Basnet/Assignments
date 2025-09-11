numbers=[]
def sum1(numbers):
    a=0
    for i in numbers:
        a=a+i
    return a
items=input("enter the numbers for the list: ")
for i in range (10000):
    if items=="":
        break
    else:
        numbers.append(int(items))
        items=input("enter the numbers for the list: ")

print(numbers)
print(sum1(numbers))

