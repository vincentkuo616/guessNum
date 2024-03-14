# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:44:04 2024

@author: vincentkuo
"""

# -*- coding: utf-8 -*-
import random
ANDONE = False
def numStr(num):
    numArray = ['一','二','三','四','五','六','七','八','九']
    return numArray[num-1]
    
def main(num):
    ST=[]
    t=0
    while t<num :
        tem=str(random.randrange(0,10))
        if not (tem in ST):
            ST.append(tem)
            t+=1
    num_zh = numStr(num)
    #宣告一個ST,存放亂數產生要猜的一組不重覆的四位數
    time=1
    while True:
        if time==1:
            print(u"請輸入一個不重覆的",num_zh,"位數字或輸入'STOP'以退出遊戲:")
        A=0
        B=0
        input_s=input()
        if "STOP" in input_s.upper():
            print(u"離開遊戲! 正確答案為 %s" % "".join(str(n) for n in ST))
            break
        elif "QWER" in input_s.upper():
            try:
                num = int(input_s[-1])
                main(num)
                break
            except:
                print(u"錯誤! 輸入錯誤的個數")
        else:
            try:
                int(input_s)    #測試是否輸入的為數字,若非會產生列外處理
                if "".join(str(n) for n in ST)==input_s: #猜到數字,結束遊戲
                    print(u"Good Job!! 共猜了 %d 次" %time)
                    return input_s
                    break
                elif len(input_s) != num:
                    print(u"錯誤! 不正確的長度!\n")
                elif len(set(input_s)) != num:
                    print(u"錯誤! 內含重複的數字!\n")
                else:   #未猜到,計算與目標數字的差異
                    for tem in range(num):
                        if ST[tem] == input_s[tem]: #包括、且位置相符
                            A+=1
                        if input_s[tem] in ST:  #計算包括的數字,所以需再減去A的總合,才是僅包括,但位置不同的數量
                            B+=1
                    print("%d A\t%d B" % (A,B-A))
                    time+=1
            except:
                print(u"錯誤! 內含非數字的字串\n")

def nAnB(num,ans,guess):
    A,B=0,0
    if ans==guess: #猜到數字,結束遊戲
        return 4,0
    elif len(guess) != num:
        print(u"錯誤! 不正確的長度!\n")
    else:   #未猜到,計算與目標數字的差異
        for tem in range(num):
            guess=str(guess)
            ST = ans
            if ST[tem] == guess[tem]: #包括、且位置相符
                A+=1
            if guess[tem] in ST:  #計算包括的數字,所以需再減去A的總合,才是僅包括,但位置不同的數量
                B+=1
        return str(A)+str(B-A)

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

def guess(num,ans_list,st,answer):
    guess = nAnB(num,answer,st)
    try:
        a = int(guess[0])
        b = int(guess[1])
        temp_list = ans_list
        temp_st = st

        maybeAns = checkAns(temp_list,a,b,temp_st)
        #print(maybeAns)
        if a==int(num):
            print(u"恭喜猜對囉!!")
            return 1,[],temp_st
        elif len(maybeAns)==1:
            print(u"答案只能是",maybeAns[0],"了")
            global ANDONE
            ANDONE = True
            return 1,[],temp_st
        else:
            ans = random.sample(maybeAns, 1)
            print(u"再猜一次 是......",ans[0],"嗎?")
            temp_st = ans[0]
            return num,maybeAns,temp_st
            #break    
    except:
            print(u"錯誤!!輸入非數值之數")

num = 4
ans = main(4)
ST=[]
st=""
t=0
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
#print(ans_list)

while t<int(num) :
    tem=str(random.randrange(0,9))
    if not (tem in ST):
        ST.append(tem)
        t+=1
for i in range(0,len(ST)):
    st+=str(ST[i])
print(u"請問是",st,"嗎?")

ans_list.remove(st)

try:
    switch,time=0,0
    while switch<1:
        rt_num,rt_list,rt_st = guess(num,ans_list,st,ans)
        num=rt_num
        ans_list=rt_list
        st=rt_st
        time+=1
        if ANDONE:  time+=1
        if rt_num==1:
            print(u"Good Job!! 共猜了 %d 次" %time)
            break
except:
    print(u"程式掛了 工程師上班囉!!")

