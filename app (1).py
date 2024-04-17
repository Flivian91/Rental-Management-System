import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.info_var = tk.StringVar()

        self.label = tk.Label(root, text="Enter Information:")
        self.label.pack()

        self.entry = tk.Entry(root, textvariable=self.info_var)
        self.entry.pack()

        self.open_first_button = tk.Button(root, text="Open First Second Window", command=self.open_first_window)
        self.open_first_button.pack()

        self.open_second_button = tk.Button(root, text="Open Second Second Window", command=self.open_second_window)
        self.open_second_button.pack()

        self.second_window = None  # Variable to store the reference to the open SecondWindow

    def open_first_window(self):
        self.open_window("")

    def open_second_window(self):
        self.open_window("")

    def open_window(self, window_name):
        if self.second_window:
            # If a SecondWindow is already open, close it before opening a new one
            self.second_window.destroy()

        info_text = self.info_var.get()

        if info_text:
            self.second_window = tk.Toplevel(self.root)
            SecondWindow(self.second_window, info_text, window_name)
            self.root.withdraw()  # Hide the main window
        else:
            messagebox.showwarning("Warning", "Please enter information before opening the second window.")

class SecondWindow:
    def __init__(self, root, info_text, window_name):
        self.root = root
        self.root.title(f"{window_name} Second Window")

        self.info_label = tk.Label(root, text=f"Received Information: {info_text}")
        self.info_label.pack()

        self.close_button = tk.Button(root, text=f"Close {window_name} Second Window", command=self.close_second_window)
        self.close_button.pack()

    def close_second_window(self):
        self.root.destroy()  # Destroy the second window
        # The main window is not explicitly shown here; it will be shown when the corresponding button is clicked in MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
