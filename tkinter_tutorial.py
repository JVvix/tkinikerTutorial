from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Add Frames to Your Program")
root.iconbitmap('icon.ico')

frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click This!")
b.grid(row=0, column=0)

b2 = Button(frame, text="or here!")
b2.grid(row=2, column=0)

root.mainloop()
