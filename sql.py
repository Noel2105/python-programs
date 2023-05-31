import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Noel", passwd="5690", database="hello")

mycursor = mydb.cursor()
mycursor.execute("select * from bro")

result = mycursor.fetchone()

for i in result:
    print(i)
