import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
    )
cur=myconn.cursor()
try:
    cur.execute("alter table Employee add branch_name varchar(20) not null")
except:
    myconn.rollback()
myconn.close()