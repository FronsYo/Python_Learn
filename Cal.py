#! usr/bin/env python

'''
Calculator 
Author:  FY
Data  :  2023-11-08
'''

from Tkinter import *
import time
import os

'''
1.create button
2.print select value on screen
3.print result 
'''

def printvar(Bvar):
    '''get value and print it at relatead label'''
    global dflag
    if (dflag==1):
        e.delete(0,END)
        dflag=0
    currval=e.get()
    e.delete(0,END)
    e.insert(0,str(currval)+str(Bvar))
def cal():
    currval=e.get()
    res=eval(currval)
    global dflag
    dflag=1             #clear render after math operation and new value inputed
    e.delete(0,END)
    e.insert(0,str(res))

def delOne():
    currval=e.get()
    NumV=len(currval)
    e.delete(NumV-1,END)

def delAll():
        e.delete(0,END)


if __name__=="__main__":
# Screeen Render
    tk_obj=Tk()
    tk_obj.geometry('500x800')
    tk_obj.resizable(0, 0)
    tk_obj.config(bg='white')
    tk_obj.title('Calculator')
    global dflag
    dflag=0
    '''display render'''
    e=Entry(tk_obj,width=15,bd=3, font=("Arial",40,"roman"))
    e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    '''Create button'''
    button1=Button(tk_obj, text='1', bd='5', command=lambda:printvar('1'), bg='gray', font=("Arial",50,"roman"))
    button2=Button(tk_obj, text='2', bd='5', command=lambda:printvar('2'), bg='gray', font=("Arial",50,"roman"))
    button3=Button(tk_obj, text='3', bd='5', command=lambda:printvar('3'), bg='gray', font=("Arial",50,"roman"))
    button0=Button(tk_obj, text='0', bd='5', command=lambda:printvar('0'), bg='gray', font=("Arial",50,"roman"))  
    button4=Button(tk_obj, text='4', bd='5', command=lambda:printvar('4'), bg='gray', font=("Arial",50,"roman"))
    button5=Button(tk_obj, text='5', bd='5', command=lambda:printvar('5'), bg='gray', font=("Arial",50,"roman"))
    button6=Button(tk_obj, text='6', bd='5', command=lambda:printvar('6'), bg='gray', font=("Arial",50,"roman"))
    button_=Button(tk_obj, text='.', bd='5', command=lambda:printvar('.'), bg='gray', font=("Arial",50,"roman"))
    button7=Button(tk_obj, text='7', bd='5', command=lambda:printvar('7'), bg='gray', font=("Arial",50,"roman"))
    button8=Button(tk_obj, text='8', bd='5', command=lambda:printvar('8'), bg='gray', font=("Arial",50,"roman"))
    button9=Button(tk_obj, text='9', bd='5', command=lambda:printvar('9'), bg='gray', font=("Arial",50,"roman"))
    button__=Button(tk_obj, text='=', bd='5', command=cal, bg='gray', font=("Arial",50,"roman"))
    buttonP=Button(tk_obj, text='+', bd='5', command=lambda:printvar('+'), bg='blue', font=("Arial",50,"roman"))
    buttonM=Button(tk_obj, text='-', bd='5', command=lambda:printvar('-'), bg='blue', font=("Arial",50,"roman"))
    buttonT=Button(tk_obj, text='*', bd='5', command=lambda:printvar('*'), bg='blue', font=("Arial",50,"roman"))
    buttonDi=Button(tk_obj, text='/', bd='5', command=lambda:printvar('/'), bg='blue', font=("Arial",50,"roman"))
    buttonD=Button(tk_obj, text='<<', bd='5', command=delOne, bg='red', font=("Arial",50,"roman"))
    buttonC=Button(tk_obj, text='del', bd='5', command=delAll, bg='red', font=("Arial",50,"roman")) 
    '''Place button'''
    button1.place(x=10, y=210)
    button2.place(x=140, y=210)
    button3.place(x=280, y=210)
    button0.place(x=420, y=210)    
    button4.place(x=10, y=350)
    button5.place(x=140, y=350)
    button6.place(x=280, y=350)
    button_.place(x=420, y=350)
    button7.place(x=10, y=490)
    button8.place(x=140, y=490)
    button9.place(x=280, y=490)
    button__.place(x=420, y=490)
    buttonP.place(x=10, y=630)
    buttonM.place(x=140, y=630)
    buttonT.place(x=280, y=630)
    buttonDi.place(x=420, y=630)    
    buttonD.place(x=180, y=90)
    buttonC.place(x=310, y=90) 
    
    tk_obj.mainloop()
