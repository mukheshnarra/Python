# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:35:37 2019

@author: MUKHESH
"""
import os
import simplejson as js

path='./path1.json'
if os.path.isfile(path) and os.stat(path).st_size!=0:        
    r=open(path,'r+')
    data=js.loads(r.read())
    print('the age is ',data['age'])
    data['age']=data['age']+1

else:
    r=open(path,'w+')
    data=[]
    data.append({'name':'mukhesh','age':22})
    data.append({'name':'stita','age':23})
   

r.seek(0)
r.write(js.dumps(data[0]))
r.write(js.dumps(data[1]))  