gallons=float(input("enter the quantity in gallons: "))
def conversion():
    for i in range(10000):
        if gallons>0:
             litres=gallons*3.78541
             gallons=float(input("enter the quantity in gallons: "))

litre=conversion()
print(f'{gallons} gallons is {litre} litres')
