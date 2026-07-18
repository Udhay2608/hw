import tkinter as tk

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password.")
    elif length < 5:
        result_label.config(text="Password Strength: Weak")
    elif length < 10:
        result_label.config(text="Password Strength: Medium")
    else:
        result_label.config(text="Password Strength: Strong")

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x250")

# UI Elements
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, show="*", width=25)
password_entry.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
