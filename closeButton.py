import tkinter as tk

root = tk.Tk()
root.title("Stop button")

Label = tk.Label(root, text = "press the button to close it")
Label.pack()

button = tk.Button(root, text="Stop", width = 25, command= root.destroy)
button.pack()

root.mainloop()