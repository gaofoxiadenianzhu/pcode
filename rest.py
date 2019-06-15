import requests

res = requests.get('http://www.baidu.com')
print('---text---')
print(res.text)

print('---content---')
print(res.content)

print('---url---')
print(res.url)

print('---encoding---')
print(res.encoding)

print('---status---')
print(res.status_code)
