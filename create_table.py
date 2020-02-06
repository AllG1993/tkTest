# import db_connection
#
# cur = db_connection.cursor
#
# cur.execute('''CREATE TABLE test_db
#      (ADMISSION INT PRIMARY KEY NOT NULL,
#      NAME TEXT NOT NULL,
#      AGE INT NOT NULL,
#      COURSE CHAR(50),
#      DEPARTMENT CHAR(50));''')
#
# print('Таблица создана успешно')
#
# db_connection.conn.commit()
# db_connection.conn.close()
