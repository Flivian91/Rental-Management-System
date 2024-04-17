import tkinter as tk
from tkinter import ttk

def submit_form():
    # You can access the entry values here and process them as needed
    print("Name:", entry_name.get())
    print("Email:", entry_email.get())
    # Add more fields as needed

# Create the main window
root = tk.Tk()
root.title("Entry Form")

# Create a custom style for rounded entry fields
style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=5, relief="ridge", bordercolor="white", foreground="black", padding=(10, 5))

# Create and configure the Entry widgets using ttk.Entry with the custom style
entry_name = ttk.Entry(root, style="Rounded.TEntry")
entry_email = ttk.Entry(root, style="Rounded.TEntry")

# Create and configure the labels
label_name = ttk.Label(root, text="Name:")
label_email = ttk.Label(root, text="Email:")

# Create and configure the Submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)

# Arrange widgets using the grid layout manager
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_email.grid(row=1, column=1, padx=10, pady=5)

submit_button.grid(row=2, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
