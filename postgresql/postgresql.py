import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="123456", host="127.0.0.1", port="5432")
print('opened database successfully')

cur = conn.cursor()
'''
cmd = 'create table company(id int primary key not null, name text not null, age int not null, address char(50),salary real);'
cur.execute(cmd)
print('table created successfully')
'''


cmd1 = "insert into company(id,name,age,address,salary) values(1,'Paul',32,'California',20000.00);"
cmd2 = "insert into company values(2, 'Allen', 25, 'Texas', 15000.00);"
cmd3 = "insert into company values(3, 'Teddy', 23, 'Norway', 20000.00);"
cur.execute(cmd1)
cur.execute(cmd2)
cur.execute(cmd3)
print('Records created successfully')



cmd = 'update company set salary = 3300.00 where ID = 3;'
cur.execute(cmd)
conn.commit()
print('rows updated')


cmd = 'select name, id, address, salary from company;'
cur.execute(cmd)
rows = cur.fetchall()
for row in rows:
    print('ID = ', row[1])
    print('NAME = ', row[0])
    print('ADDRESS = ', row[2])
    print('SALARY = ', row[3])


cmd = 'delete from company;'
cur.execute(cmd)
conn.commit()
print('rows deleted')

conn.close()
