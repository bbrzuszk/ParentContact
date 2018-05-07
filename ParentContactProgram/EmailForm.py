from tkinter import *
from tkinter import ttk
import sys
class ContactGui(object):

    def __init__(self, root:Tk):
        root.title("Parent Contact")
        root.geometry("1000x600")
        root.resizable(width=True, height=True)
        formStyle = ttk.Style()
        formStyle.configure('TButton', font=('Helvetica', 10))
        #upper frame - Gradebook, message destination
        topFrame = Frame(root)
            #Row 0
        lbl_Gradebook = ttk.Label(topFrame, text = "Gradebook: ")
        lbl_Gradebook.grid(row = 0, column = 0, columnspan = 2)
        entry_Gradebook = Entry(topFrame)
        entry_Gradebook.grid(row = 0, column = 2, columnspan = 3)
        btn_GradebookBrowse = ttk.Button(topFrame,text = "Select a Gradebook", style = 'TButton')
        btn_GradebookBrowse.grid(row = 0, column = 5)
            # Row 1
        lbl_MessageDestination = ttk.Label(topFrame, text="Message Destination: ")
        lbl_MessageDestination.grid(row=1, column=0, columnspan=2)
        entry_MessageDestination = Entry(topFrame)
        entry_MessageDestination.grid(row=1, column=2, columnspan=3)
        btn_MessageBrowse = ttk.Button(topFrame, text="Select a MessageDestination", style='TButton')
        btn_MessageBrowse.grid(row=1, column=5)
            # Row 2
        lbl_Components = ttk.Label(topFrame, text= "Grade Components: ")
        lbl_Components.grid(row= 2, column = 0, columnspan = 2)
        btn_Letter = ttk.Button(topFrame, text = "Letter")
        btn_Letter.grid(row = 2, column = 2)
        btn_Percentage = ttk.Button(topFrame, text = "Percentage")
        btn_Percentage.grid(row=2, column=3)
        btn_MissingWork = ttk.Button(topFrame, text = "Missing Assignments")
        btn_MissingWork.grid(row = 2, column = 4, columnspan = 2)
            #Row 3
        txtArea_Message = Text(topFrame, width = 40, height = 20)
        txtArea_Message.grid(row = 3, column = 0, columnspan = 4, rowspan = 6, pady = 20)
        lbl_pronounButts = ttk.Label(topFrame, text = "Pronoun's")
        lbl_pronounButts.grid(row = 3, column = 4, columnspan = 2)



        topFrame.grid()








root = Tk()
Contact = ContactGui(root)
root.mainloop()
sys.exit("closed")
