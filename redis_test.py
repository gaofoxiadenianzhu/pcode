#coding:utf-8

import redis

# r = redis.Redis(host='127.0.0.1', port=6379)

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

print('foo = %s'%r.get('foo'))
print('fire = %s'%r.get('fire'))

r.set('foo', 'Bar')
print( r.get('foo'))

r.setnx('foo', 'Bar2')
print(r.get('foo'))

r.setex('fire',10,'888')
print('fire = %s'%r.get('fire'))

r.set('count', 1)
print('count = %s'%r.get('count'))
print('count = %s'%r.incr('count'))
print('count = %s'%r.incr('count'))
r.delete('count')
print('count = %s'%r.get('count'))

r.hset('name:age', 'panll', 38)
r.hset('name:age', 'panj', 41)
r.hset('name:age', 'chenll', 38)
r.hset('name:age', 'panh', 9)
print(r.hgetall('name:age'))
print('chenll = %s'%r.hget('name:age', 'chenll'))

r.delete('names')
r.rpush('names', 'lvbin')
r.rpush('names','wangwenjun')
r.rpush('names','lihuiwen')
r.rpush('names','zhangfan')
r.rpush('names','yexinde')
r.save()
print('names = ')
lenth = r.llen('names')
index = 0
while index < lenth :
    print(r.lindex('names', index))
    index += 1
