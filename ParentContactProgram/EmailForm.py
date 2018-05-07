from tkinter import *
from tkinter import ttk

class ContactGui(object):

    def __init__(self, root:Tk):
        root.title("Parent Contact")
        root.geometry("1000x600")
        root.resizable(width=True, height=True)


root = Tk()
Contact = ContactGui(root)
root.mainloop()