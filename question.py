import tkinter as tk

root = tk.Tk()
v = tk.StringVar(value=1)

def checkAwnswer():
    answer = "2"
    if(v.get() == answer):
        print("correct")
    else:
        print("wrong")


label = tk.Label(root, text="what is two plus two")
label.pack()

tk.Radiobutton(root, text="3", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="4", variable=v, value=2).pack(anchor=tk.W)

#get value from button
btn = tk.Button(root, text="Submit", command=checkAwnswer)
btn.pack()

root.mainloop()