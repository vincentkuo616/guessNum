# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:42:12 2019

@author: vincentkuo
"""

#import random
from collections import Counter

def numStr(num):
    numArray = ['一','二','三','四','五','六','七','八','九']
    return numArray[num-1]

def checkAns(ans_list,a,b,st):
    maybeAns = []
    list_st = list(st)
    for ans in ans_list:
        A,B = 0,0
        for i in range(0,len(st)):
            if ans[i]==st[i]:
                A+=1
            if ans[i] in list_st:
                B+=1
        #print(A,a,B,b)
        #print(type(A),type(a),type(B),type(b))
        if (a==A) and (b==(B-A)):
            maybeAns.append(ans)

    return maybeAns

def guess(num,ans_list,st):
    print(u"答案是幾A幾B?")
    guess = input()
    try:
        a = int(guess[0])
        b = int(guess[1])
        temp_list = ans_list
        temp_st = st

        maybeAns = checkAns(temp_list,a,b,temp_st)
        #print(maybeAns)
        if len(maybeAns)==1:
            print(u"答案只能是",maybeAns[0],"了")
            return 1,[],temp_st
        elif a==int(num):
            print(u"恭喜猜對囉!!")
            return 1,[],temp_st
        else:
            return num,maybeAns,temp_st
            #break    
    except:
            print(u"錯誤!!輸入非數值之數")
            
def anslist(num):
    try:
        ans_list = []
        for i in range(10**(int(num)-2),10**(int(num)-1)):
            st_i = str(i)
            list_i = []
            for j in range(0,len(st_i)):
                list_i.append(st_i[j])
            if len(list_i)==len(set(list_i)) and list_i[0]!="0" and list_i[1]!="0" and list_i[2]!="0":
                ans_list.append("0"+str(i))
        for i in range(10**(int(num)-1),10**int(num)):
            st_i = str(i)
            list_i = []
            for j in range(0,len(st_i)):
                list_i.append(st_i[j])
            if len(list_i)==len(set(list_i)):
                ans_list.append(str(i))
        return ans_list
    except:
        print(u"Something Wrong while creating answer list.")

print(u"請問是猜幾位數 且數字不能重複?")
num = input()
ans_list = anslist(num)
possible_list=[]
try:
    switch=0
    while switch<1:
        
        print(u"你猜了什麼?")
        st = input()
        ans_list.remove(st)
        rt_num,rt_list,rt_st = guess(num,ans_list,st)
        num=rt_num
        possible_list.extend(rt_list)
        #possible_list = rt_list
        result = Counter(possible_list)
        print(result.most_common(8))
        st=rt_st
        if rt_num==1:
            break
        if result.most_common(2)[0][1]>result.most_common(2)[1][1]:
            print(u"答案只能是",result.most_common(2)[0][0],"了")
            break
except:
    print(u"程式掛了 工程師上班囉!!")