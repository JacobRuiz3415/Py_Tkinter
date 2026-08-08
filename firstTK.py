import tkinter as tk

root = tk.Tk()
# Widgets are added here

root.title("First widget")

label = tk.Label(root, text="My program")
label.pack()
root.mainloop()