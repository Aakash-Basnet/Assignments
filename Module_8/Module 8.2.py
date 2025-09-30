import mysql.connector
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

country_code=input('enter the Country code : ')
cursor.execute("SELECT * FROM airports where iso_country=%s ORDER BY type DESC",(country_code,))
airport_rows=cursor.fetchall()
if airport_rows:
    for items in airport_rows:
        print(f' {items[3]}\n:{items[2]} ')