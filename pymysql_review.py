import pymysql

conn = pymysql.connect(database="hk2874_test", user="hk2874", password="c3wnhbuv", host="warehouse.cims.nyu.edu")
cur = conn.cursor()

q = """
SELECT * 
FROM artist 
WHERE nationality = 'American' 
	AND gender = 'Female' 
	AND name ilike 'Z%';
"""
cur.execute(q);

for res in cur:
    print(res)