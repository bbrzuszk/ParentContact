from tkinter import *
from tkinter import ttk

class ContactGui(object):

    def __init__(self, root:Tk):
        root.title("Parent Contact")
        root.geometry("1000x600")
        root.resizable(width=True, height=True)

        #upper frame - Gradebook, message destination
        lbl_GradeBook = ttk.Label(root, text = "GradeBook: " ,borderwidth = 2, relief = "sunken", )
        lbl_GradeBook.grid(row = 0, column = 0, columnspan = 2)

        #column Spacer
        for i in range(10):
            bt = ttk.Button(root)
            bt.grid(row = 1, column = i)






root = Tk()
Contact = ContactGui(root)
root.mainloop()
