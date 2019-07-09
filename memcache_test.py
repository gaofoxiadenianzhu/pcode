import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
k1 = 'things'
v1 = 'yuxing'
k2 = 'vsl'
v2 = 'zhangfan'
mc.set(k1, v1)
mc.set(k2, v2)
d1 = mc.get(k1)
d2 = mc.get(k2)
print('%s, %s'%(k1, v1))
print('%s, %s'%(k2, v2))
mc.delete(k1)
mc.delete(k2)
mc.set('apple', 111)
mc.set('orange', 222)
mc.set('pear', 333)

