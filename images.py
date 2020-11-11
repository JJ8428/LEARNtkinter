from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Lets put an image up on here')

# root.iconbitmap('icons/construction.xbm')
# This has an issue with the icon file itself
# Linux prefers .xbm whereas windows prefers .ico

# Images are put in a ImageTk object and then put in a label
img = ImageTk.PhotoImage(Image.open("image/py.png"))
label = Label(image = img)
label.pack()

# Exit button
button_quit = Button(root, text = "Exit GUI", command = root.quit)
button_quit.pack()

root.mainloop()