# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:06:24 2019

@author: MUKHESH
"""

import os
import numpy as np
import pandas as pd
import zipfile
from collections import Counter
pd.options.display.max_colwidth=19000
pd.options.display.max_rows=1900
#unzipping the file and extract in specific folder
file='C:/Users/MUKHESH/Downloads/edwisor_predictive.zip'
zipf=zipfile.ZipFile(file,'r')
if(os.path.isdir('C:/Users/MUKHESH/OneDrive/Documents/Python Scripts/data01s2l1')==0):
    zipf.extractall('C:/Users/MUKHESH/OneDrive/Documents/Python Scripts')
    zipf.close()
#setting my working directory where csv file is present
os.chdir('C:/Users/MUKHESH/OneDrive/Documents/Python Scripts/data01s2l1')
#where skipping the second row with properties like header=True and seperator=',' and storing in data variable. where skiprows option will remove the secommd row
d=pd.read_csv('IMDB_data.csv',encoding = "ISO-8859-1",skiprows=[2])
print(d.head(1))
#where creating data frame  storing unique genre count.
genre_counts=pd.DataFrame(d.Genre.value_counts())
#resetting the index values and setting column names for genre_counts dataframe.
genre_counts.reset_index(inplace=True)
genre_counts.columns=['Genre','Count']
print(genre_counts.head(1))
#where creating data frame  storing unique genre count by count occurance of string.
l=d.Genre.str.split(',').map(Counter).sum()#where we use Counter object from collections module which output counter object  
genre_counts1=pd.DataFrame({'Genre':list(l),'Count':list(l.values())}) #converting counter object to list
print(genre_counts.head(1))
#converting data types where Plot,Title,Poster,imdbID converted to character and imdb rating and imdb votes converted to numeric
d.astype('object',inplace=True)
d.iloc[:,2].fillna("0",inplace=True)#where idmbvotes column as na values so filling with 0
d.iloc[:,2]=pd.to_numeric(d.iloc[:,2].str.replace(',',''), errors='coerce')
d.iloc[:,4]=pd.to_numeric(d.iloc[:,4].str.replace(',',''), errors='coerce')
#sorting the data frame according to genre
d=d.sort_values(by='Genre',ascending=True)
print(d.head(5))
#Create new variable whose values should be square of difference between imdbrating and imdbvotes.
def f(x):
    return(pow(x[2]-x[4],2))
l=d.apply(f,axis=1).tolist()