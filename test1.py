import mysql.connector as conn

mydb = conn.connect(host = "localhost", user ="root", passwd = "mYsQL@2022" )
cursor = mydb.cursor()
#cursor.execute("create database sudhanshu")
cursor.execute("show databases")
#cursor.execute(s)
print(cursor.fetchall())