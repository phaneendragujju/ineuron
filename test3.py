import mysql.connector as conn

mydb = conn.connect(host = "localhost", user ="root", passwd = "mYsQL@2022" )
cursor = mydb.cursor()
s = "insert into sudhanshu.ineuron values(101,'sudhanshu kumar', 'sudhanshu@ineuron.ai',100,30)"
cursor.execute(s)
mydb.commit()