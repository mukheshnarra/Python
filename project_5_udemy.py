# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:46:43 2019

@author: MUKHESH
"""
import datetime
import pymongo
from pymongo import MongoClient
#MongoClient('mongo://localhost:27017/')
client=MongoClient()
db=client['mydatabase']
users=db.users
user={'name':'mukhesh','id':907,'income':385000}
user1={'name':'sthita','id':908,'income':385000}
#user_id=users.insert_many([user,user1]).inserted_ids
#print(user_id)
#print(list(users.find({'id':{'$lte':907}},{'name':'mukhesh'}).sort('name')))
#index=users.create_index([('id',pymongo.ASCENDING)],unique=True)
#print(users.index_information())
#cars=users.find({},{'_id':1,'name':1})
#agr=[{'$group':{'_id':1,'all':{'$sum':'$income'}}}]
#car=users.aggregate(agr)
#print(list(car))
#for car in cars:
#    print(car)
    #print('{0} {1}'.format(car['name'],car['id']))
    
#date=datetime.datetime.now()   
#insertedid=users.update_many({'id':{'$gte':907}},{'$set':{'Date':date}})
b=users.find()
for bi in b:
    print("{0}->{1}->{2}".format(bi['name'],bi['id'],bi['Date'],bi['income']))