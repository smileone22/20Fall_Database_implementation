
import urllib.request, json
tag = 'cat'
api_key = 'XBu4Lke6Cyh2UrLFIZW0jIo79sUT8EwtruJduMAknEUNhccNwY'
domain = 'api.tumblr.com'
url = f'http://{domain}/v2/tagged?api_key={api_key}&tag={tag}'
print(url)
res = urllib.request.urlopen(url).read().decode('utf-8')
posts = json.loads(res)['response']
extract_url = lambda p: p['photos'][0]['original_size']['url']
filter_posts =  lambda p: p['type'] == "photo" and len(p['tags']) > 2
filtered = [extract_url(p) for p in posts if filter_posts(p)]
print(filtered)