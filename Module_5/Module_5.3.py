number=int(input("enter the number you want to check for prime: "))
if number<=1:
    print("this is not a prime number")


for i in range(2,number):
    if number%i==0:
        print(f'this is not a prime number')
        break
else:
        print("this is  a prime number")
