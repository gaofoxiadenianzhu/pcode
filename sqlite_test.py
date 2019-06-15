import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cmd = 'create table user2(id varchar(20) primary key, name varchar(20))'
cursor.execute(cmd)

cmd = 'insert into user2(id,name) values(\'1\', \'Michael\')'
cursor.execute(cmd)
print(cursor.rowcount)
conn.commit()

cmd = 'select * from user2 where id = \'1\''
cursor.execute(cmd)
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
