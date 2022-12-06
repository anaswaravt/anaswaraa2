import mysql.connector
myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythondb"
    )
cur=myconn.cursor()
#insert multiplevalues
   sql="insert into Employee(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
   val=[("John",112,25000.00,201,"Newyork"),("Ram",111,23000.00,203,"portofspain"),("Raj",304,43000.00,504,"newyork")]
try:
    cur.execute("delete from Employee where id=112")
    cur.executemany(sql,val)
    #commit transaction
    myconn.commit()

except:
    myconn.rollback()
print(cur.rowcount,"record inserted!")

myconn.close()