# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:08:28 2021

@author: USER
"""
score=[]
for i in range(1,6,1):
    x=input()
    x=int(x)
    score.append(x)
print(*score)
sum=0
for i in range(0,5,1):
    sum=sum+score[i]
print(sum/5)
a=[1,2,3,4,5,]
m=0
for i in range(0,5,1,):
    if(m<score[i]):
        m=score[i]
print(m)
a=[1,2,3,4,5]
m=1000
for i in range(0,5,1,):
    if(m>score[i]):
        m=score[i]
print(m)



