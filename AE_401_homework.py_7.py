# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:08:28 2021

@author: USER
"""
name = [["a",100],["b",99],["c",88],["d",77],["e",66]]
sum=0
for i in range(1,10,2):
    sum=sum+name[i]
print(sum/5)
m=0
max_k=0
small_k=0
for i in range(1,10,2):
    if(m<name[i]):
        m=name[i]
        max_k=i
print(name[max_k-1])
print(m)
for i in range(1,10,2):
    if(m>name[i]):
        m=name[i]
        small_k=i
print(name[small_k-1])
print(m)



