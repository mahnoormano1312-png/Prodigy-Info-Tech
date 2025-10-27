import tkinter as tk
from tkinter import messagebox, ttk

# Caesar Cipher function
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'a' <= char <= 'z':
            start = ord('a')
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            result += char
    return result


# GUI function for encryption/decryption
def process_text():
    text = text_entry.get("1.0", tk.END).strip()
    shift_value = shift_entry.get()
    mode = mode_var.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    if not shift_value.isdigit():
        messagebox.showwarning("Input Error", "Shift value must be a number.")
        return

    shift = int(shift_value)
    result = caesar_cipher(text, shift, mode)
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
    output_text.config(state='disabled')


# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("600x500")
root.configure(bg="#1e1e2f")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 11, "bold"), padding=6, background="#00adb5", foreground="white")
style.map("TButton", background=[("active", "#00ced1")])

# Title Label
title_label = tk.Label(root, text="🔐 Caesar Cipher Encryption & Decryption Tool", 
                       font=("Helvetica", 16, "bold"), bg="#1e1e2f", fg="#00adb5")
title_label.pack(pady=15)

# Frame for Inputs
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

# Text Input
tk.Label(frame, text="Enter Text:", font=("Arial", 12), bg="#1e1e2f", fg="white").grid(row=0, column=0, sticky="w")
text_entry = tk.Text(frame, width=60, height=5, font=("Courier New", 11), wrap="word", bg="#2b2b3d", fg="white")
text_entry.grid(row=1, column=0, columnspan=2, pady=5)

# Shift Input
tk.Label(frame, text="Shift Value:", font=("Arial", 12), bg="#1e1e2f", fg="white").grid(row=2, column=0, sticky="w", pady=5)
shift_entry = tk.Entry(frame, font=("Arial", 11), width=10, bg="#2b2b3d", fg="white", insertbackground="white")
shift_entry.grid(row=2, column=1, sticky="w", pady=5)

# Mode Selection
tk.Label(frame, text="Mode:", font=("Arial", 12), bg="#1e1e2f", fg="white").grid(row=3, column=0, sticky="w", pady=5)
mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(frame, text="Encrypt", variable=mode_var, value="encrypt", 
                               font=("Arial", 11), bg="#1e1e2f", fg="white", selectcolor="#2b2b3d")
decrypt_radio = tk.Radiobutton(frame, text="Decrypt", variable=mode_var, value="decrypt", 
                               font=("Arial", 11), bg="#1e1e2f", fg="white", selectcolor="#2b2b3d")
encrypt_radio.grid(row=3, column=1, sticky="w")
decrypt_radio.grid(row=3, column=1, sticky="e")

# Process Button
process_button = ttk.Button(root, text="🔄 Process", command=process_text)
process_button.pack(pady=15)

# Output
tk.Label(root, text="Result:", font=("Arial", 12), bg="#1e1e2f", fg="white").pack()
output_text = tk.Text(root, width=65, height=6, font=("Courier New", 11), wrap="word", bg="#2b2b3d", fg="#00ffcc")
output_text.pack(pady=5)
output_text.config(state='disabled')

# Footer
footer = tk.Label(root, text="Developed by [Your Name] | For Educational Use", 
                  font=("Arial", 9), bg="#1e1e2f", fg="#aaaaaa")
footer.pack(side="bottom", pady=10)

root.mainloop()