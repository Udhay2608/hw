import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\nResult: {result}"
    )

# Main window
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("350x300")

tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=12, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=12, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissor", width=12, command=lambda: play("Scissor")).pack(pady=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
