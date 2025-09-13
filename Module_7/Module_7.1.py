season=('Winter','Spring','Summer','Autumn',)
month=int(input("enter the month: "))

if month>=1 and month<4:
    print(season[0])
elif month>=4 and month<7:
    print((season[1]))
elif month>=7 and month<10:
    print(season[2])
elif month>=10 and month<13:
    print(season[3])
else:
    print("That's not a month")

