import db_connection

cur = db_connection.cursor
conn = db_connection.conn

cur.execute("SELECT admission, name, age, course, department from test_db")

rows = cur.fetchall()
for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")

conn.close()