
def conversion():
    for i in range(10000):
        gallons = float(input("enter the quantity in gallons: "))
        if gallons>0:
             litres=gallons*3.78541
             print(f'{gallons} gallons is {litres} litres')
        else:
            break

conversion()

