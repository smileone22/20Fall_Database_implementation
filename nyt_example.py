import requests
import json 
res = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=TODO&api-key=TODO')

data = res.json()
docs = data['response']['docs']
for doc in docs:
    print(doc['headline']['main'])
    print(docs[0].keys())
    print(len(docs))