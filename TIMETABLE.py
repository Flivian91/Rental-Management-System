
import tkinter as tk
from customtkinter import*


class TimeTable():
  def __init__(self, root):
    self.root = root
    self.root.geometry("350x540+300+30")
    self.root.config(bg="#4b4bc1")

    CTkLabel(self.root, text="<- NTURIRI SECONDARY SCHOOL ->", fg_color="white", bg_color="#4b4b51", width=350).place(x=0, y=5)


    CTkLabel(self.root, text="School", fg_color="#4b4bc1", bg_color="#4b4b51", width=350, anchor=W).place(x=5, y=350)
    # School Logo 
    self.school_var = tk.StringVar()
    school = CTkEntry(self.root, width=340, bg_color="white",textvariable=self.school_var, fg_color="white", height=20, corner_radius=0, border_width=0 )
    school.place(x=5, y=380)

    CTkLabel(self.root, text="Licence", fg_color="#4b4bc1", bg_color="#4b4b51", width=350, anchor=W).place(x=5, y=400)
    # School Logo 
    licence= CTkEntry(self.root, width=340, bg_color="white", fg_color="white", height=20, corner_radius=0, border_width=0 )
    licence.place(x=5, y=430)


    CTkLabel(self.root, text="Serial Number", fg_color="#4b4bc1", bg_color="#4b4b51", width=350, anchor=W).place(x=5, y=450)
    # School Logo 
    licence= CTkEntry(self.root, width=340, bg_color="white", fg_color="white", height=20, corner_radius=0, border_width=0 )
    licence.place(x=5, y=480)

    check_btn = CTkButton(self.root, text="Check", command=self.click, width=100, height=35, fg_color="green", border_width=0)
    check_btn.place(x=180, y=505)



    # Function Definition for the check button
  def click(self):
    if self.school_var.get()=="":
        CTkLabel(self.root, text="Fill School Name", fg_color="#4b4bc1", bg_color="#4b4b51", anchor=W).place(x=5, y=505)
      


    





    





if __name__ == "__main__":
  root = tk.Tk()
  TimeTable(root)
  root.mainloop()
