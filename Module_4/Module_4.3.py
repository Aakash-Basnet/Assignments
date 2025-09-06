number=[]
num = (input("enter the numbers : "))
while num !="":
    num=float(num)
    number.append(num)
    num=input("enter another number or just press enter to exit: ")
number.sort()
print(f'the greatest number among the entered number is: {number[len(number)-1]}')
print(f'the smallest number among the entered number is: {number[0]}')



