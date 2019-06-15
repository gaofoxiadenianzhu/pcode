from elasticsearch2 import Elasticsearch
import time

es = Elasticsearch([{'host':'127.0.0.1','port':9200}], timeout=3600)

es.indices.delete(index='news', ignore=[400,404])
es.indices.create(index='news', ignore=400)

data = {'title':'mei guo liu gei yi la ke de shi ge lan tan zi ma', 'url':'http://www.sina.com', 'date':'2011-12-16'}

result = es.index(index='news', doc_type='sss', body=data, id = 1)
print(result)

data2 = {'title':'aaa', 'url':'bbb', 'date':'2019-08-16'}
result = es.index(index='news', doc_type='sss', body=data2, id = 2)
print(result)

data3 = {'title':'zhong hua ren ming gong', 'url':'http://www.baidu.com.cn', 'date':'2008-10-26'}
result = es.index(index='news', doc_type='sss', body=data3, id = 3)
print(result)

#doc = {'query': {'range':{'date': {'gt':'2011-12-16'}}}}
#query = {'query': {'match_all':{}}}
#result = es.search(index='news', body=doc)

print('sleep some seconds...')
time.sleep(2)

query2 = {"query":{"bool":{"must":[{"query_string":{"default_field":"title","query":"hua"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}
result = es.search(index='news', body=query2)
print(result)
