data={}
info=int(input("enter 1 to store new airport\nenter 2 to fetch information of an existing airport\nenter 3 to quit\n"))
while info!=3:
    if info==1:
        icao_id=(input("enter the ICAO code: "))
        airport=input("enter the name of airport")
        data[icao_id]=airport
        print('Data has been added successfully')
    elif info==2:
        icao=input("enter the Icao  of an airport: ")
        if icao in data:
            print(f'The {icao} airport is {data[icao]}')
    else:
        break
    info = int(
        input("enter 1 to store new airport\nenter 2 to fetch information of an existing airport\nenter 3 to quit\n"))



