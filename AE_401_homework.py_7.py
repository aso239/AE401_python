# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:08:28 2021

@author: USER
"""
score = [["a",100],["b",99],["c",88]]
m=9999999
m_index=0
for i in range(0,3,1):
    if(m>score[i][1]):
        m_index=i
        m=score[i][1]
print(score[m_index][0],m)
m=0
m_index=0
for i in range(0,3,1):
    if(m<score[i][1]):
        m_index=i
        m=score[i][1]
print(score[m_index][0],m)



