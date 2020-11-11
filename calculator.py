from tkinter import *
import time

root = Tk()
root.title("Calculator")

e = Entry(root)
e.grid(row = 0, column = 0 columnspan = 4) # padx and pady are padding for inner text to element border

# Note the e.delete and e.insert functions in their particular
def button_add(input):
    current = str(e.get())
    e.delete(0, END)    
    e.insert(0, current + str(input))

def clear():
    e.delete(0, END)

def calc():
    try:
        toCalc = e.get()
        OPcount = e.get().count("+") + e.get().count("-")
        if OPcount != 1:
            e.delete(0, END)
            e.insert(0, "ERR")
            time.sleep(1)
            e.delete(0, END)
        else:
            if "+" in toCalc:
                toCalc2 = toCalc.split("+")
                display = float(toCalc2[0]) + float(toCalc2[1])
            elif "-" in toCalc:
                toCalc2 = toCalc.split("-")
                display = float(toCalc2[0]) - float(toCalc2[1])
            e.delete(0, END)
            e.insert(0, str(display))
    except Exception as e:
        e.delete(0, END)
        e.insert(0, "ERR")
        time.sleep(1)
        e.delete(0, END)

def clear():
    e.delete(0, END) 


# Numerical buttons
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_add(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_add(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_add(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_add(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_add(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_add(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_add(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_add(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_add(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_add(0))
button_plus = Button(root, text = "+", padx = 40, pady = 20, command = lambda: button_add("+"))
button_minus = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_add("-"))
button_equal = Button(root, text = "=", padx = 40, pady = 60, command = calc)
button_clear = Button(root, text = "C", padx = 40, pady = 20, command = clear)
button_decimal = Button(root, text = ".", padx = 40, pady = 20, command = lambda: button_add("."))


button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 0)
button_decimal.grid(row = 4, column = 1)
button_clear.grid(row = 4, column = 2)
button_plus.grid(row = 1, column = 4)
button_minus.grid(row = 2, column = 4)
button_equal.grid(row = 3, column = 4, rowspan = 2)

root.mainloop()