import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest (compounded annually)
        ci = p * ((1 + r/100) ** t) - p

        result_label.config(
            text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}"
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("350x300")

# Labels and Inputs
tk.Label(root, text="Principal Amount:").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Time Period (years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Rate of Interest (%):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

# Button
tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
