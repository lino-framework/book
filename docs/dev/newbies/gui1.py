#!/usr/bin/python
# http://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox

top = Tk()

L1 = Label(top, text="User Name")
# L1.pack(side=LEFT)
L1.grid(row=0, column=0)

E1 = Entry(top, bd =5)
# E1.pack(side=RIGHT)
E1.grid(row=0, column=1)

def helloCallBack():
   messagebox.showinfo(
       "Hello Python",
       "Hello, " + E1.get())

B = Button(top, text ="Hello", command=helloCallBack)

# B.pack(side=RIGHT)
B.grid(row=1, column=0, columnspan=2)

top.mainloop()
