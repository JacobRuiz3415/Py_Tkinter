from tkinter import *
root = Tk()

root.title("Paint App")
root.geometry("500x500")

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)

    color = "#000fff000"

    w.create_line(x1, y1, x2, y2, fill=color)

w = Canvas(root, width=500, height=500)

w.bind("<B1-Motion>" , paint)

l = Label(root, text= "")
l.pack()
w.pack()

mainloop()