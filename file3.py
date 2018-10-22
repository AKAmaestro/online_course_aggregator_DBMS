# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 20:32:48 2018

@author: ADITYA
"""
from tkinter import *
import sqlite3


def sel():
    pr=str(var1.get())
    pr=pr.lower()
    st=str(var2.get())
    st=st.lower()
    #print(pr+" "+st)
    query='''SELECT * FROM courses, details WHERE provider="'''+pr+'''" AND category="'''
           +st+'''"'''
    
    conn = sqlite3.connect('onlineCourses.db')
    c = conn.cursor()
    c.execute(query)
    
    data=c.fetchall()
    

root = Tk()

frame1 = Frame(root, highlightbackground="green", highlightcolor="green",width=500, height=500, bg="blue")
frame1.pack()
frame2 = Frame(root, highlightbackground="red", highlightcolor="red",width=500, height=500, bg="red")
frame2.pack()

providers=['UDEMY','UDACITY','COURSERA']
var1 = StringVar()

for provider in providers:
    radio1 = Radiobutton(frame1, text=provider, variable=var1 ,value=provider,command=sel)
    radio1.pack(side=TOP)
   
var1.set("UDEMY")    
    
streams=['DATA SCIENCE','BLOCKCHAIN','DEVELOPMENT']
var2 = StringVar()

for stream in streams:
    radio2 = Radiobutton(frame2 ,text=stream, variable=var2 ,value=stream,command=sel)
    radio2.pack(side=TOP)
    
var2.set("DATA SCIENCE")
root.mainloop()