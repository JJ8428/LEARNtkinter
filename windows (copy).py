from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Main Window')

def open():
    global img
    # Images have to be global for sub-windows called by functions
    top = Toplevel()
    top.title('Second Window')
    lbl = Label(top, text="This is window # 2!").pack()
    img = ImageTk.PhotoImage(Image.open("image/py.png"))
    label = Label(top, image=img).pack()
    b2 = Button(top, text="Close the 2nd window", command = top.destroy).pack()


b1 = Button(root, text="Open the second window", command = open).pack()

mainloop()