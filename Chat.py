# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:35:22 2017

@author: RD2016
"""

import sys
from tkinter import *
from tkinter import filedialog

myApp = Tk()
myApp.title('Chat')                 #set the Title of the App
myApp.geometry('450x450+200+200')   #set the size of window

mLabel = Label(myApp,text='Wanna to Chat?')
mLabel.pack()

mEntry = StringVar()                      #create a string variable

def mHello():
    mText = mEntry.get()
    mlabel1 = Label(myApp,text=mText)
    mlabel1.pack()
    
def myNew():
    mlabel1 = Label(myApp,text="YO")
    mlabel1.pack()
    
def myOpen():
    myOpen = filedialog.askopenfile()
    mlabel4 = Label(myApp,text=myOpen).pack()
    mlabel4.pack()
    
def mAbout():
    messagebox.showinfo(title="About",message="This is my first Chat App")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure to Quit?")
    if mExit > 0:
        myApp.destroy()
        
mButton = Button(myApp,text ='OK', command = mHello)
mButton.pack()

mEntry = Entry(myApp,textvariable=mEntry)     #set the mEntry variable from the text entry box
mEntry.pack()

menubar = Menu(myApp)                               #create the menubar
menubar.add_cascade(label="File",menu=filemenu)     #create File Menu Item
menubar.add_cascade(label="Help",menu=helpmenu)     #create Help Menu Item

filemenu = Menu(menubar, tearoff=0)                 #create File component
filemenu.add_command(label="New", command=myNew)    #Add subheadings to File Menu Item
filemenu.add_command(label="Open", command=myOpen)
filemenu.add_command(label="Save As...")
filemenu.add_command(label="Close", command=mQuit)

helpmenu = Menu(menubar, tearoff=0)                 #create Help component
helpmenu.add_command(label="Open Help File")             #Add subheadings to Help Menu Item
helpmenu.add_command(label="About",command=mAbout)

myApp.config(menu=menubar)                          #add menubar to the window
myApp.mainloop()
