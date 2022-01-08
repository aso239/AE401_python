# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:45:50 2021

@author: USER
"""
a={}
while True:
    flg=int(input("繼續1結束0列出2查詢3測驗4"))
    if flg==0:
        break
    elif flg==1:
        eng=input("請輸入英文單字")
        ch=input("請輸入中文解釋")
        a[eng]=ch
        print(a)
    elif flg==2:
        print(a)
    elif flg==3:
        eng=input("請輸入英文單字")
        if eng in a:
            a[eng]
            print(a[eng])
        else:
            print("沒有")
    elif flg==4:
        print("題目共有",len(a),"提，一提一分")
        sum=0
        for k,v in a.items():
            print("題目為",k)
            ans=input("答案")
            if v==ans:
                print("對,加1分")
                sum=sum+1
            else:
                print("答錯")
        print("總分為",sum,"分")
        