# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:41:12 2019

@author: MUKHESH
"""

from bs4 import BeautifulSoup
import requests
from PIL  import Image
from io import BytesIO
import os


while True:
    search=input('Enter which item to search:')
    if(search=='quit'):
        print('existing searching')
        break
    params={'q':search}
#r=requests.get('https://www.google.com/search',params)
    if os.path.isdir(search)==False:
        os.mkdir(search)
    r=requests.get('https://www.google.com/images',params)
#print(r.text)
#with open('./path2.html','w+',encoding='utf-8') as fd: 
#    fd=open('./path2.html','w+')  
#    fd.write(r.text)
    soup=BeautifulSoup(r.text,'html.parser')
#print(soup.prettify)
#results=soup.findAll('div',{'class':'g'})
#print(results)
#for result in results:
#    item=result.find('a').text
#    item1=result.find('a').attrs['href'].split('=')
#    print(item,"\n",item1[1])
    results=soup.findAll('a')
    print(results)
    i=0
    for result in results:
   # print('\n',type(result),'\n')
        if result.find('img')==None:
            continue
        else:
            item=result.find('img')['src']
    
        q=requests.get(item)
        title=result.find('img').attrs['src'].split(':')[-1]
        image=Image.open(BytesIO(q.content))
        path='path'+str(i)+'.'+image.format
        image.save('./'+search+'/'+title+'.jpeg',image.format)
        i+=1
#for result in results:
#    q=requests.get(result.find('img').attrs['src'])
#    
#    title=result.find('img').attrs['src'].split('/')[-1]
#    image=Image.open(BytesIO(q.content))
#    path='path'+str(i)+'.'+image.format
#    image.save('./'+title,image.format)
#    i+=1