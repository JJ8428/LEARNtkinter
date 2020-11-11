from tkinter import *

root = Tk()

# Label Widget, divide how you space everything grid like
myLabel1 = Label(root, text="Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text="I am in pain.").grid(row = 1, column = 1)

'''
#Put it on the main screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)
'''

root.mainloop()