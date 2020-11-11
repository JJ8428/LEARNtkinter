from tkinter import *

root = Tk()
# Change the title
root.title("Java String Printer")

e = Entry(root, width = 20, borderwidth = 5)
e.pack()
# e.insert(0, "Enter some text:")

def submit():
    hello = "System.out.println(\"" + e.get() + "\");"
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click Me", padx = 100, pady = 100, command = submit) 
# No need to add () at the end of the function
# If parameters are necessary to pass, we need to use lambda functions

myButton.pack()

root.mainloop()