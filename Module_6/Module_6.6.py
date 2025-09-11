diameter1= float(input("enter the diameter of 1st pizza in cm: "))
price1=float(input("enter the price of 1st pizza: "))
diameter2=float(input("enter the diameter of 2nd pizza in cm: "))
price2=float(input("enter the price of 2nd pizza: "))
def price_per_square(x,y):
    meters=x/100
    radius=meters/2
    area=3.1416*radius*radius
    price_pizza=y/area
    return price_pizza
a=price_per_square(diameter1,price1)
b=price_per_square(diameter2,price2)

if a>b:
    print("the second pizza provides the better value for money")
elif b>a:
    print("the first pizza provides the better value for money")
else:
    print("both provides the equal values for money")