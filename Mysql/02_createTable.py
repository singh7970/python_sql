import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="abc",
    password="1234Qwer!",
    database="college",
)
mycursor=mydb.cursor()
# for creating a table
# mycursor.execute("CREATE TABLE school (name varchar(100), address VARCHAR(200), schoolCode INT AUTO_INCREMENT PRIMARY KEY)")

""" We use the statement "INT AUTO_INCREMENT PRIMARY KEY" 
which will insert
a unique number for each record. Starting at 1,
 and increased 
by one for each record."""

# for showing tables
mycursor.execute("show tables")
for i in mycursor:
    print(i)