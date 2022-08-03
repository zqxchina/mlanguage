__name__ ='M language'
__version__ = '1.0.0'
__author__ = 'Oranges - Zhangqi Xuan'
__thanks__='oranges - Chengze Li’s  oython1.0.2'
#           ©oython   橙子工作室版权所有
#           侵权必究，如有雷同，后果自负！
import tkinter as tk
import tkinter.messagebox
import time,os,sys
import webbrowser
from qrcode import *
import requests,pygame
from random import randint
from time import*
import time,os,sys
from xes.weather import *
import re
import requests
import time
from bs4 import BeautifulSoup
from urllib import parse
#------------------------------获取使用帮助
def help():#  ©oython   橙子工作室版权所有
    output("""
1.名字：messagebox  消息框
  用法：m.messagebox("内容","标题")  
  
2.名字：pip_install  使用pip下载python库
  用法：m.pip_install("下载库的名字",等待的时间)
  备注1：等待的时间指的是运行程序后的延时时间
  备注2：运行完本程序后会打开cmd，所以会有延时时间
  备注3：等待的时间不加括号！

3.名字：help  获取oython教学
  用法：m.help()
  
4.名字：waitoutput  逐字输出
  用法：m.waitoutput("内容")
  备注：逐字输出速度为每个字相隔0.05秒
  
5.名字：cleanscreen/Cls  清屏
  用法：m.cleanscreen()/m.Cls()
  备注：m.Cls()中的C是大写的！
  
6.名字：webopen  打开网址
  用法：m.webopen("网址")
  
7.名字：broadcast_mp3/bc_mp3  打开网址
  用法：m.broadcast_mp3("mp3名字")/bc_mp3("mp3名字")
  备注1：mp3名字需要加".mp3"后缀！
  备注2：只能播放mp3(M4A文件不行)
  
8.名字：output  输出
  用法：m.output("内容")
  
9.名字：make_qrcode  制作二维码
  用法：m.make_qrcode("二维码中储存的内容")
  
10.名字：translate  翻译
  用法：m.translate("翻译的内容")/print(translate("翻译的内容"))
  备注：这个程序只是储存一个变量...如需输出可以使用print

11.名字：m_sleep  等待
   用法：m.m_sleep("等待的时间")
  
12.名字：logo  logo制作器
   用法：m.logo("颜色")
   备注：颜色数字为1-9(是啥颜色自己试吧...)

13.名字：mgame_pic  oygame-显示图片模块
   用法：m.mgame_pic(长,宽,"弹窗名字","图片名字")
   备注：图片名字需要加文件后缀名！
   
14.名字：grttime  获取时间
   用法：m.gettime()
   
15.名字：getweather  获取天气
   用法：m.getweather("城市")
   
16.名字：ask  询问
   用法：m.ask("内容")
   注意：m.ask("内容")必须有上下引号（即使没有内容！）
    """)
    
#---------------------------------------messagebox  消息框
def messagebox(message,title):
    tk.messagebox.showerror(title,message) 
#---------------------------------------output 逐字输出 
def waitoutput(z): 
    t = 0.05
    a = 0 
    z = str(z) 
    t = float(t) 
    q = 0 
    for i in z: 
        q += 1 
        time.sleep(t)
        if a == len(z): 
            print(i) 
        else: 
            print(i,end = "") 
#---------------------------------------pip_install  使用pip下载python库
#备注1：等待的时间指的是运行程序后的延时时间
#备注2：运行完本程序后会打开cmd，所以会有延时时间
#备注3：等待的时间不加括号！
def pip_install(pip): 
    os.system("start pip install "+pip) 
#---------------------------------------cleanscreen/Cls  清屏
def cleanscreen(): 
    sys.stdout.write("\033[2J\033[00H") 
def Cls(): 
    sys.stdout.write("\033[2J\033[00H") 
#---------------------------------------webopen  打开网址
def webopen(web): 
    webbrowser.open(web) 
#---------------------------------------broadcast_mp3/bc_mp3  打开音乐
def broadcast_mp3(mp3,time = None): 
 
    if not isinstance(mp3,str): 
        raise Exception("") 
    pygame.mixer.init() 
    pygame.mixer.music.load(mp3) 
    pygame.mixer.music.play() 
    if time is not None: 
        time.sleep(time) 
        pygame.mixer.music.stop() 
    return "" 
def bc_mp3(mp3,time = None): 
 
    if not isinstance(mp3,str): 
        raise Exception("") 
    pygame.mixer.init() 
    pygame.mixer.music.load(mp3) 
    pygame.mixer.music.play() 
    if time is not None: 
        time.sleep(time) 
        pygame.mixer.music.stop() 
    return "" 
#---------------------------------------make_qrcode  制作二维码
def make_qrcode(qrcode): 
    qr = QRCode() 
    qr.add_data(qrcode) 
    img = qr.make_image() 
    img.show() 
#---------------------------------------输出
def output(content): 
    print(content) 
#---------------------------------------翻译 
def translate(content): 
    url = "http://fanyi.youdao.com/translate?doctype=json&type=AUTO&i="+content
    r = requests.get(url) 
    result = r.json() 
    return result["translateResult"][0][0]["tgt"] 
#---------------------------------------等待
def m_sleep(waittime): 
    time.sleep(waittime) 
#---------------------------------------logo制作器
def logo(cz):
    for lcz in range(len(cz)):
        if cz[lcz]=="1":
            print("\033[47m ",end="")
        elif cz[lcz]=="2":
            print("\033[43m ",end="")#  ©oython   橙子工作室版权所有
        elif cz[lcz]=="3":
            print("\033[41m ",end="")
        elif cz[lcz]=="4":
            print("\033[44m ",end="")
        elif cz[lcz]=="5":
            print("\033[45m ",end="")
        elif cz[lcz]=="6":
            print("\033[46m ",end="")
        elif cz[lcz]=="7":
            print("\033[42m ",end="")            #  ©oython   橙子工作室版权所有
        elif cz[lcz]=="8":
            print("\033[49m ",end="")
        elif cz[lcz]=="9":
            print("\033[40m ",end="")
        else:
            print(cz[lcz],end="")#  ©oython   橙子工作室版权所有
    print("\033[0m")
#---------------------------------------mgame-显示图片模块
def mgame_pic(a,b,c,d):
    pygame.init()                   
    screen = pygame.display.set_mode((a,b))
    pygame.display.set_caption(c)
    myImg = pygame.image.load(d)#  ©oython   橙子工作室版权所有
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(myImg,(0,0))#  ©oython   橙子工作室版权所有
        pygame.display.update()
#---------------------------------------gettime 获取时间
def gettime():
    e = strftime("%Y/%D   %H:%M")
    print(e)#  ©oython   橙子工作室版权所有
#---------------------------------------getweather 获取天气
def getweather(sp):
    temp=air_temp(sp,0)
    air=air_speed(sp,0)
    print("今日",temp,"度")
    print("风速",air)
#---------------------------------------ask 询问
def ask(sth):
    input(sth)
