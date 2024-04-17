import customtkinter as ctk
import tkinter as tk


class Example():
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x300+100+100")
        self.root.title("Example Tkinter")
        self.root.overrideredirect(False)

        frame = tk.Frame(self.root, bg="red")
        frame.pack(side=tk.LEFT)
        frame.pack_propagate(False)
        frame.config(width=900, height=300)

        student = tk.LabelFrame(frame, text="Add Student Information")
        student.place(x=10, y=10, width=200, height=200)

        ctk.CTkLabel(student, text="Username", width=2).place(x=40, y=20)
        ctk.CTkLabel(student, text="*", text_color="red", bg_color="white").place(x=60, y=10)




if __name__ == "__main__":
    root = tk.Tk()
    obj = Example(root)
    root.mainloop()


