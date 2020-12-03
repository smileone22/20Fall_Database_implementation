Class Note 11/24 

> var res=db.books.find(q,fields)
> res.next()
{ "read" : 1 }
> res.next()

var res=db.books.find(q, fields)
res.forEach(book => book.TITLE)

var res=db.books.find(q, fields)
var titles = res.map(book => book.TITLE) //map in python? list comprehenshion

titles

db.books.findOne() //first document

db.books.find().limit(2)
db.books.find().count() 
db.books.find()

//syntax for find 
find(queryObject, projection)
queryObject format > {k:valueToMatch}
projection format > {fieldName:0/1}

db.books.find({AUTHOR:'Austen, Jane'})

// if you want to see only author and title
db.books.find({AUTHOR:'Austen, Jane'},{_id:0, AUTHOR:1,TITLE:1})

db.books.find({AUTHOR:'Austen, Jane'},{_id:0, AUTHOR:1,TITLE:1}).count()
db.books.find({AUTHOR: 'Tolstoy, Leo'},{_id:0, YEAR_WRITTEN:1}).count()

//count
db.books.find({},{_id:0,AUTHOR:1,TITLE:1,YEAR_WRITTEN:1}).count()

//sort with two cols
db.books.find({},{_id:0,AUTHOR:1,TITLE:1,YEAR_WRITTEN:1}).sort({YEAR_WRITTEN:1 , AUTHOR:1})

//1870 greater than
var q={YEAR_WRITTEN:{$gt:1870}}
var proj= {_id:0,YEAR_WRITTEN:1,AUTHOR:1,TITLE:1}
db.books.find(q,proj)

//AND for query queryObject - simply by adding more to our query queryObject
var q={YEAR_WRITTEN:{$gt:1870}, AUTHOR: 'Woolf, Virginia'}

//OR for query queryObject
// {$or: [{k1:v1},{...}]} 
var q={$or: [{YEAR_WRITTEN:{$gt:1870}},{AUTHOR: 'Tolstoy, Leo'}]}

//find returns cursor and you can call methods on that such as 
//.count 
//.limit
//.sort

db.collectionName.insert({})

db.collectionName.remove({})

db.collectionName.drop() //drop collection 


similar to query 
----------------------------------------------------------------
 db.jobs.distinct('Full-Time/Part-Time indicator')

 db.jobs.distinct('agency')

 db.jobs.find({Agency:'POLICE DEPARTMENT'},{_id:0,"Job ID":1,"Business Title":1,"Agency":1}).sort({'Job ID':1})


// ONLY show job id, business title, posting date,and salary RangeTo

var orderBy = {'Salary Range To':-1}
var proj = {'Job ID':1, 'Business Title':1, 'Salary Range To':1}
db.jobs.find({},proj).sort(orderBy).limit(20)

----------------------------------------------------------------
group by- aggregate

.aggregate([{$match: ...},{$group: },{}])
