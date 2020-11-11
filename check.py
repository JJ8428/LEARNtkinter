from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Boiler Plate')
root.geometry("400x400")

# var1 = IntVar()
# 1 means checked, 0 means not checked
var1 = StringVar()

def show():
    label = Label(root, text = var1.get()).pack()

check1 = Checkbutton(root, text = "Checkbox 1", variable = var1, onvalue = "Yes", offvalue = "No")
check1.deselect() # Deselect is needed due to a bug in tkinter when checkboxes have custom on/off values
check1.pack()

btn = Button(root, text="Is the checkbox selected?", command = show).pack()

root.mainloop()