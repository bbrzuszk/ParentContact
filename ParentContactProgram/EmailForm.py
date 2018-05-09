from tkinter import *
from tkinter import ttk


import sys
class ContactGui(object):
    names = ('steve', 'jen', 'bill', 'carter')
    def __init__(self, root:Tk):
        print()
        root.title("Parent Contact")
        root.geometry("600x400")
        root.resizable(width=True, height=True)
        ttk.Style().theme_use('vista')
        self.gradebookString = StringVar()
        self.messageDestinationString = StringVar()
        self.buildTopInputs(root)
        self.buildMessageComponents(root)



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







    def getGradeBook(self):
        print("getting Gradebook")
        self.gradebookString.set("getting Gradebook")

    def getMessageDestinationFolder(self):
        self.messageDestinationString.set("getting message destination")








root = Tk()

Contact = ContactGui(root)
root.mainloop()
sys.exit("closed")
