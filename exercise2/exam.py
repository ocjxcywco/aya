#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import os
from tkinter import *

#按扭调用的函数，
equ=''
order=0
wrong_equ=''
wrong_num=0
counter=0
time=0

def counter_label(label):
    def count(): 
        global counter,s
        counter+=1      
        #configures
        #text
        label.config(text=str(counter//600//10)+str(counter//600%10)+':'+str(counter%600//100)+str(counter%100//10)+'.'+str(counter%10))
        #color
        label.config(fg='red')
        #label position
        label.config(anchor='c')
        #after every 100ms,do count()
        s=label.after(100, count)
    count()

def calc_label(label_equ,label_ord):
    global order
    def calc():
        global equ
        n=random.randint(3,5)
        num=[0]*5   #numbers used in equations
        op=['']*4   #oprators used in equations
        equ=''      #equation

        for i in range(n-1):                                #randomize num & op
            num[i]=random.randint(1,100)
            op[i]=random.choice('+-*/')
            equ+=str(num[i])+op[i]                          #set up equations
        num[n-1]=random.randint(1,100)
        equ+=str(num[n-1]) 

    calc()   
    label_equ['text']=equ
    order+=1
    label_ord.config(text=str(order)+'.',bg='gray',fg='blue')

def ans():
    global root0
    root.destroy()
    root0=Tk()
    root0.geometry('300x400')
    root0.title("结果")
    Message(root0,text='你做对了'+str(10-wrong_num)+'道题，耗时'+str(time//600//10)+str(time//600%10)+':'+str(time%600//100)+str(time%100//10)+'.'+str(time%10)+'\n\n这些是你做错的题目：\n'+wrong_equ).pack()
    l_quit=Button(root0,text='Quit',width='10',height='2',command=quit).pack(anchor='n',side='right',padx=10,pady=10)
    l_restart=Button(root0,text='Restart',width='10',height='2',command=main).pack(anchor='n',side='right',padx=10,pady=10)

def quit():
    root0.destroy()

def check():
    global wrong_num,wrong_equ,order,counter,time

    l_ans['text']=''
    Equ=e_equ.get()
    len_equ=len(Equ)

    if (len_equ==0):
        order-=1
        l_ans.config(text=equ+'正确答案是：'+str(round(eval(l_equ['text']))),fg='dark cyan')
        l_ans.pack()
        b_enter.pack(side='right')
        l_msg['text']='Skipped'
        l_msg['fg']='blue'
        counter=time

    elif (Equ == str(round(eval(l_equ['text'])))):
        l_msg['text']='Correct!'
        l_msg['fg']='dark green'
        time=counter
    else:
        l_msg['text']='Wrong!'
        l_msg['fg']='red'
        wrong_num+=1
        wrong_equ+=l_equ['text']+'='+str(round(eval(l_equ['text'])))+'\n'
        time=counter

    e_equ.delete(0,len_equ)
    if (order<10):
        calc_label(l_equ,l_ord)
    else:
        l_time.after_cancel(s)
        ans()

def main():
    global root,l_msg,l_ord,l_time,l_ans,l_equ,e_equ,b_enter,order,wrong_equ,wrong_num,time,counter
    equ=''
    order=0
    wrong_equ=''
    wrong_num=0
    counter=0
    time=0
    root0.destroy()

    root=Tk()
    root.title("出题器")
    l_frame=Frame(root)
    #first line: title
    l_msg=Label(root,text='Welcome')
    l_msg.pack(pady=10)

    #second line: order number,equation,entry
    l_ord=Label(l_frame)
    l_ord.pack(side='left')
    l_equ=Label(l_frame)
    calc_label(l_equ,l_ord)
    l_equ.pack(side='left')
    Label(l_frame,text='=').pack(side='left')
    e_equ=Entry(l_frame)
    e_equ.pack(side='left')
    l_frame.pack(anchor='n')

    #third line: time,hint,"Enter" button
    l_time=Label(root)
    l_time.pack(anchor='n',side='left',padx=10,pady=10)
    counter_label(l_time)
    l_ans=Label(root,text='')
    l_ans.pack(anchor='n',side='left')
    b_enter=Button(root,text='Enter',command=check)
    b_enter.pack(anchor='n',side='right',padx=10,pady=10)

    root.mainloop()

root0=Tk()
root0.title("出题器")
root0.geometry('250x150')
Button(root0,text='Start',width='10',height='2',command=main).pack(anchor='center',expand='yes')
root0.mainloop()