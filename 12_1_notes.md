# 12_1 Class Notes

db.jobs.find().count() 
db.jobs.count()

* One document
db.jobs.findOne() 

* Distinct 
db.jobs.distinct("Full-Time/Part-Time indicator")
db.jobs.distinct("Agency") 

* First three documents ordered job id
var proj = {"Job Description":0, _id:0}
db.jobs.find({},proj).sort({"Job ID":1}).limit(3).pretty()

* no data , schema in mongodb

* You can't mix positionanl arugments and option arguments

* /---/i 
db.jobs.find({"Business Title": /people/i})

db.jobs.find({"Business Title": /people/i})

var proj={"Job ID":1,"Business Title":1,"Salary Range To":1,_id:0}

db.jobs.find({},proj).sort({"Salary Range To":-1}).limit(20)

---------------------------------------
# AGGREGATION 

* aggregation pipeline is a multi-stage process that transforms docs to aggregated result 
- output of one stage becomes input for the next stage

* FORMAT: db.collectionName.aggregate([match, project, match, group, limit ...])

* $match - filter documents
    - acts like find query
    - similar to having and where in sql
    var matchA ={$match: {Agency:"POLICE DEPARTMENT"}}
    
    db.jobs.aggregate([matchA])

* $count - count ( x in i6)

* $project - to calculate or select fields
    - rename and calculate fields
    var fields = {$project: {"Job ID":1, _id:0, "Business Title":1,"Salary Range To":1}}
    db.jobs.aggregate([matchA, fields])

    db.jobs.aggregate([fields, matchA]) // nothing back, order sensitive

* $group 
* $addFields
* $bucket
 - $ means value at that field 
 - firstName : value as a string 
 - $firstName: eva, bruce etc 

 var division = {$divide : ["$Salary Range To",1000]}
 var fields = {$project: {"Job ID":1, _id:0, "Business Title":1,maxSalary:division}}
db.jobs.aggregate([matchA,fields])

var fields = {$project: {"Job ID":1, _id:0, title: {$toUpper: "$Business Title"},maxSalary:division}}
db.jobs.aggregate([matchA,fields])

var groupBy = {$group: {_id:"$Agency" , countListings:{$sum: 1}}}

db.jobs.aggregate([groupBy, {$sort: {"countListings":-1}}])

var groupBy = {_id :'$Agency',avgTo:{$avg: '$Salary Range To'}}
var orderBy = {avgTo:-1}
db.jobs.aggregate([{$group: groupBy},{$sort:orderBy}])

$sum,$avg,$max,$last,$push (it adds everything to the list)
-------------------------------------------------
Database Design from mongodb
-------------------------------------------------
From RHDBMS
- to reduce insert, update and delete anomalies
- extend or expend the database within minimum impact on existing design
- in general, make the database easier to understand 
-------------------------------------------------
From MONGOdb
- want documents to be related to each together but we don't have foreign keys
- You could have embedding (single document with sub documents inside it) or linking (kind of like linked list) 

