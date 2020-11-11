from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Dropdown Menus')
root.geometry("400x400")

def println():
    label = Label(root, text = var.get()).pack()
'''
var = StringVar()
var.set("1") # This can be used to set a default variable

dropdown = OptionMenu(root, var, "1", "2", "3", "4")
dropdown.pack()
'''

options = ["1", "2", "3"]
var = StringVar()
var.set(options[0]) # Sets the default value
dropdown = OptionMenu(root, var, *options)
dropdown.pack()

btn = Button(root, text="Print selected number", command = println).pack()

root.mainloop()