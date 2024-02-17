# -*- coding: utf-8 -*-
import random
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
                
main(4)