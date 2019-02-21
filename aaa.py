def connect():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='db')
    return mydb
def insert(kooi):
    val=connect()
    x=val.cursor()
    x.executemany("insert into product(id,name,description,price)values(%s, %s, %s, %s)",kooi)
    val.commit()

m=[('c012','cpm','dell',2000),('c091','cpgu','dellu',2000)]
insert(m)