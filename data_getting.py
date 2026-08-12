import tkinter as tk
#this is from google

def retrieve_data():
    # 1. Call the .get() method on your Entry widget
    user_text = my_entry.get()
    print("User entered:", user_text)

root = tk.Tk()
root.title("Get Entry Data")

# 2. Create and pack the Entry widget
my_entry = tk.Entry(root)
my_entry.pack(pady=10)

# 3. Create a Button to trigger the retrieval function
submit_btn = tk.Button(root, text="Submit", command=retrieve_data)
submit_btn.pack(pady=5)

root.mainloop()