
* 12_09 Notes

topics 
- db design, er diagrams
- normalization
- api (json) ex.tumblr
- scraping data
- cursor, pysql
- mongodb (crud, aggreagation, embedd vs reference, cardinality)


* HTML Parsing 
1. locate your data within the markup
    - download the page <-- open with a text editor (notepad, textedit, sublime, atom, spyder, pycharm)
    - inspect , view source
2. When you find data what next?
    - look for 
        - tag name > tagName
        - class name > .className
        - id  > #id
        - relationship between tages ( embedded in another?)
    - try example of popular baby names 
    
* mongoDB 
document oriented 
$match, $group, $project, $sort

* pymysql
import pymysql
con = pymysql.connect(username='sdfs', password='sfds')
cur = con.cursor()
cur.execute()

q... don't concatenate 
( select * from t where i_id = ' + userinput' )
f'select ... {user_input}'

cur.execute(q)
cur.execute('select * from where t_id = %s', (user_input, ))

for row in cur <- select 
cur.commit() <-- when you insert or update 

* embedded vs reference 
embedded        vs      reference (link) 

insert anomolies               
redundancy 
faster 