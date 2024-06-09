#!/usr/bin/env python3

import tkinter as tk

def submit_name():
    name = name_entry.get()
    if name:
        hello_label.config(text="Hello " + name + "!")

def clear_name():
    name_entry.delete(0, tk.END)
    hello_label.config(text="")

# Create the main application window
root = tk.Tk()
root.title("Name Greeting App")

# Create labels
label_prompt = tk.Label(root, text="Enter your name:")
label_prompt.grid(row=0, column=0, padx=5, pady=10)

hello_label = tk.Label(root, text="")
hello_label.grid(row=1, column=0, padx=5, pady=5)

# Create text entry widget
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Create buttons
submit_button = tk.Button(root, text="Submit", command=submit_name)
submit_button.grid(row=1, column=1, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_name)
clear_button.grid(row=1, column=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
