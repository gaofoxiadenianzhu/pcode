from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
print('create and connect mydb...')
db = conn.mydb
myset = db.myset

print('insert one...')
student = {'id':'20170101',
           'name':'Jordan',
           'age':20,
           'gender':'male'
          }

result = myset.insert_one(student)
print(result)
print(result.inserted_id)


print('insert many...')
student2 = { 'id' : '20170102',
             'name': 'Jack',
             'age': 23,
             'gender':'female'
           }

student3 = { 'id' : '20170202',
             'name': 'Mike',
             'age': 21,
             'gender': 'make'
           }

result = myset.insert_many([student2, student3])
print(result)
print(result.inserted_ids)

print('find one...')
result = myset.find_one({'name':'Mike'})
print(type(result))
print(result)

print('find...')
results = myset.find({'age':{'$gt':20}})
print(results)
for result in results:
    print(result)



print('update...')
condition = {'name':'Jack'}
student = myset.find_one(condition)
student['age'] = 20
result = myset.update(condition, student)
print(result)


print('delete...')
result = myset.delete_many({'age':{'$lt':60}})
print(result.deleted_count)

print('test mongodb over...')
print('hello,mongodb...')
print('just a joke...')
