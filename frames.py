from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text = "Test Frame 123", padx = 5, pady = 5) # Inside padding
frame.pack(padx = 5, pady = 5) # Outside padding

# Button now in the frame
b1 = Button(frame, text = "Test Button 1 in Frame")
b1.grid(row = 0, column = 0)
b2 = Button(frame, text = "Test Button 2 in Frame")
b2.grid(row = 0, column = 1)

root.mainloop()