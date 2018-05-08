from tkinter import *
from tkinter import ttk


import sys
class ContactGui(object):

    def __init__(self, root:Tk):
        print()
        root.title("Parent Contact")
        root.geometry("600x400")
        root.resizable(width=True, height=True)
        ttk.Style().theme_use('vista')
        self.gradebookString = StringVar()
        self.buildTopInputs(root)



    def buildTopInputs(self, master):
        frame = LabelFrame(master, text = "Inputs")

        frame.grid()
        ttk.Label(frame, text = "Gradebook: ").grid(row = 0, column = 0, sticky = "w")
        self.gradebookEntry = ttk.Entry(frame, cursor = "xterm" , width = "60", textvariable = self.gradebookString )
        self.gradebookEntry.grid(row = 0, column = 1, sticky = "e")
        self.gradebookBrowse = ttk.Button(frame, text = "...", command = self.getGradeBook)
        self.gradebookBrowse.grid(row = 0, column = 2)

        ttk.Label(frame, text="Message Destination: ").grid(row=1, column=0, sticky = "w")


    def getGradeBook(self):
        print("getting Gradebook")
        self.gradebookString.set("getting Gradebook")









root = Tk()

Contact = ContactGui(root)
root.mainloop()
sys.exit("closed")
