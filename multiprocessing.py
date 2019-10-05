# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:55:12 2019

@author: MUKHESH
"""

import multiprocessing
import time

def summ(a,b,value,q,lock):
    for i in range(10):
        time.sleep(1)
        c=a+b+i
        q.put(c)
        lock.acquire()
        value.value=value+1
        lock.release()
def release(a,b,value,q,lock):
    for i in range(10):
        time.sleep(1)
        c=a+b+i
        q.put(c)
        lock.acquire()
        value.value=value-1
        lock.release()
def f(n):
    return n*n;
       
if __name__=='__main__':
#    t=time.time()
#    a=2;b=3;	
#    q=multiprocessing.Queue()
#    value=multiprocessing.Value('i',2)
#    lock=multiprocessing.Lock()
#    summm=multiprocessing.Process(target=summ,args=(a,b,value,q,lock))
#    release=multiprocessing.Process(target=release,args=(a,b,value,q,lock))
#    summm.start()
#    release.start()
#    summm.join()
#    release.join()
    p=multiprocessing.Pool()
    result=p.map(f,[1,23,4,5,6])
    p.close()
    p.join()
    print(result)
#    print(value.value)
#    while q.empty() is False:
#        print(q.get())