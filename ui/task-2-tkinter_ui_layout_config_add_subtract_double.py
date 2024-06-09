#!/usr/bin/env python3

import tkinter as tk

def add_one():
    global value
    value += 1
    update_label()

def subtract_one():
    global value
    value -= 1
    update_label()

def double_value():
    global value
    value *= 2
    update_label()

def reset_value():
    global value
    value = 0
    update_label()

def update_label():
    value_label.config(text=str(value))

# Global variable to hold the value
value = 0

# Create the main application window
root = tk.Tk()
root.title("Value Manipulation App")

# Create buttons
button_add = tk.Button(root, text="Add one", command=add_one)
button_add.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

button_subtract = tk.Button(root, text="Subtract one", command=subtract_one)
button_subtract.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

button_double = tk.Button(root, text="Double", command=double_value)
button_double.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# Create value label
value_label = tk.Label(root, text=str(value))
value_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create reset button
reset_button = tk.Button(root, text="Reset", command=reset_value)
reset_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Configure grid weights
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the Tkinter event loop
root.mainloop()
