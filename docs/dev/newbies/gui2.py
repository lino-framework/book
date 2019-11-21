#!/usr/bin/python
# coding: utf-8
import random
from tkinter import *
from tkinter import messagebox

good_answer = random.randint(100, 999)

print("Spoiler: the good asnwer is", good_answer)

top = Tk()
top.title("Guees my number (between 100 and 999)")

Label(top, text="Guess my number").grid(row=0, column=0)

entry = Entry(top, bd =5)
entry.grid(row=0, column=1)
entry.focus_set()


def ctrl_a(event):
    "Select all the text in widget"
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

entry.bind("<Control-Key-a>", ctrl_a)
entry.bind('<FocusIn>', ctrl_a)

def submit_guess():
    a = int(entry.get())
    ok = False
    if a < good_answer:
        # msg = "Liiga väike."
        msg = "Too small!"
    elif a > good_answer:
        msg = "Liiga suur"
        msg = "Too big!"
    elif a == good_answer:
       # msg = "Õige. Tubli oled!"
       msg = "You got it! It was {}".format(good_answer)
       ok = True
    else:
       msg = "Uups, see pole võimalik."
    if ok:
        messagebox.showinfo(
           "Congratulation!", msg)
        top.destroy()
    else:
        messagebox.showinfo(
           "Try again!", msg)
        entry.focus_set()


btn = Button(top, text="Guess", command=submit_guess, default='normal')
btn.grid(row=1, column=0, columnspan=2)

def submit(e, b=None):
    btn.invoke()

entry.bind('<Return>', submit)
entry.bind('<KP_Enter>', submit)

# def func(event):
#     print(event.keysym)
# top.bind("<Key>", func)

top.mainloop()
