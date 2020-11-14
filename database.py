from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Database')

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
        toPrint += str(datum[0]) + " " + str(datum[1]) + " " + str(datum[-1])
        if datum != data[-1]:
            toPrint += "\n"
    queryLabel = Label(root, text = toPrint)
    queryLabel.grid(row = 7, column = 0, columnspan = 2)

def delete():
    conn = sqlite3.connect('LEARNtkinterDB.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM addresses WHERE oid=" + to_del.get())
    print("DELETE FROM addresses WHERE oid=" + to_del.get())
    conn.commit()
    conn.close()

def update():

    # Function to actually write into the database
    def upd():
        conn = sqlite3.connect('LEARNtkinterDB.db')
        cursor = conn.cursor()
        record_id = to_upd.get()
        cursor.execute("""
        UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid
        """,
        {
            'first' : first_upd.get(),
            'last' : last_upd.get(),
            'address' : address_upd.get(),
            'city' : city_upd.get(),
            'state' : state_upd.get(),
            'zipcode' : zipcode_upd.get(),

            'oid' : record_id
        })
        conn.commit()
        conn.close()
        tmp.destroy()
        
    
    # This function renders the window to do enter updated info
    # Will display info prior to change.
    conn = sqlite3.connect('LEARNtkinterDB.db')
    cursor = conn.cursor()
    tmp = Tk()
    tmp.title('Update Record') 
    # Make the entries GLOBAL
    global first_upd
    global last_upd
    global address_upd
    global city_upd
    global state_upd
    global zipcode_upd
    # Entry boxes with labels
    labelf_upd = Label(tmp, text = "First Name:")
    labelf_upd.grid(row = 0, column = 0)
    first_upd = Entry(tmp)
    first_upd.grid(row = 0, column = 1)
    labell_upd = Label(tmp, text = "Last Name:")
    labell_upd.grid(row = 1, column = 0)
    last_upd = Entry(tmp)
    last_upd.grid(row = 1, column = 1)
    labela_upd = Label(tmp, text = "Address:")
    labela_upd.grid(row = 2, column = 0)
    address_upd = Entry(tmp)
    address_upd.grid(row = 2, column = 1)
    labelc_upd = Label(tmp, text = "City:")
    labelc_upd.grid(row = 3, column = 0)
    city_upd = Entry(tmp)
    city_upd.grid(row = 3, column = 1)
    labels_upd = Label(tmp, text = "State:")
    labels_upd.grid(row = 4, column = 0)
    state_upd = Entry(tmp)
    state_upd.grid(row = 4, column = 1)
    labelz_upd = Label(tmp, text = "Zipcode:")
    labelz_upd.grid(row = 5, column = 0)
    zipcode_upd = Entry(tmp)
    zipcode_upd.grid(row = 5, column = 1)
    # Get query info of that ID
    record_id = to_upd.get()
    cursor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    data = cursor.fetchall()
    for datum in data:
        first_upd.insert(0, datum[0])
        last_upd.insert(0, datum[1])
        address_upd.insert(0, datum[2])
        city_upd.insert(0, datum[3])
        state_upd.insert(0, datum[4])
        zipcode_upd.insert(0, datum[5])
    # Submit the update
    submit_upd = Button(tmp, text = "Save Record", command = upd)
    submit_upd.grid(row = 6, column = 0, columnspan = 2)
    tmp.mainloop()

# Entry boxes with labels
labelf = Label(root, text = "First Name:")
labelf.grid(row = 0, column = 0)
first = Entry(root)
first.grid(row = 0, column = 1)
labell = Label(root, text = "Last Name:")
labell.grid(row = 1, column = 0)
last = Entry(root)
last.grid(row = 1, column = 1)
labela = Label(root, text = "Address:")
labela.grid(row = 2, column = 0)
address = Entry(root)
address.grid(row = 2, column = 1)
labelc = Label(root, text = "City:")
labelc.grid(row = 3, column = 0)
city = Entry(root)
city.grid(row = 3, column = 1)
labels = Label(root, text = "State:")
labels.grid(row = 4, column = 0)
state = Entry(root)
state.grid(row = 4, column = 1)
labelz = Label(root, text = "Zipcode:")
labelz.grid(row = 5, column = 0)
zipcode = Entry(root)
zipcode.grid(row = 5, column = 1)

# Submit Button
submit = Button(root, text = "Add to Database", command = submit)
submit.grid(row = 6, column = 0)

# Query Button
query = Button(root, text = "View All", command = query)
query.grid(row = 6, column = 1)

# Delete Menu 
to_del = Entry(root)
to_del.grid(row = 8, column = 0)
delete = Button(root, text = "Delete", command = delete)
delete.grid(row = 8, column = 1)

# Update Menu
to_upd = Entry(root)
to_upd.grid(row = 9, column = 0)
update = Button(root, text = "Update", command = update)
update.grid(row = 9, column = 1)

# This will update the database and save all changes
conn.commit()
conn.close()




root.mainloop()