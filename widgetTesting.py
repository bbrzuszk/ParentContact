from tkinter import *
from tkinter import ttk


import sys

names = ('steve', 'jen', 'bill', 'carter')
root = Tk()
root.geometry("400x400")
nameBox = Listbox(root)
for name in names:
    nameBox.insert(END, name)
nameBox.pack()

root.mainloop()