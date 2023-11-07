#! usr/bin/env python

'''
Calculator 
Author:  FY
Data  :  2023-11-07
'''

from Tkinter import *
import time
import os



def var1():
    



if __name__=="__main__":
# Screeen Render
    tk_obj=Tk()
    tk_obj.geometry('500x600')
    tk_obj.resizable(0, 0)
    tk_obj.config(bg='white')
    tk_obj.title('Calculator')


    Button(tk_obj, text='1', bd='5', command='var1', bg='gray', font=("Arial",50,"roman")).place(x=10, y=210)
    Button(tk_obj, text='2', bd='5', command='var2', bg='gray', font=("Arial",50,"roman")).place(x=140, y=210)
    Button(tk_obj, text='3', bd='5', command='var3', bg='gray', font=("Arial",50,"roman")).place(x=280, y=210)
    Button(tk_obj, text='0', bd='5', command='var0', bg='gray', font=("Arial",50,"roman")).place(x=420, y=210)    
    Button(tk_obj, text='4', bd='5', command='var4', bg='gray', font=("Arial",50,"roman")).place(x=10, y=350)
    Button(tk_obj, text='5', bd='5', command='var5', bg='gray', font=("Arial",50,"roman")).place(x=140, y=350)
    Button(tk_obj, text='6', bd='5', command='var6', bg='gray', font=("Arial",50,"roman")).place(x=280, y=350)
    Button(tk_obj, text='.', bd='5', command='var_', bg='gray', font=("Arial",50,"roman")).place(x=420, y=350)
    Button(tk_obj, text='7', bd='5', command='var7', bg='gray', font=("Arial",50,"roman")).place(x=10, y=490)
    Button(tk_obj, text='8', bd='5', command='var8', bg='gray', font=("Arial",50,"roman")).place(x=140, y=490)
    Button(tk_obj, text='9', bd='5', command='var9', bg='gray', font=("Arial",50,"roman")).place(x=280, y=490)
    Button(tk_obj, text='=', bd='5', command='var=', bg='gray', font=("Arial",50,"roman")).place(x=420, y=490)
    tk_obj.mainloop()
