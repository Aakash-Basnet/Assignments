year=int(input("enter a year: "))
if (year % 4==0 and year%100!=0) or( year%100==0 and year%400==0):
    print("the given year is a leap year")
else:
    print("given year is not leap year")