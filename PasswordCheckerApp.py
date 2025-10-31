import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Calculate strength score
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Provide feedback
    if score == 5:
        feedback = "💪 Strong Password"
        color = "green"
    elif 3 <= score < 5:
        feedback = "🙂 Medium Password"
        color = "orange"
    else:
        feedback = "⚠️ Weak Password"
        color = "red"

    # Update GUI labels
    result_label.config(text=f"Score: {score}/5 → {feedback}", fg=color)
    length_label.config(text=f"Length (>=8): {'✅' if not length_error else '❌'}")
    upper_label.config(text=f"Uppercase Letter: {'✅' if not uppercase_error else '❌'}")
    lower_label.config(text=f"Lowercase Letter: {'✅' if not lowercase_error else '❌'}")
    digit_label.config(text=f"Number: {'✅' if not digit_error else '❌'}")
    special_label.config(text=f"Special Character: {'✅' if not special_char_error else '❌'}")

def on_check_click():
    password = entry.get()
    if not password:
        messagebox.showwarning("Empty Field", "Please enter a password first.")
    else:
        check_password_strength(password)

# Create GUI window
root = tk.Tk()
root.title("🔒 Password Strength Checker")
root.geometry("400x350")
root.resizable(False, False)

# UI elements
title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=on_check_click, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=5)

# Criteria labels
length_label = tk.Label(root, text="", font=("Arial", 10))
upper_label = tk.Label(root, text="", font=("Arial", 10))
lower_label = tk.Label(root, text="", font=("Arial", 10))
digit_label = tk.Label(root, text="", font=("Arial", 10))
special_label = tk.Label(root, text="", font=("Arial", 10))

length_label.pack()
upper_label.pack()
lower_label.pack()
digit_label.pack()
special_label.pack()

root.mainloop()
