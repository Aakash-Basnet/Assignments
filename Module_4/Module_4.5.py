import sys

i=5
a = input("enter the username: ")
b = input("enter the password: ")
while i>1:

    if a.lower()=="python" and b.lower()=="rules":
        print("Welcome")
        sys.exit()

    else:
        print('Wrong Credentials !!!! Try again')
        a=input("enter the username")
        b=input("enter the password")
        i -= 1

print("Access Denied")


