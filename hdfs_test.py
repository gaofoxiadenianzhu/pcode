import sys
import time
from hdfs import InsecureClient

def append_to_hdfs(client, hdfs_path, data):
    client.write(hdfs_path, data, overwrite=False, append=True, encoding='utf-8')

client =InsecureClient("http://172.16.245.229:50070", user='root')
print('connect ok')
#client.makedirs('/user/root/xxx')
#print('mkdir ok')
data = client.list('/')
print(data)

fpath = '/aaa.txt'
print('append to file = %s'%(fpath))
data = 1
#COUNT = 1728000
while True:
    strdata = '++++++++++++++++++++++++++++++++hello, world++++++++++++++++++++++++++++++ %d \n\n\n\n\n\n\n\n'%(data)
    data += 1
    append_to_hdfs(client, fpath, strdata)
    time.sleep(1)
print('append to hdfs over!')

