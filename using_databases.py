from tkinter import *
import sqlite3

root = Tk()
root.title("Use DataBases Tutorial")
root.geometry("400x400")

# databases
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
