import tkinter as tk

def retrieve_vardata():

    number1 = int(entry1.get())
    print(number1)

    number2 = int(entry2.get())
    print(number2)
    print(f'sum of {number1} and {number2} is {number1 + number2}')

root = tk.Tk()

root.title("Adding Numbers")

tk.Label(root, text="First Number:").grid(row= 0, column= 0)
tk.Label(root, text="Second Number:").grid(row= 1, column= 0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column= 1)
entry2.grid(row=1, column= 1)

button = tk.Button(root, text = "Submit", command= retrieve_vardata)
button.grid(row=3, column=1)

root.mainloop()
