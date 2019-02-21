import mysql.connector
mydb=mysql.connector.connect(host='local host',user='root',password='root',database='db')
x=mydb.cursor()
x.execute("insert into cust"(id,name,address,phone,email,landmark) values(%s,%s,%s,%s,%s,$s)",z)
