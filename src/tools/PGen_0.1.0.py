import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        result_label.config(text="Please enter a valid length")
        return

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    result_label.config(text="Generated Password: " + password)
    generated_password.set(password)
    copy_button.grid(row=2, columnspan=2)  # Show the copy button after generating password

def copy_to_clipboard():
    password = generated_password.get()
    if password:
        pyperclip.copy(password)
        result_label.config(text="Password copied to clipboard")
    else:
        result_label.config(text="No password generated yet")

# Create the main window
root = tk.Tk()
root.title("PGen")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position
window_width = 400
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame for the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Length Label
length_label = ttk.Label(frame, text="Length:")
length_label.grid(column=0, row=0, sticky=tk.W)

# Length Entry
length_entry = ttk.Entry(frame, width=10)
length_entry.grid(column=1, row=0, sticky=tk.W)
length_entry.insert(tk.END, "12")

# Generate Button
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=1, columnspan=2)

# Copy to Clipboard Button (initially hidden)
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(column=0, row=2, columnspan=2)
copy_button.grid_remove()  # Hide the copy button initially

# Result Label
result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2)

# Variable to store generated password
generated_password = tk.StringVar()

# Start the GUI event loop
root.mainloop()
