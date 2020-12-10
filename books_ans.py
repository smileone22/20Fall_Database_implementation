
import urllib, json

counts = {}
while True:
    
    base_url='http://jvers.com/csci-ua.0060-fall2020-001/data/final/books'
    extension = '.json'
    num=input('Enter a number: ')
    url = base_url + str(num) + extension
    res = urllib.requests.urlopen(url)
    raw = res.read()
    s = raw.decode('utf-8')
    parsed = json.loads(s)
    for book in parsed["data"]:
        if book["author"] in counts:
            counts[book["author"]] += 1
        else:
            counts[book["author"]] = 1
    num += 1
    if parsed["info"]["curPage"] == parsed["info"]["totalPages"]: 
        break
print(counts)  