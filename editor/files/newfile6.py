import mysql.connector


dbconf = {
  "user": "terahzbf_test", 
  "pass": "oN7staJjuYb5", 
  "name": "terahzbf_test",   
  "host": "162.241.148.100"
}

mydb = mysql.connector.connect(
  host=dbconf["host"],
  user=dbconf["user"],
  passwd=dbconf["pass"],
  database=dbconf["name"]
)

mycursor = mydb.cursor()

sql = "INSERT INTO data (date, price) VALUES (%s, %s)"
val = [
  ('2019/10/21', '10.23'),
  ('2019/11/21', '8.00'),
  ('2019/07/21', '100.40')
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


