from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio")

'''
r = IntVar()
r.set(3)
'''

# Format (v1, v2) in the for loop
TUPLE = [
    ("a", "one"),
    ("b", "two"),
    ("c", "three"),
    ("d", "four")
]

string = StringVar()
string.set("a1")

for v1, v2 in TUPLE:
    Radiobutton(root, text = v1, variable = string, value = v2).pack()

def clicked(val):
    new_label = Label(root, text = val)
    new_label.pack()

'''
Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()
'''

label = Label(root, text=string.get())
label.pack()

myButton = Button(root, text = "Print Value", command = lambda: clicked(string.get()))
myButton.pack()

root.mainloop()