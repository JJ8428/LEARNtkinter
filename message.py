from tkinter import *
from PIL import ImageTk, Image
# We need this import for message boxes
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')

# Differet types of popups
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno 

def popup():
    response = messagebox.askyesno("Popup Header", "Popup Content")
    if response == 0:
        Label(root, text="Selected N").pack() # This will get response set to 1 for yes and 0 for no
    else:
        Label(root, text="Selected Y").pack()



Button(root, text="Pop Up Message", command = popup).pack()

mainloop()