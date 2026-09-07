from tkinter import * 


root = Tk()
root.title("Canvas")

C = Canvas(root, bg = "yellow", height=250, width=300)

oval = C.create_oval(50, 50, 150, 150, fill="blue")
oval = C.create_oval(75, 50, 85, 50, fill="black")
oval = C.create_oval(50, 50, 125, 100, fill="black")

line = C.create_line(108, 120, 100, 40, fill="green")

C.pack()
mainloop()