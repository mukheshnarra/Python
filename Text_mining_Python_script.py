# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 01:11:34 2019

@author: MUKHESH
"""

import re

#assigning the text varibale with sample text
text='This is a simple way to outline the essential reasons for taking or defending a position. Make a list of answers that satisfy the question around which your position is focused. For instance, a list of "bcz" statements for the claim "Grades should be abolished in non-major courses"'
#replacing the bcz with because
new_text=re.sub(r'bcz','because',text)
#printing the new text
#print(new_text)


#another method
short_words={'bcz':'because','ur':'there'}
text='This is a simple way to outline the essential reasons for taking or defending a position. Make a list of answers that satisfy the question around which your position is focused. For instance, a list of bcz statements for the claim "Grades should be abolished in non-major courses"'
#written a function to replace the shortkey words
def remove_short_words(text):
    text_list=[]
    for i in text.split():
        if list(short_words.keys()).count(i)>0:#checking the words is present in dictionary key
            i=short_words[i]#if present then replace with the actual word
        text_list.append(i)
    return ' '.join(text_list)

text=remove_short_words(text)#calling the function
print(text)#printing the text
