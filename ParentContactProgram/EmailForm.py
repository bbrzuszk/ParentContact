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



    def buildTopInputs(self, master):
        """Builds top frame for message input components"""
        frame = LabelFrame(master, text = "Inputs")

        frame.grid(padx = 20)
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

        ttk.Label(frame, text = "Select Student(s): ").grid(row = 2, column = 0, sticky = "w")

        self.studentDropDownMenu = Listbox(frame, selectmode = MULTIPLE, height = 1, activestyle = "none")
       # yScroll = Scrollbar(self.studentDropDownMenu,orient=VERTICAL)
       # yScroll.grid(row=0, column=1, sticky="ns")
      #  yScroll['command'] = self.studentDropDownMenu.yview()
        self.buildStudentMenu()
        self.studentDropDownMenu.grid(row = 2, column = 1, sticky = "w")




    def getGradeBook(self):
        print("getting Gradebook")
        self.gradebookString.set("getting Gradebook")

    def getMessageDestinationFolder(self):
        self.messageDestinationString.set("getting message destination")

    def buildStudentMenu(self):
        for i in range(len(ContactGui.names)):
            self.studentDropDownMenu.insert(i, ContactGui.names[i])






root = Tk()

Contact = ContactGui(root)
root.mainloop()
sys.exit("closed")
