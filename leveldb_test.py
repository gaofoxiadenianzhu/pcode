import leveldb
import datetime

def show(db):
    for k in db.RangeIter(include_value = False):
        print(db.Get(k))

db = leveldb.LevelDB('/var/leveldb/data')

'''
db.Put(b'foo', b'dongsheng')
print(db.Get(b'foo'))
db.Delete(b'foo')
#print(db.Get(b'foo'))

bat = leveldb.WriteBatch()
bat.Put(b'panll', b'11')
bat.Put(b'cll', b'22')
bat.Put(b'panh', b'33')
bat.Put(b'zhoum', b'44')
db.Write(bat)

show(db)

db.Put(b'apple', b'pingguo')
s1 = db.CreateSnapshot()
db.Put(b'apple', b'juzi')
s2 = db.CreateSnapshot()

print('-------')
print(db.Get(b'apple'))
print(s1.Get(b'apple'))
print(s2.Get(b'apple'))
'''
print('---write begin---')

dt1 = datetime.datetime.now()

data = 1
for x in range(10):
    bt = leveldb.WriteBatch()
    for i in range(1000):
        s = 'a%d'%data
        db.Put( bytes(s,'ascii'), str(data).encode('utf-8'))
        data += 1
    db.Write(bt)



dt2 = datetime.datetime.now()

span = dt2- dt1
print('span %d seconds'%(span.total_seconds()))

print('---write end---')

#print(db.Get(bytes(5000)))
