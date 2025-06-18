from tkinter import *
import random
#Turtle (Canvas)
def Shape(length, side):
    import turtle
    X = turtle.Turtle()
    X.speed(1)
    for n in range(side):
         c = random.choice(["blue", "yellow", "red", "green", "cyan", "orange"])
         X.color(c)
         X.forward(length)
         X.right(180 -(((side - 2) * 180) / side))
    return()

#Tkinter (GUI)
root = Tk()
root.title("hello")
label = Label(root, text="Length of sides").grid(row=1, column=1)
label1 = Label(root, text="number of sides").grid(row=1, column=2)
label2 = Label(root, text="               ").grid(row=3, column=2)
entry1 = Entry(root)
entry1.grid(row=2, column=1)
entry2 = Entry(root)
entry2.grid(row=2, column=2)
def click():
     A = int(entry1.get())
     B = int(entry2.get())
     Shape(A, B)
     return()
button = Button(root, text = "Submit", command=click).grid(row=4, column=3)
root.mainloop()

