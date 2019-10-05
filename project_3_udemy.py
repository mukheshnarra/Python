# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:17:20 2019

@author: MUKHESH
"""

import requests
import simplejson as js
from PIL import Image
from io import BytesIO

search={'q':'pizza'}
#r=requests.get('https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg?output-quality=60&resize=1000:*')
##print(r.url)
##print(r.status_code)
##read=open('./path1.html','w+')
##read.write(r.text)
#image=Image.open(BytesIO(r.content))
#
#print(image.size,image.format,image.mode)
#path='./image1.png'
#try:
#    image.save(path,'png')
#except IOError:
#    print('Cannot Save Image')
#param={'q':'pizza'}
#r=requests.post('https://www.google.com/search',params=param,header=)
json={'longurl':'https://www.example.com'}
headers={'Content-Type':'application/json'}
r=requests.post('https://www.googleapis.com/urlshortener/v1/url',json=json,headers=headers)
print(js.loads(r.text)['error']['message'])
print(r.headers)