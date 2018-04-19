# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:56:50 2018

@author: 猪猪
"""
import random
opr = ['＋','－','×','÷']      #四则运算的选择
jg = '0'
print('输入 "0000" 可退出')
while True:
    fh = random.randint(0, 3) #fh可取0,1,2,3
    n1 = random.randint(1, 10) #n1为1~10范围内的数
    n2 = random.randint(1, 10) #n2为1~10范围内的数
    rjg = 0
    if fh == 0:  #加法
        rjg = n1 + n2
    elif fh == 1: #减法
        n1,n2 = max(n1,n2),min(n1,n2) #因为不能出现负数 所以用大的值减去小的值
        rjg = n1 - n2
    elif fh == 2:#乘法
        rjg = n1 * n2
    elif fh == 3:#除法
        n1,n2 = max(n1,n2),min(n1,n2)
        while n1 % n2 != 0:#只考虑整除的情况
            n1 = random.randint(1, 10)
            n2 = random.randint(1, 10)
            n1,n2 = max(n1,n2),min(n1,n2)#保证用大的数除以小的数
        rjg = int(n1 / n2)
 
    print(n1, opr[fh], n2, '= ', end='')#输出题目
    jg = input()#输入答案
    if jg == '0000':#输入0000 意为退出
        break
    sr = int(jg)
    if int(sr) == rjg:#如果输入答案与正确答案相等 则输出 正确
        print('正确')
    else:
        print('错误，正确答案为：', rjg)