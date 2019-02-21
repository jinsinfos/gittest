def connect():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='db')
    return mydb
def insert(id):
    val=connect()
    x=val.cursor()
    x.execute("select * from cust where id="+id)
    for i in x:
        print(i)

insert('111')