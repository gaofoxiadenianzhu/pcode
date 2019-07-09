import  happybase

pool = happybase.ConnectionPool(size = 3, host='127.0.0.1')

conn = None

with pool.connection() as connection:
    conn = connection

print( conn.tables() )

tbl = conn.table('my_table')

'''
conn.create_table( 'my_table',
      {
        'cf1': dict(max_versions=10),
        'cf2': dict(max_versions=1, block_cache_enabled=False),
        'cf3': dict()
      }
)
'''
'''
cloth_data={'cf1:content':'niuzaiku', 'cf1:price':'299', 'cf1:rating':'98%'}
tbl.put(row='www.test1.com',data=cloth_data)

bat = tbl.batch()
bat.put('www.test5.com',{'cf1:price':'999', 'cf2:title':'Hello Python', 'cf2:length':'34', 'cf3:code':'A43'})
bat.put('www.test6.com',{'cf1:content':'tixudao','cf1:price':'168', 'cf1:rating':'97%'})
bat.put('www.test7.com',{'cf3:function':'print'})
bat.send()
'''

for key, value in tbl.scan():
    print(key, value)

print('--------------')

row = tbl.row('www.test6.com')
print(row)

print('--------------')

rows = tbl.rows(['www.test1.com', 'www.test8.com', 'www.test7.com'], columns=['cf1'])
print(rows)

tbl.delete('www.test1.com')
print('---------------')


for key, value in tbl.scan():
    print(key, value)
