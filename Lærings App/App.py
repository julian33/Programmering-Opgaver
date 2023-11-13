import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter UI")

# Create a label to display text
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
