'''
import tkinter as tk

root = tk.Tk()
main_frame = tk.Frame(root, border=3, relief=tk.GROOVE)
main_frame.grid()

for i in range(10):

    #Create Labels for numbering the rows:
    tk.Label(main_frame, 
            text=str(i+1), 
            border=1,
            relief=tk.GROOVE,
            padx=20,
            pady=20,
            ).grid(column=0, row=i)

    #Create Frames with a Label inside:
    frame = tk.Frame(main_frame,
        border=1,
        relief=tk.GROOVE,
        background="blue",
    )

    frame.grid(row=0, column=i+1, rowspan=i+1, sticky=tk.N+tk.S)

    tk.Label(frame, 
            text='Rowspan {}'.format(i+1), 
            border=1,
            relief=tk.GROOVE,
            padx=20,
            pady=20,).grid()

root.mainloop() 
'''
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

height = 20

label_frame = tk.Frame(root,width=700,height=height,bg="white")
label_frame.pack_propagate(0) # Stops child widgets of label_frame from resizing it
tk.Label(label_frame,bg="white",fg="black",text="test",font=("Calibri",15)).pack()
label_frame.place(x=10,y=10)

root.mainloop()