import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="db")

print(mydb)

x=mydb.cursor()
x.execute("select * from cust")
for i in x:
    print(i)


