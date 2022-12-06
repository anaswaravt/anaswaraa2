import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythonDB")
#creating cursor object
cur=mydb.cursor()
try:
    # cur.execute("create database pythonDB")
    dbs=cur.execute("show databases")
except:
    mydb.rollback()
for x in cur:
    print(x)
    
mydb.close()
