# Mongo basics exercise 

## Sorting 
* sort by author, then title
db.books.find({},{_id:0,'AUTHOR':1,'TITLE':1}).sort({'AUTHOR':1,'TITLE':1})

* how about by year ascending/ descending ?
db.books.find({},{_id:0,'AUTHOR':1,'TITLE':1,'YEAR_WRITTEN':1}).sort({'YEAR_WRITTEN':1})
db.books.find({},{_id:0,'AUTHOR':1,'TITLE':1,'YEAR_WRITTEN':1}).sort({'YEAR_WRITTEN':-1})

## Comparisons
* $lt - less than 
* $lte - less than or equal
* $gt - greater than 
* *gte - greater than or equal

* find all books written after 1870 
db.books.find({'YEAR_WRITTEN':{$gt:1870}},{_id:0})

* how about 1870 and 1900 (inclusive) 
db.books.find( {"YEAR_WRITTEN":{$gte:1870, $lte: 1900}},{ _id:0} )

* …and sort the result by author
db.books.find( {"YEAR_WRITTEN":{$gte:1870, $lte: 1900}},{ _id:0} ).sort({'AUTHOR':1})

* anything written exactly in 1870
db.books.find({"YEAR_WRITTEN":1870},{ _id:0})

## Operators 
* books that cost $15 or more… or after 1899
var f = {"$or":[ {"PRICE":{"$gte":15}},{"YEAR_WRITTEN":{"$gt":1899}}]}
var p ={_id:0}
db.books.find(f,p)

* Show the title, author and year of all books written after 1870 by either Tolstoy or Woolf
// using $or 
var f = {"YEAR_WRITTEN":{"$gt":1870}, "$or":[ {"AUTHOR":/Woolf/},{"AUTHOR":/Tolstoy/} ] }
var p = {_id:0,"TITLE":1,"AUTHOR":1,"YEAR_WRITTEN":1}
db.books.find(f,p)
// using $in 
var f = {"YEAR_WRITTEN":{"$gt":1870}, "AUTHOR":{$in: [ /Tolstoy/,/Woolf/]} }
var p = {_id:0,"TITLE":1,"AUTHOR":1,"YEAR_WRITTEN":1}
db.books.find(f,p)

## Xtra: $group > db.collection_name.aggregate([])

db.books.aggregate[ {$group : {_id: "$YEAR_WRITTEN", books: {$push: "$TITLE"}}}]

db.books.aggregate([ {$group: {_id: "$PRICE", books:{$push:"$TITLE"}}}])

db.books.aggregate(
	[{$group : {
		_id: "$YEAR_WRITTEN", 
		books: {$push: "$TITLE"}, 
		price: {$avg: "$PRICE"}
	}}]
)