# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:37:04 2019

@author: MUKHESH
"""

#import re
# 
#string='"hello" hi im waiting'
##s=re.sub('[\b]',"",string)
##print(s)
#li=[s.strip("\"") for s in string.split(" ")]
#print(li)

import re

previous=0
run=True

def perform_math():
    global previous
    global run
    if previous==0:
        equation=input('enter equation:')
    else:
        equation=input(str(previous))
    if equation.lower()=='clear':
        previous=0
        return
    else:
        if equation.upper()=='QUIT':
            run=False
        else:
            equation=re.sub('[a-zA-Z.," "\"\']',"",equation)
            if previous is 0:
                previous=eval(equation)
            else:
                previous=eval(str(previous)+equation)
                          
perform_math.__doc__="doing the calucaltion"
while run:
    perform_math()
print(perform_math.__doc__)