import pymysql

conn = pymysql.connect( host = '127.0.0.1', user = 'root', password = 'root', db = 'test' )
cursor = conn.cursor()

#
sql3 = "update person set age = 4 where name = 'weiyi'"
cursor.execute(sql3)
conn.commit()
#
sql = 'select * from person'

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print('unable to fetch data')


'''
sql2 = "insert into person(name,age,female) values('weiyi',3,1)"
cursor.execute(sql2)
conn.commit()
'''

conn.close()
