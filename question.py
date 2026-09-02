import tkinter as tk

root = tk.Tk()
v = tk.StringVar()

def checkAwnswer():
    print(f"{v.get()}")

tk.Radiobutton(root, text="A", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="B", variable=v, value=2).pack(anchor=tk.W)

#get value from button
btn = tk.Button(root, text="Submit", command=checkAwnswer)
btn.pack()

root.mainloop()