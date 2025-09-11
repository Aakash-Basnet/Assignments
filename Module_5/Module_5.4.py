cities=[]

for i in range(10000):
    city = input("enter the name of the city: ")
    if city!="":
        cities.append(city)
    else:
        break


for i in cities:
    print(i)