import tkinter as tk

root = tk.Tk()

root.title("adding number")

tk.Label(root, text="First Number:").grid(row= 0, column= 0)
tk.Label(root, text="Second Number:").grid(row= 1, column= 1)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column= 1)
entry2.grid(row=1, column= 1)

button = tk.Button(root, text = "Submit", command= root.destroy)
button.grid(row=4, column=0)

root.mainloop()
print(entry1.get)
print(entry2.get)