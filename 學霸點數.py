# coding=UTF-8
from tkinter import *
import tkinter
import os
path = os.path.dirname(os.path.abspath(__file__))
import math
import re
import time

def ssts(char, a):
    if re.search(a,char):
        return 1
    else:
        return 0

command_r = open(path + '/txts/command.txt', 'r',encoding="utf-8")

commands = []

def rc():
    global user
    global point
    command_r = open(path + '/txts/command.txt', 'r',encoding="utf-8")
    for cline in command_r.readlines():
        old_na = cline[0:2]
        old_nu = cline[3:]
        if old_nu[-1:] == "\n":
            old_nu = old_nu[:-1]
        if old_na == "點數":
            old_nu = int(old_nu)
        old_cmd = {'name': old_na, 'number': old_nu}
        commands.append(old_cmd)
    command_r.close
    for command in commands:
        if command['name'] == "用戶":
            user = command['number']
        elif command['name'] == "點數":
            point = command['number']
        else:
            break

rc()
win = Tk() 
win.title("學霸點數") 
win.geometry("400x1000+0+300") 
win.minsize(width="400", height="65") 
win.resizable(0, 1) 
win.iconbitmap(path+"/images/icon.ico") 
win.config(background="white") 
win.attributes("-alpha", 1) 
win.attributes("-topmost", 1) 

lb = Label(text="-用戶資料-", bg="yellow", fg="orange", height=1, width=10000, cursor="star")
lb.pack()

lbu = Label(text="用戶："+user, bg="white", fg="black")
lbu.pack()

def rp():
    global point
    global user
    rc()
    level = 1
    point1 = point
    level_point = level*10
    while point1-level_point >= 0:
        point1 = point-level_point
        level = level+1
        level_point = level*10
    lbl.config(text="等級：["+str(level)+"]"+str(point1)+"/"+str(level_point))

lbl = Label(bg="white", fg="black")
lbl.pack()
rp()

def usersetok():
    global win2
    global enug
    global enu
    global enpg
    global enp
    enug = enu.get()
    if enug == "":
        enug = "未登入"
    enpg = enp.get()
    if enpg == "":
        enpg = 0
    command_a = open(path + '/txts/command.txt', 'w+',encoding="utf-8")
    command_a.write("用戶："+enug+"\n點數："+str(enpg))
    command_a.close
    history_w = open(path + '/txts/history.txt', 'w',encoding="utf-8")
    history_w.close
    win2.quit()

def userset():
    global win2
    global enu
    global enp
    global btnsetok
    rc()
    global user
    global point
    win2 = Tk()
    win2.title("學霸點數") 
    win2.geometry("400x1000+400+300") 
    win2.minsize(width="400", height="65") 
    win2.resizable(0, 1) 
    win2.iconbitmap(path+"/images/icon.ico") 
    win2.config(background="white") 
    win2.attributes("-alpha", 1) 
    win2.attributes("-topmost", 1) 
    lb = Label(win2, text="-用戶設定-", bg="yellow", fg="orange", height=1, width=10000, cursor="star")
    lb.pack()
    lb = Label(win2, text="用戶(目前："+str(user)+")", bg="white", fg="black")
    lb.pack()
    enu = Entry(win2)
    enu.pack()
    lb = Label(win2, text="用戶(目前："+str(point)+")", bg="white", fg="black")
    lb.pack()
    enp = Entry(win2)
    enp.pack()
    btnsetok = Button(win2, text="確認")
    btnsetok.config(command=usersetok)
    btnsetok.pack()
    lb = Label(win2, text="1)本軟體由貓虎皮開發\n2)如果程式自行退出，請重新開啟\n3)感謝您的下載，歡迎多加利用\n4)如有問題，請聯絡「5j.vm0.m3@gmail.com」\n6)不同筆成績的「備註」請使用不同內容，否則在註銷時，\n   點數扣除與紀錄刪除可能出錯\n7)點數與紀錄並不會因登入而同步", bg="white", fg="black", justify="left")
    lb.pack()

btnset = Button(text="設定",cursor="man")
btnset.config(command=userset)
btnset.pack()

def point_p(num=0):
    global user
    global point
    rc()
    command_a = open(path + '/txts/command.txt', 'w',encoding="utf-8")
    command_a.write("用戶："+user+"\n點數："+str(point+num))
    command_a.close
    rp()

lb = Label(text="-點數申請-", bg="yellow", fg="orange", height=1, width=10000, cursor="heart")
lb.pack()

lb = Label(text="類別", bg="white", fg="black")
lb.pack()
en1 = Entry()
en1.pack()

lb = Label(text="科目", bg="white", fg="black")
lb.pack()
en2 = Entry()
en2.pack()

lb = Label(text="分數", bg="white", fg="black")
lb.pack()
en3 = Entry()
en3.pack()

lb = Label(text="滿分", bg="white", fg="black")
lb.pack()
en4 = Entry()
en4.pack()

lb = Label(text="備註", bg="white", fg="black")
lb.pack()
en5 = Entry()
en5.pack()

def enter_en():
    append_point = 0
    eg = en1.get()
    if ssts(eg, "一抽") == 1:
        h_a = "一抽"
        h_an = 5
    elif ssts(eg, "二抽") == 1:
        h_a = "二抽"
        h_an = 5
    elif ssts(eg, "三抽") == 1:
        h_a = "三抽"
        h_an = 5
    elif ssts(eg, "一段") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "二段") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "三段") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "小考") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "中考") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "抽考") == 1:
        h_a = "抽考"
        h_an = 3
    elif ssts(eg, "大考") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "段考") == 1:
        h_a = "段考"
        h_an = 5
    elif ssts(eg, "成測") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "u4t..") == 1:
        h_a = "一抽"
        h_an = 5
    elif ssts(eg, "-4t..") == 1:
        h_a = "二抽"
        h_an = 5
    elif ssts(eg, "n0 t..") == 1:
        h_a = "三抽"
        h_an = 5
    elif ssts(eg, "u.2j04") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "-42j04") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "n0.2j04") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "vul3dl3") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "5j/.dl3") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "t..dl3") == 1:
        h_a = "抽考"
        h_an = 3
    elif ssts(eg, "284dl3") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "2j04dl3") == 1:
        h_a = "段考"
        h_an = 5
    elif ssts(eg, "t/6hk4") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "b") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "1m") == 1:
        h_a = "一抽"
        h_an = 3
    elif ssts(eg, "2m") == 1:
        h_a = "二抽"
        h_an = 3
    elif ssts(eg, "3m") == 1:
        h_a = "三抽"
        h_an = 3
    elif ssts(eg, "1b") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "2b") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "3b") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "1l") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "2l") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "3l") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "at") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "s") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "m") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "l") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "b") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "a") == 1:
        h_a = "成測"
        h_an = 8
    else:
        h_a = eg
        h_an = 1
    eg2 = en2.get()
    if ssts(eg2, "國文") == 1:
        h_b = "國文"
    elif ssts(eg2, "國語") == 1:
        h_b = "國語"
    elif ssts(eg2, "數學") == 1:
        h_b = "數學"
    elif ssts(eg2, "自然") == 1:
        h_b = "自然"
    elif ssts(eg2, "生物") == 1:
        h_b = "生物"
    elif ssts(eg2, "理化") == 1:
        h_b = "理化"
    elif ssts(eg2, "生科") == 1:
        h_b = "生科"
    elif ssts(eg2, "生活科技") == 1:
        h_b = "生科"
    elif ssts(eg2, "物理") == 1:
        h_b = "物理"
    elif ssts(eg2, "化學") == 1:
        h_b = "化學"
    elif ssts(eg2, "社會") == 1:
        h_b = "社會"
    elif ssts(eg2, "地理") == 1:
        h_b = "地理"
    elif ssts(eg2, "地科") == 1:
        h_b = "地科"
    elif ssts(eg2, "地球科學") == 1:
        h_b = "地科"
    elif ssts(eg2, "歷史") == 1:
        h_b = "歷史"
    elif ssts(eg2, "公民") == 1:
        h_b = "公民"
    elif ssts(eg2, "英文") == 1:
        h_b = "英文"
    elif ssts(eg2, "英語") == 1:
        h_b = "英語"
    elif ssts(eg2, "eji6jp6") == 1:
        h_b = "國文"
    elif ssts(eg2, "eji6m3") == 1:
        h_b = "國語"
    elif ssts(eg2, "gj4vm,6") == 1:
        h_b = "數學"
    elif ssts(eg2, "y4b06") == 1:
        h_b = "自然"
    elif ssts(eg2, "g/.j4") == 1:
        h_b = "生物"
    elif ssts(eg2, "xu3cj84") == 1:
        h_b = "理化"
    elif ssts(eg2, "g/.dk.") == 1:
        h_b = "生科"
    elif ssts(eg2, "g/.cji6dk.ru4") == 1:
        h_b = "生科"
    elif ssts(eg2, "j4xu3") == 1:
        h_b = "物理"
    elif ssts(eg2, "cj84vm,6") == 1:
        h_b = "化學"
    elif ssts(eg2, "gk4cjo4") == 1:
        h_b = "社會"
    elif ssts(eg2, "2u4xu3") == 1:
        h_b = "地理"
    elif ssts(eg2, "2u4dk.") == 1:
        h_b = "地科"
    elif ssts(eg2, "2u4fu.6dk.vm,6") == 1:
        h_b = "地科"
    elif ssts(eg2, "xu4g3") == 1:
        h_b = "歷史"
    elif ssts(eg2, "ej/.aup6") == 1:
        h_b = "公民"
    elif ssts(eg2, "u/.jp6") == 1:
        h_b = "英文"
    elif ssts(eg2, "u/.m3") == 1:
        h_b = "英語"
    elif ssts(eg2, "c") == 1:
        h_b = "國文"
    elif ssts(eg2, "m") == 1:
        h_b = "數學"
    elif ssts(eg2, "n") == 1:
        h_b = "自然"
    elif ssts(eg2, "s") == 1:
        h_b = "社會"
    elif ssts(eg2, "e") == 1:
        h_b = "英文"
    else:
        h_b = eg2
    eg3 = en3.get()
    h_c = int(eg3)
    eg4 = en4.get()
    h_d = int(eg4)
    eg5 = en5.get()
    h_e = eg5
    append_point = (math.floor(h_c*100/h_d)-80)*h_an
    history_a = open(path + '/txts/history.txt', 'a+',encoding="utf-8")
    history_a.write("\n"+"["+h_a+h_b+"]"+str(append_point)+"(分數："+str(h_c)+"/"+str(h_d)+"備註："+str(h_e)+")")
    history_a.close
    history_r = open(path + '/txts/history.txt', 'r',encoding="utf-8")
    lbh.config(text=history_r.read())
    history_r.close
    point_p(append_point)

btn1 = Button(text="送出",cursor="plus")
btn1.config(command=enter_en)
btn1.pack()

def rh():
    lbh.config(text=history_r.read())
    history_r.close
    
def delete_en():
    append_point = 0
    eg = en1.get()
    if ssts(eg, "一抽") == 1:
        h_a = "一抽"
        h_an = 5
    elif ssts(eg, "二抽") == 1:
        h_a = "二抽"
        h_an = 5
    elif ssts(eg, "三抽") == 1:
        h_a = "三抽"
        h_an = 5
    elif ssts(eg, "一段") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "二段") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "三段") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "小考") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "中考") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "抽考") == 1:
        h_a = "抽考"
        h_an = 3
    elif ssts(eg, "大考") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "段考") == 1:
        h_a = "段考"
        h_an = 5
    elif ssts(eg, "成測") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "u4t..") == 1:
        h_a = "一抽"
        h_an = 5
    elif ssts(eg, "-4t..") == 1:
        h_a = "二抽"
        h_an = 5
    elif ssts(eg, "n0 t..") == 1:
        h_a = "三抽"
        h_an = 5
    elif ssts(eg, "u.2j04") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "-42j04") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "n0.2j04") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "vul3dl3") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "5j/.dl3") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "t..dl3") == 1:
        h_a = "抽考"
        h_an = 3
    elif ssts(eg, "284dl3") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "2j04dl3") == 1:
        h_a = "段考"
        h_an = 5
    elif ssts(eg, "t/6hk4") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "b") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "1m") == 1:
        h_a = "一抽"
        h_an = 3
    elif ssts(eg, "2m") == 1:
        h_a = "二抽"
        h_an = 3
    elif ssts(eg, "3m") == 1:
        h_a = "三抽"
        h_an = 3
    elif ssts(eg, "1b") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "2b") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "3b") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "1l") == 1:
        h_a = "一段"
        h_an = 5
    elif ssts(eg, "2l") == 1:
        h_a = "二段"
        h_an = 5
    elif ssts(eg, "3l") == 1:
        h_a = "三段"
        h_an = 5
    elif ssts(eg, "at") == 1:
        h_a = "成測"
        h_an = 8
    elif ssts(eg, "s") == 1:
        h_a = "小考"
        h_an = 1
    elif ssts(eg, "m") == 1:
        h_a = "中考"
        h_an = 5
    elif ssts(eg, "l") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "b") == 1:
        h_a = "大考"
        h_an = 10
    elif ssts(eg, "a") == 1:
        h_a = "成測"
        h_an = 8
    else:
        h_a = eg
        h_an = 1
    eg2 = en2.get()
    if ssts(eg2, "國文") == 1:
        h_b = "國文"
    elif ssts(eg2, "國語") == 1:
        h_b = "國語"
    elif ssts(eg2, "數學") == 1:
        h_b = "數學"
    elif ssts(eg2, "自然") == 1:
        h_b = "自然"
    elif ssts(eg2, "生物") == 1:
        h_b = "生物"
    elif ssts(eg2, "理化") == 1:
        h_b = "理化"
    elif ssts(eg2, "生科") == 1:
        h_b = "生科"
    elif ssts(eg2, "生活科技") == 1:
        h_b = "生科"
    elif ssts(eg2, "物理") == 1:
        h_b = "物理"
    elif ssts(eg2, "化學") == 1:
        h_b = "化學"
    elif ssts(eg2, "社會") == 1:
        h_b = "社會"
    elif ssts(eg2, "地理") == 1:
        h_b = "地理"
    elif ssts(eg2, "地科") == 1:
        h_b = "地科"
    elif ssts(eg2, "地球科學") == 1:
        h_b = "地科"
    elif ssts(eg2, "歷史") == 1:
        h_b = "歷史"
    elif ssts(eg2, "公民") == 1:
        h_b = "公民"
    elif ssts(eg2, "英文") == 1:
        h_b = "英文"
    elif ssts(eg2, "英語") == 1:
        h_b = "英語"
    elif ssts(eg2, "eji6jp6") == 1:
        h_b = "國文"
    elif ssts(eg2, "eji6m3") == 1:
        h_b = "國語"
    elif ssts(eg2, "gj4vm,6") == 1:
        h_b = "數學"
    elif ssts(eg2, "y4b06") == 1:
        h_b = "自然"
    elif ssts(eg2, "g/.j4") == 1:
        h_b = "生物"
    elif ssts(eg2, "xu3cj84") == 1:
        h_b = "理化"
    elif ssts(eg2, "g/.dk.") == 1:
        h_b = "生科"
    elif ssts(eg2, "g/.cji6dk.ru4") == 1:
        h_b = "生科"
    elif ssts(eg2, "j4xu3") == 1:
        h_b = "物理"
    elif ssts(eg2, "cj84vm,6") == 1:
        h_b = "化學"
    elif ssts(eg2, "gk4cjo4") == 1:
        h_b = "社會"
    elif ssts(eg2, "2u4xu3") == 1:
        h_b = "地理"
    elif ssts(eg2, "2u4dk.") == 1:
        h_b = "地科"
    elif ssts(eg2, "2u4fu.6dk.vm,6") == 1:
        h_b = "地科"
    elif ssts(eg2, "xu4g3") == 1:
        h_b = "歷史"
    elif ssts(eg2, "ej/.aup6") == 1:
        h_b = "公民"
    elif ssts(eg2, "u/.jp6") == 1:
        h_b = "英文"
    elif ssts(eg2, "u/.m3") == 1:
        h_b = "英語"
    elif ssts(eg2, "c") == 1:
        h_b = "國文"
    elif ssts(eg2, "m") == 1:
        h_b = "數學"
    elif ssts(eg2, "n") == 1:
        h_b = "自然"
    elif ssts(eg2, "s") == 1:
        h_b = "社會"
    elif ssts(eg2, "e") == 1:
        h_b = "英文"
    else:
        h_b = eg2
    eg3 = en3.get()
    h_c = int(eg3)
    eg4 = en4.get()
    h_d = int(eg4)
    eg5 = en5.get()
    h_e = eg5
    append_point = (math.floor(h_c*100/h_d)-80)*h_an
    history_r = open(path + '/txts/history.txt', 'r',encoding="utf-8")
    historyn_a = open(path + '/txts/historyn.txt', 'a+',encoding="utf-8")
    hd = "["+h_a+h_b+"]"+str(append_point)+"(分數："+str(h_c)+"/"+str(h_d)+"備註："+str(h_e)+")"
    for historyk in history_r.readlines():
        if historyk[-1:] == "\n":
            historyk = historyk[:-1]
        if historyk != hd and historyk != "":
            historyn_a.write(historyk+"\n")
    history_r.close
    historyn_a.close
    os.remove('txts/history.txt')
    os.rename('txts/historyn.txt', 'txts/history.txt')
    point_p(-append_point)
    win.quit()

btn2 = Button(text="撤銷",cursor="exchange")
btn2.config(command=delete_en)
btn2.pack()

lb = Label(text="-歷史紀錄-", bg="yellow", fg="orange", height=1, width=10000, cursor="dotbox")
lb.pack()

history_r = open(path + '/txts/history.txt', 'r',encoding="utf-8")
lbh = Label(text=history_r.read(), bg="white", fg="black")
lbh.pack()

win.mainloop()