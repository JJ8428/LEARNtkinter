from tkinter import *
from PIL import ImageTk, Image
# This is what we need to indicate statuses of file access (REQUIRED)
from tkinter import filedialog

root = Tk()
root.title('Open Files UI')

def open():
    global img
    root.filename = filedialog.askopenfile(initialdir = "/image", title = "Select an image (.png only)", filetypes=(("png files", "*.png"), ("all files", ".*")))
    path = str(root.filename).replace("<_io.TextIOWrapper name='", '').replace("' mode='r' encoding='UTF-8'>", '')
    label.forget()
    label = Label(root, text=path).pack()
    img = ImageTk.PhotoImage(Image.open(path))
    imglabel = Label(image = img).pack()

btn = Button(root, text="Select Image", command = open).pack()
root.mainloop()
