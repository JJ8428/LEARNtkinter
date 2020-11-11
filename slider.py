
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("400x400")
'''
vertical = Scale(root, from_=0, to=200)
vertical.pack()
'''
label = Label()
def slide():
	label = Label(root, text=horizontal.get()).pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

btn = Button(root, text="Update", command=slide).pack()

root.mainloop()