from tkinter import * 


root = Tk()

C = Canvas(root, bg = "yellow", height=250, width=300)

line = C.create_line(108, 120, 320, 40, fill="green")



C.pack()
mainloop()