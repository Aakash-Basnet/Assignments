list1=[]
for i in range(1000):
    num=input("enter the numbers or press enter to quit: ")
    if num=="":
        break
    else:
        list1.append(int(num))
print(list1)
list1.sort(reverse=True)
print(f'the top 5 greatest numbers are: ')
for i in range(5):

    print(list1[i])

