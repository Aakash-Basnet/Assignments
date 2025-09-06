import random
num=[]
a=int(input(f'the computer has one integer try to guess it, enter your guess: '))
while num!="":
        num.append(random.randint(1,10))

        if num[0] > a and num[0] - 1 == a:
            print("you are close but still you are smaller")
        elif num[0] > a:
            print("too low")
        elif num[0] < a and num[0] + 1 == a:
            print('you are close but still higher')
        elif num[0] < a:
            print("too high")
        else:
            print("you are correct : \U0001F600")
            break

        a = int(input("enter again"))