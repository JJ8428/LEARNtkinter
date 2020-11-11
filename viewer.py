from tkinter import *
from PIL import ImageTk, Image

root = Tk()

img1 = ImageTk.PhotoImage(Image.open("image/cpp.png"))
img2 = ImageTk.PhotoImage(Image.open("image/java.png"))
img3 = ImageTk.PhotoImage(Image.open("image/php.png"))
img4 = ImageTk.PhotoImage(Image.open("image/py.png"))
imglist = [img1, img2, img3, img4]
index = 0
label = Label(root, image = imglist[index])
label.grid(row = 0, column = 0, columnspan = 3)
status = Label(root, text= "Index:(" + str(index + 1) + "/4")
status.grid(row = 1, column = 1, bd = 1, relief = SUNKEN)


def forward():
    # Surprisingly, I never used global variables in Python until now
    global index
    global label
    global status
    index += 1
    if index == 4:
        index = 0
    label.grid_forget()
    status.forget()
    # Forget lets the tkinter thread expire, so it can render after any updates, hence why it shifts everywhere
    # Casts updates down here
    label = Label(root, image = imglist[index])
    label.grid(row = 0, column = 0, columnspan = 3)
    status = Label(root, text= "Index:(" + str(index + 1) + "/4)")
    status.grid(row = 1, column = 1)

    

def back():
    global index
    global label
    global status
    index -= 1
    if index == -1:
        index = 3
    label.grid_forget()
    status.forget()
    label = Label(root, mage = imglist[index])
    label.grid(row = 0, column = 0, columnspan = 3)
    status = Label(root, text= "Index:(" + str(index + 1) + "/4")
    status.grid(row = 1, column = 1)



root.title("What are some languages I know?")

button_back = Button(root, text="<<", command = back)
button_forward = Button(root, text=">>", command = forward)
button_back.grid(row = 1, column = 0)
button_forward.grid(row = 1, column = 2)

root.mainloop()
