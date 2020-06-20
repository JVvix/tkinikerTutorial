from tkinter import *

root = Tk()
root.title("Radio Buttons")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#Radiobutton(root, text="Option One", variable=r, value=1, command=lambda: click(r.get())).pack()
#Radiobutton(root, text="Option Two", variable=r, value=2, command=lambda: click(r.get())).pack()

myButton = Button(root, text="Order!", command=lambda: click(pizza.get()))
myButton.pack()

mainloop()
