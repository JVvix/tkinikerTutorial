from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

def popup():
    messagebox.showwarning("warning", "you suck because you got a warning")

Button(root, text="Popup", command=popup).pack()

mainloop()
