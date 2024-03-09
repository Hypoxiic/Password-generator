import string
import secrets
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_password():
    characters = ""
    if not any([lowercase_var.get(), uppercase_var.get(), digits_var.get(), special_var.get()]):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    exclude_chars = exclude_chars_var.get()
    if exclude_chars:
        characters = ''.join(c for c in characters if c not in exclude_chars)

    length = length_var.get()
    if length < 1:
        messagebox.showerror("Error", "Password length should be at least 1.")
    elif length > len(characters):
        messagebox.showerror("Error", "Password length should not exceed the number of available characters.")
    else:
        password_chars = [secrets.choice(characters) for _ in range(length)]
        password.set("".join(password_chars))

root = tk.Tk()
root.title("Password Generator")
main_frame = ttk.Frame(root, padding=20)
main_frame.grid()

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")
length_var = tk.IntVar(value=8)
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, sticky="w")

char_types_frame = ttk.LabelFrame(main_frame, text="Character Types", padding=10)
char_types_frame.grid(row=1, column=0, columnspan=2, sticky="w")

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = ttk.Checkbutton(char_types_frame, text="Lowercase", variable=lowercase_var)
lowercase_check.grid(row=0, column=0, sticky="w")

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = ttk.Checkbutton(char_types_frame, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=0, column=1, sticky="w")

digits_var = tk.BooleanVar(value=True)
digits_check = ttk.Checkbutton(char_types_frame, text="Digits", variable=digits_var)
digits_check.grid(row=0, column=2, sticky="w")

special_var = tk.BooleanVar(value=True)
special_check = ttk.Checkbutton(char_types_frame, text="Special Characters", variable=special_var)
special_check.grid(row=0, column=3, sticky="w")

exclude_chars_label = ttk.Label(main_frame, text="Exclude Characters:")
exclude_chars_label.grid(row=2, column=0, sticky="w")
exclude_chars_var = tk.StringVar()
exclude_chars_entry = ttk.Entry(main_frame, textvariable=exclude_chars_var, width=30)
exclude_chars_entry.grid(row=2, column=1, sticky="w")

generate_button_frame = ttk.Frame(main_frame)
generate_button_frame.grid(row=3, column=0, columnspan=2, pady=10)

generate_button = ttk.Button(generate_button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side="left", padx=5)

password = tk.StringVar()
password_entry = ttk.Entry(generate_button_frame, textvariable=password, width=30, state="readonly")
password_entry.pack(side="left", padx=5)

root.mainloop()