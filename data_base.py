import psycopg2
from psycopg2 import sql
from pprint import pprint
import main
conn = psycopg2.connect(dbname='peripheryx_test_db', user='aleksey',
                        password='30071993ga', host='localhost')
cursor = conn.cursor()

p1 = str(main.user_text_sn.get())
p2 = str(main.user_text_rm.get())
p3 = str(main.breakdown_list.get())

with conn.cursor() as cursor:
    conn.autocommit = True
    values = [
        (p1, p2, p3)
    ]
    insert = sql.SQL('INSERT INTO defective_headset (serial_number, workplace, malfunction) VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)

cursor.execute('SELECT * FROM defective_headset')
records = cursor.fetchall()

pprint(records)
cursor.close()
conn.close()