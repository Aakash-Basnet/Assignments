import mysql.connector
from geopy.distance import geodesic

def establish_connection():

    host='127.0.0.1'
    user='aakash'
    password='1234'
    database ='airport'

    conn=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if conn.is_connected():
        print(f'Connection Established.........')
    else:
        print(f'Connection rejected')
    return conn

conn=establish_connection()

cursor=conn.cursor()
#for AIRPORT TABLE

ICAO1=input('enter the ICAO code of country 1 : ')
ICAO2=input('enter the ICAO code of country 2 : ')

cursor.execute("SELECT name,latitude_deg,longitude_deg FROM airports where ident=%s",(ICAO1,))
airport_rows1=cursor.fetchall()
cursor.execute("SELECT name,latitude_deg,longitude_deg FROM airports where ident=%s",(ICAO2,))
airport_rows2=cursor.fetchall()
name1=airport_rows1[0][0]
name2=airport_rows2[0][0]
coordinates1=(airport_rows1[0][1],airport_rows1[0][2])
coordinates2=(airport_rows2[0][1],airport_rows2[0][2])
print(name1,name2,coordinates1,coordinates2)
distance_kilo=geodesic(coordinates1,coordinates2).kilometers
distance_miles=geodesic(coordinates1,coordinates2).miles

print(f'the distance between the given: {ICAO1} {name1} and {ICAO2} {name2} is \033[32m{distance_kilo:.2f}\033[0m kilometres or \033[32m{distance_miles:.2f}\033[0m miles')

