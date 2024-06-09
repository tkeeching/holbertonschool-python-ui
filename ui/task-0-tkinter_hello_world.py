#!/usr/bin/env python3

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Hello World App")
root.geometry("250x120")

# Create the labels
label_hello = tk.Label(root, text="Hello")
label_hello.pack()  # Pack the "Hello" label to display it

label_world = tk.Label(root, text="World")
label_world.pack()  # Pack the "World!" label to display it

# Run the Tkinter event loop
root.mainloop()
