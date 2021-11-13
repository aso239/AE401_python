# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:31:00 2021

@author: USER
"""
import random
num=random.randint(1,20)
l = 1 
while (l<=5):
    user=input()
    user=int(user)
    if user<num:
        print("太小了")
    elif user>num:
        print("太大了")
    else:
        print("答對了")
        print(l)
    l = l+1
