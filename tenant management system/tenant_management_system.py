from tkinter import ttk,messagebox
import tkinter as tk
import ttkbootstrap as ttk

#define the main window
main_win=tk.Tk()
main_win.title("Main window")
main_win.geometry("1080x600")

#center the window to the middle of the screen
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

#define labels and buttons

#center the window and loop it
center_window(main_win)
main_win.mainloop()
