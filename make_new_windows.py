from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Create New Windows in tKinter")
root.iconbitmap("icon.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("My Second Window")
    top.iconbitmap("icon.ico")
    my_img = ImageTk.PhotoImage(Image.open("images.jpg"))
    my_label = Label(top, image=my_img).pack()

btn = Button(root, text="Open another world", command=open).pack()

mainloop()
