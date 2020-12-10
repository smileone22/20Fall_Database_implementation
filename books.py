
import urllib.request, json
import requests

total = int(input(" Enter total pages: "))


for i in range(1, total+1):
    n=i 
    url= f'http://jvers.com/csci-ua.0060-fall2020-001/data/final/books{n}.json'
    r = requests.get(url)
    js = json.loads(r.content.decode())
    print(js['info'])
    print(js['data'])