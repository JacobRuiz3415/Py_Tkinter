import tkinter as tk

root = tk.Tk()

tk.Label(root, text="First Number:").grid(row= 0, column= 0)
tk.Label(root, text="Second Number:").grid(row= 1, column= 1)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column= 1)
entry2.grid(row=1, column= 1)



root.mainloop()
print(entry1)
print(entry2)