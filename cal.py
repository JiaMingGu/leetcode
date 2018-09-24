# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:38:38 2018

@author: Ming Gu
"""
import math
#计算壳体厚度专用
def Cal_siim(h,r,l=0.5,kind=0,n=1.5):
    #h为深度,单位为m
    
    #r为内径（半径）单位为mm
    
    #l为壳体长度单位为m
    
    #kind为类型：
    #0: 不指定材料类型
    #1：304
    #2：TC4
    #3: 316
    
    #n为安全系数，默认为1.5
    
    #rtype:int 外径
    pi=3.1415926
    p=10*h/1000
    if kind==0:
        g1=205/n
        g2=824/n
        g3=205/(n+0.5)
        R1=r/(1-2*p/g1)**0.5+2
        R2=r/(1-2*p/g2)**0.5+2
        R3=r/(1-2*p/g3)**0.5+2
        m1=7.93*pi*(math.ceil(R1)**2-r**2)/1000*l
        m2=4.4*pi*(math.ceil(R2)**2-r**2)/1000*l
        m3=7.98*pi*(math.ceil(R3)**2-r**2)/1000*l
        h1=(1-(r/math.ceil(R1))**2)*g1*50
        h2=(1-(r/math.ceil(R2))**2)*g2*50
        h3=(1-(r/math.ceil(R3))**2)*g3*50
        print('304此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R1)-r,m1,h1))
        print('TC4此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R2)-r,m2,h2))
        print('316此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R3)-r,m3,h3))
        return 0
    if kind==1:
        g=205/n;
        R=r/(1-2*p/g)**0.5+2
        m1=7.93*pi*(math.ceil(R)**2-r**2)/1000*l
        h1=(1-(r/math.ceil(R))**2)*g*50
        print('304此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R)-r,m1,h1))
        return 0
    if kind==2:
        g=824/n;
        R=r/(1-2*p/g)**0.5+2
        m2=4.4*pi*(math.ceil(R)**2-r**2)/1000*l
        h2=(1-(r/math.ceil(R))**2)*g*50
        print('TC4此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R2)-r,m2,h2))
        return 0
    if kind==3:
        g=205/(n+0.5);
        R=r/(1-2*p/g)**0.5+2
        m3=7.98*pi*(math.ceil(R)**2-r**2)/1000*l
        h3=(1-(r/math.ceil(R))**2)*g*50
        print('316此时壁厚为:%dmm,质量为：%fkg,耐压极限为：%fm'%(math.ceil(R3)-r,m3,h3))
        return 0
    print('参数输入错误')
    return 0