from tkinter import * 


root = Tk()

C = Canvas(root, bg = "yellow", height=250, width=300)

line = C.create_line(108, 120, 320, 40, fill="green")

oval = C.create_oval(50, 50, 100, 100, fill="blue")
oval = C.create_oval(50, 50, 10, 10, fill="black")
oval = C.create_oval(80, 50, 10, 10, fill="black")


C.pack()
mainloop()