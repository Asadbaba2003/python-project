import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asad23",
    database="mydb"
)

mycurs = mydb.cursor()
mycurs.execute("CREATE TABLE users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")
mycurs.execute("SHOW TABLES")
sql="INSERT INTO users(name, email, password) values(%s,%s,%s)"
val=("asad","asadbaba2003@gmail.com","asadasad")
mycurs.execute(sql,val)

print(mycurs)
