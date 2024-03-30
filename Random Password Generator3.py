import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True  
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def generate_password_handler():
    min_length = int(min_length_entry.get())
    has_number = number_var.get() == 1
    has_special = special_var.get() == 1
    pwd = generate_password(min_length, has_number, has_special)
    messagebox.showinfo("Generated Password", f"The generated password is: {pwd}")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create frames
frame1 = tk.Frame(root)
frame1.pack(pady=10)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

# Create widgets
label1 = tk.Label(frame1, text="Minimum Length:")
label1.grid(row=0, column=0, padx=5)

min_length_entry = tk.Entry(frame1)
min_length_entry.grid(row=0, column=1, padx=5)

number_var = tk.IntVar(value=1)
number_check = tk.Checkbutton(frame2, text="Include Numbers", variable=number_var)
number_check.grid(row=0, column=0, padx=5)

special_var = tk.IntVar(value=1)
special_check = tk.Checkbutton(frame2, text="Include Special Characters", variable=special_var)
special_check.grid(row=0, column=1, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_handler)
generate_button.pack(pady=10)

# Run the GUI
root.mainloop()

