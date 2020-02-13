import db_connection

cur = db_connection.cursor

cur.execute('''CREATE TABLE defective_headset2
      (serial_number TEXT NOT NULL,
      workplace INT NOT NULL,
      malfunction CHAR(50));''')

print('Таблица создана успешно')
db_connection.conn.commit()
db_connection.conn.close()
