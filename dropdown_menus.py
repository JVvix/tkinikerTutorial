from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menu Tutorial")
root.iconbitmap("icon.ico")
root.geometry("400x400")

options = [
        "Monday",
        "Tuesday",
        "Wedensday",
        "Thursday",
        "Friday",
        "Saturday"
]

def show():
    myLabel = Label(root, text=clicked.get()).pack()
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
