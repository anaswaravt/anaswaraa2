import mysql.connector
mydb=mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
)
cur=mydb.cursor()
try:
    cur.execute("create table dprtmnt(id int not null primary key,dep_name varchar(20))")
except:
    mydb.rollback()
mydb.close()

    



import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb")
cur=mydb.cursor()
sql="insert into dprtmnt(id,dep_name)values(%s,%s)"
val=[(1,"civil"),(2,"cs"),(3,"accountant")]
try:
    cur.executemany(sql,val)
    mydb.commit()
except:
    mydb.rollback()
print(cur.rowcount,"record inserted!")

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb")
cur=mydb.cursor()
try:
    cur.execute("create table empl(department_id int not null primary key,name varchar(20) not null,salary int,id int not null,branch varchar(25),foreign key(id) references dprtmnt(id))")
except:
    mydb.rollback()
mydb.close()

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb")
cur=mydb.cursor()
sql="insert into empl(department_id,name,salary,id,branch)values(%s,%s,%s,%s,%s)"
val=[(1001,"abi",25000,1,"kochi"),(1003,"manu",23900,2,"calicut"),(1002,"aji",1234,2,"kochi")]
try:
    cur.executemany(sql,val)
    mydb.commit()
except:
    mydb.rollback()
print(cur.rowcount,"record inserted!")
mydb.close()
    
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb")
cur=mydb.cursor()
try:
    cur.execute("select empl.department_id,empl.name,empl.salary,empl.id,empl.branch,dprtmnt.id,dprtmnt.name from dprtmnt join empl on dprtmnt.id=empl.id")
    print( " id    name  salary  branch   department_id    dept_name")
    for row in cur:
        print("%d  %s  %d %s  %d  %s "%(row[0],row[1],row[2],row[3],row[4],row[5]))
except:
    mydb.rollback()
mydb.close()
    
