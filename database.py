from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Database')
root.geometry("400x400")

# Create DB or connect to pre-existing one
conn = sqlite3.connect('LEARNtkinterDB.db')

cursor = conn.cursor()
# Create a table
# Commented out since the table has been created
'''
cursor.execute("""
CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)
""")
'''

def submit():
    conn = sqlite3.connect('LEARNtkinterDB.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
    {
        'first_name' : first.get(),
        'last_name' : last.get(),
        'address' : address.get(),
        'city' : city.get(),
        'state' : state.get(),
        'zipcode' : zipcode.get()
    })
    # Clear the textboxes
    first.delete(0, END)
    last.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('LEARNtkinterDB.db')
    cursor = conn.cursor()
    # Get all queries + the primary key (oid)
    cursor.execute("SELECT *, oid FROM addresses")
    data = cursor.fetchall()
    # Putting all the data into a string for a label to display
    toPrint = ''
    for datum in data:
        toPrint += str(datum) + "\n"
    queryLabel = Label(root, text = toPrint)
    queryLabel.grid(row = 8, column = 0, columnspan = 2)

# Entry boxes with labels
labelf = Label(root, text = "First Name:")
labelf.grid(row = 0, column = 0, padx = 20)
first = Entry(root, width = 30)
first.grid(row = 0, column = 1, padx = 20)

labell = Label(root, text = "Last Name:")
labell.grid(row = 1, column = 0, padx = 20)
last = Entry(root, width = 30)
last.grid(row = 1, column = 1, padx = 20)

labela = Label(root, text = "Address:")
labela.grid(row = 2, column = 0, padx = 20)
address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

labelc = Label(root, text = "City:")
labelc.grid(row = 3, column = 0, padx = 20)
city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)

labels = Label(root, text = "State:")
labels.grid(row = 4, column = 0, padx = 20)
state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

labelz = Label(root, text = "Zipcode:")
labelz.grid(row = 5, column = 0, padx = 20)
zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

# Submit Button
submit = Button(root, text = "Add to Database", command = submit)
submit.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10)

# Query Button
query = Button(root, text = "Show Records", command = query)
query.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10)

# This will update the database and save all changes
conn.commit()
conn.close()




root.mainloop()