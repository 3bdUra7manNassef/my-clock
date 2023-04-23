from tkinter.ttk import *
from tkinter import *
from time import strftime

root = Tk()
root.title('Clock by 3bdo')

def timec():
    string = strftime('%I:%M:%S %p') # Corrected time format
    lable.config(text = string)
    lable.after(1000,timec) # Changed time to timec (typo)

lable = Label(root, font=("ds-digital",80),background = "black",foreground="green") # Corrected Label capitalization and spelling of "green"
lable.pack(anchor = 'center')
timec()

mainloop()
