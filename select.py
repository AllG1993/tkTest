import db_connection

cur = db_connection.cursor
conn = db_connection.conn

cur.execute("SELECT id, serial_number, workplace, malfunction from defective_headset")

rows = cur.fetchall()
for row in rows:
    print("ID =", row[0])
    print("Серийный номер =", row[1])
    print("Рабочее место =", row[2])
    print("Неисправность =", row[3], "\n")

print("Operation done successfully")

conn.close()