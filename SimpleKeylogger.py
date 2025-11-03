"""
Safe in-app keystroke logger for learning/testing.
- Captures key events that occur when this window has focus.
- Logs timestamped events to a file you choose.
- Includes explicit consent notice and start/stop controls.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

LOG_HEADER = (
    "IN-APP KEYLOG (ONLY KEYS PRESSED INSIDE THIS APP)\n"
    "User consent: You are using this program to record your own keystrokes.\n"
    "Do NOT use this for other people's keystrokes without consent.\n\n"
)

class InAppLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("In-App Keystroke Logger (Safe)")
        self.log_file_path = None
        self.logging = False

        # UI
        self.text = tk.Text(root, width=60, height=20, wrap="word")
        self.text.pack(padx=8, pady=8)

        controls = tk.Frame(root)
        controls.pack(pady=(0,8))

        self.start_btn = tk.Button(controls, text="Start Logging", command=self.start_logging)
        self.start_btn.grid(row=0, column=0, padx=6)

        self.stop_btn = tk.Button(controls, text="Stop Logging", command=self.stop_logging, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=6)

        self.choose_btn = tk.Button(controls, text="Choose Log File", command=self.choose_log_file)
        self.choose_btn.grid(row=0, column=2, padx=6)

        self.clear_btn = tk.Button(controls, text="Clear Text", command=self.clear_text)
        self.clear_btn.grid(row=0, column=3, padx=6)

        self.status_label = tk.Label(root, text="Logging: OFF · No log file chosen", anchor="w")
        self.status_label.pack(fill="x", padx=8)

        # Bind key event for the text widget only (in-app)
        self.text.bind("<Key>", self.on_key_event)

        # Show consent notice the first time
        messagebox.showinfo("Consent & Ethics",
            "This app records keystrokes typed inside this window only.\n"
            "Do not use it to record other people's keystrokes without explicit consent."
        )

    def choose_log_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Choose file to save keystroke log"
        )
        if path:
            self.log_file_path = path
            # create file and write header if empty
            try:
                with open(self.log_file_path, "a", encoding="utf-8") as f:
                    if f.tell() == 0:
                        f.write(LOG_HEADER)
                self.update_status()
            except Exception as e:
                messagebox.showerror("File Error", f"Could not open log file:\n{e}")
                self.log_file_path = None

    def start_logging(self):
        if not self.log_file_path:
            messagebox.showwarning("No file", "Please choose a log file before starting.")
            return
        self.logging = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.update_status()

    def stop_logging(self):
        self.logging = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.update_status()

    def clear_text(self):
        self.text.delete("1.0", tk.END)

    def update_status(self):
        file_info = self.log_file_path if self.log_file_path else "No log file chosen"
        state = "ON" if self.logging else "OFF"
        self.status_label.config(text=f"Logging: {state} · {file_info}")

    def on_key_event(self, event):
        """
        This function is called only for keys pressed while the Text widget has focus.
        event.keysym contains a readable name (e.g., 'a', 'Return', 'BackSpace').
        event.char contains the character (may be empty for special keys).
        """
        # Record only when logging is enabled
        if not self.logging or not self.log_file_path:
            return

        timestamp = datetime.utcnow().isoformat(sep=" ", timespec="seconds") + " UTC"
        key_name = event.keysym  # readable key name
        char = event.char if event.char else ""  # actual typed char if any

        # Create a safe log line - avoid writing raw binary
        log_line = f"{timestamp} | keysym={key_name} | char={repr(char)}\n"

        try:
            with open(self.log_file_path, "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception as e:
            # On file error, stop logging and notify
            self.logging = False
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            self.update_status()
            messagebox.showerror("Write Error", f"Could not write to log file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InAppLogger(root)
    root.mainloop()
