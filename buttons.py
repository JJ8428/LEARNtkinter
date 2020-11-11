from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click Me", padx = 100, pady = 100, command = myClick, fg = "white", bg="blue") 
# No need to add () at the end of the function

myButton.pack()

root.mainloop()