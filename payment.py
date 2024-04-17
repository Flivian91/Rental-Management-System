import tkinter as tk
from tkinter.simpledialog import askinteger
 
class SettingsWindow:
    def __init__(self, func):
        self.win = tk.Toplevel()
        self.func = func
 
        frame = tk.Frame(self.win)
        frame.pack(padx=5, pady=5)
        self.label=tk.Label(frame, text="Settings Window")
        self.label.pack(padx=20, pady=5)
 
        self.var = tk.IntVar()
        radio=tk.Radiobutton(frame, text = "Option 1", value = 1, 
                             variable=self.var, command=self.ParentFunc)
        radio.pack(padx = 10, pady = 5)
        radio2=tk.Radiobutton(frame, text = "Option 2", value = 2,
                              variable=self.var, command=self.ParentFunc)
        radio2.pack(padx = 10, pady = 5)
 
    def ParentFunc(self):
        self.func(self.var.get())
 
 
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.settings = None
        self.SettingsValue = None
 
        self.frame = tk.Frame(self.master, width=200, height=200)
        self.frame.pack()
 
        self.button = tk.Button(self.frame, text="Settings Window", 
                                command=self.openSettings)
        self.button.place(x=50, y=50)
 
        self.button2 = tk.Button(self.frame, text = "Update Settings", 
                                command = self.updateLabelinSettings)
        self.button2.place(x=50, y=150)
 
 
    def update(self, n):
        self.SettingsValue = n
        print(self.SettingsValue)
 
    def openSettings(self):
        self.settings = SettingsWindow(self.update)
 
    def updateLabelinSettings(self):
        prompt = askinteger("Input", "Input an Integer")
        if self.settings != None:
            self.settings.label.configure(text="Updated")
 
root = tk.Tk()
window = MainWindow(root)
root.mainloop()