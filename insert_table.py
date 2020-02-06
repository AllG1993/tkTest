import db_connection

cur = db_connection.cursor
conn = db_connection.conn

cur.execute(
    "INSERT INTO test_db (ADMISSION, NAME, AGE, COURSE, DEPARTMENT) VALUES (202020, 'Василий', 18, 'IT', 'С++')"
)

conn.commit()
print('Данные записаны')

conn.close()