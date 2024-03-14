import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="1234Qwer!",
    database="college"#add database that we can use 
)
l=mydb.cursor()
# l.execute("create database college")
l.execute("show databases")
for i in l:
    print(i)

