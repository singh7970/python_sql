import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="1234Qwer!",
  database="school"
)


mycursor =mydb.cursor()
# mycursor.execute("create table student(Nmae varchar(100),ADDRESS varchar(100)) ")
sql = "INSERT INTO student (NAME, address) VALUES (%s, %s)"
val=("priyanshu","halkorwa")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
    