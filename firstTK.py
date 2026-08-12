import tkinter as tk
#used to create the main window
root = tk.Tk()
# Widgets are added here

root.title("First widget")

label = tk.Label(root, text="My Program is being displayed here")
label.pack()
root.mainloop()