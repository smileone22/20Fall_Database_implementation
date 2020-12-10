from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL="https://www.babynames.com/blogs/names-blog/100-trending-names-of-2020/"

res=urlopen(baseURL)
raw_data=res.read()
# raw_data.decode('utf-8')
soup = BeautifulSoup(raw_data,'html.parser')
#print(soup)

rows= soup.select('.namos tr')
for row in rows:
    tds =row.find_all('td')
    rank = tds[0].get_text()
    b_name = tds[1].get_text()
    g_name = tds[2].get_text()
    print(rank, b_name,g_name,"\n------")
