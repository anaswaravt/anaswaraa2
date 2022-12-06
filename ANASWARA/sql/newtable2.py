import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cur=myconn.cursor()
try:
    cur.execute("create table EMPLOY(id int primary key not null,name varchar(20) not null,salary int,dep_id varchar(10)not null,foreign key(dep_id) references (dep_id))")
except:
    myconn.rollback()
myconn.close()