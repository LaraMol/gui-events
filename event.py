from re import T
import tkinter as tk

def printEventandClose(event):
    print('event: ' + str(event))
    mainwindow.destroy()

import tkinter

mainwindow = tkinter.Tk()

mainwindow.bind("a", printEventandClose)
mainwindow.bind("b", printEventandClose)

button = tkinter.Button (text="click here",command= mainwindow.destroy)
button.pack(ipady = 5 , ipadx =5)


mainwindow.mainloop()