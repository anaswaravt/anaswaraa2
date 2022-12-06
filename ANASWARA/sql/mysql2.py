import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb")
cur=myconn.cursor()

try:
    cur.execute("create table EMP(id int not null primary key,name varchar not null,salary int,dep_id int not null,branch varchar(20) not null,foriegn key(dep_id) references DEPARTMENT (dep_id)")
except:
    myconn.rollback()
    
myconn.close()