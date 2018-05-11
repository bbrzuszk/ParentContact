from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import sys
class ContactGui(object):
    names = ('steve', 'jen', 'bill', 'carter')
    def __init__(self, root:Tk):
        print()
        root.title("Parent Contact")
        root.geometry("750x500")
        root.resizable(width=True, height=True)
        ttk.Style().theme_use('vista')
        self.gradebookString = StringVar()
        self.messageDestinationString = StringVar()
        self.buildTopInputs(root)
        self.buildMessageComponents(root)
        self.buildExecutionComponents(root)



    def buildTopInputs(self, master):
        """Builds top frame for message input components"""
        frame = LabelFrame(master, text = "Inputs")

        frame.grid(row = 0,padx = 20, sticky = "w")
        ttk.Label(frame, text = "Gradebook: ").grid(row = 0, column = 0, sticky = "w")
        self.gradebookEntry = ttk.Entry(frame, cursor = "xterm" , width = "60", textvariable = self.gradebookString )
        self.gradebookEntry.grid(row = 0, column = 1, sticky = "e")
        self.gradebookBrowse = ttk.Button(frame, text = "...", command = self.getGradeBook)
        self.gradebookBrowse.grid(row = 0, column = 2)

        ttk.Label(frame, text="Message Destination: ").grid(row=1, column=0, sticky = "w")
        self.messageEntry = ttk.Entry(frame, cursor = "xterm" , width = "60", textvariable = self.messageDestinationString)
        self.messageEntry.grid(row=1, column=1, sticky="e")
        self.messageBrowse = ttk.Button(frame, text="...", command = self.getMessageDestinationFolder)
        self.messageBrowse.grid(row=1, column=2)

    def buildMessageComponents(self, master):
        frame = LabelFrame(master, text="Message")
        frame.grid(row = 1, padx=20, sticky = "w")
        ttk.Label(frame, text = "Grade Components").grid(row = 0, column = 0 , sticky = "w")
        self.btn_insertLetter = ttk.Button(frame, text = "Letter")
        self.btn_insertLetter.grid(row = 0, column = 1, padx = 10)
        self.btn_insertPercent = ttk.Button(frame, text = "Student %")
        self.btn_insertPercent.grid(row = 0, column = 2, padx = 10)
        self.btn_insertMissingWork = ttk.Button(frame, text = "Missing Work")
        self.btn_insertMissingWork.grid(row = 0, column = 3, columnspan = 2, padx = 10)

        self.message = Text(frame, width = 60, height = 20, relief = SUNKEN, borderwidth = 3)
        self.message.grid(row = 1, column = 0, columnspan = 3, rowspan = 2, padx = 5, pady = 5)


    def buildExecutionComponents(self, master):
        frame = LabelFrame(master, text="Build")
        frame.grid(row=2, padx=20, sticky="w")


        self.btn_GeneratePlainText = ttk.Button(frame, text = "Generate Plain Text Message")
        self.btn_GeneratePlainText.grid(row = 0, column = 0, sticky = "e")




    def getGradeBook(self):
        import os
        print("getting Gradebook")
        self.gradebookString.set(filedialog.askopenfilename(initialdir = os.getcwd()))

    def getMessageDestinationFolder(self):
        self.messageDestinationString.set(filedialog.askdirectory())









root = Tk()

Contact = ContactGui(root)
root.mainloop()
sys.exit("closed")