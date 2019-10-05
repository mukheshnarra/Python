# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:02:10 2019

@author: MUKHESH
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,KFold,cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from matplotlib import pyplot as plt
iris=load_iris()
#print(dir(iris))

data=pd.DataFrame(iris.data,columns=iris.feature_names)
#print(data.head())
data['target']=iris.target
#plt.scatter()
d1=data.drop('target',axis='columns')
#print(d1.head())
d2=data['target']
#X_train,X_test,Y_train,Y_test=train_test_split(d1,d2,test_size=0.4)
#classifier=SVC()
#classifier.fit(X_train,Y_train)
#print(classifier.score(X_test,Y_test))
kf=KFold(n_splits=4)
def model_score(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)
    return model.score(x_test,y_test)
    
for train_index,test_index in kf.split(iris.data):
    x_train,x_test,y_train,y_test=iris.data[train_index],iris.data[test_index],iris.target[train_index],iris.target[test_index]
    print( model_score(SVC(gamma=0.4),x_train,x_test,y_train,y_test))
    print(model_score(LogisticRegression(),x_train,x_test,y_train,y_test))
    print(model_score(RandomForestClassifier(),x_train,x_test,y_train,y_test))
       