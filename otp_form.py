import tkinter as tk
import customtkinter as ctk
import random as rad
from tkinter import messagebox
import time as time
from change_password import Password_change


class Otp_form():
    def __init__(self,root):
        self.root = root
        self.root.title("O.T.P Management System")
        self.root.geometry('550x450+330+90')
        self.root.resizable(False, False)
        self.root.config(background="light gray")

        # Create a four digit otp number
        self.random_otp = rad.randint(1000, 9999) 
        print(self.random_otp)
        # time.sleep(3)

        # self.mes = messagebox.showinfo(title="OTP Number", message=f"Your OTP Code is: {str(self.random_otp)}", parent=self.root)

        
        ctk.CTkLabel(self.root, text="Enter The OTP Sent To Your Email!", font=("Bookman Old Style", 18), width=550, height=35, fg_color="light gray").place(x=0, y=5)
        ctk.CTkLabel(self.root, text="Click Resend If Not Sent!", font=("Bookman Old Style", 18), width=550, height=35, fg_color="light gray").place(x=0, y=410)


        # Main Frame to Hold Entry widget and submit button
        frame = tk.Frame(self.root, bg="white", width=400,height=250)
        frame.place(x=75, y=40)

        #  Title for Otp Form
        ctk.CTkLabel(frame, text="OTP Verification", font=("Bookman Old Style", 25)).place(x=100, y=30)

        # Entry Widget for OTP
        self.otp_var = tk.StringVar()
        otp_entry = ctk.CTkEntry(frame, border_color="black",width=260,textvariable=self.otp_var, height=40, border_width=1, font=("Bookman Old Style", 20), corner_radius=5)
        otp_entry.place(x=60, y=90)
        otp_entry.focus()

        #  Submit Button
        self.error = ctk.CTkLabel(frame, text="", font=("Bookman Old Style", 18),fg_color="white", width=400, height=20)
        self.error.place(x=0, y=135)

        submit_btn = ctk.CTkButton(frame, text="Submit",hover_color="green",command=self.submit, font=("Bookman Old Style", 15),height=40,cursor="hand2", width=180, corner_radius=3, fg_color="orange",text_color="white")
        submit_btn.place(x=100, y=170)

        # Label To display Currently sent Otp
        self.response = ctk.CTkLabel(self.root, text="", width=100, font=("Bookman Old Style", 25))
        self.response.place(x=170, y=300)

        # Resent Button
        resend_btn = ctk.CTkButton(self.root, text="RESEND OTP",command=self.resend, hover_color="green",cursor="hand2", font=("Bookman Old Style", 25),height=50, width=250, corner_radius=3, fg_color="orange",text_color="white")
        resend_btn.place(x=140, y=350)

        # self.mes = messagebox.showinfo(title="OTP Number", message=f"Your OTP Code is: {str(self.random_otp)}")


    #  =====================================Function Definition============================================
    def submit(self):
        # if self.otp_var.get() == "":
            # self.error.configure(text="No text Found!!", text_color="red")

        # elif  len(self.otp_var.get()) > 4:
            # messagebox.showerror(title="OTP Status", message="Invalid OTP", parent=self.root)
        try:
            if int(self.otp_var.get()) == self.random_otp:
                ans = messagebox.askyesno(title="OTP Status", message="Are You Sure you Want to change Password?", parent = self.root)
                # Allow the user to register if the otp is correct
                if ans ==True:
                    #  Creates a new window for creating Next window
                    self.change = tk.Toplevel(self.root)
                    Password_change(self.change)
                else:
                    pass
                self.random_otp ="done"
            
            elif self.random_otp == "done":
                messagebox.showerror(title="OTP Status", message="OTP Already Used!!", parent=self.root)
            elif self.otp_var.get() == "":
                pass
                # self.error.configure(text="No text Found!!", text_color="red")

            elif  len(self.otp_var.get()) > 4:
                messagebox.showerror(title="OTP Status", message="OTP Cannot Exceed 4 Character", parent=self.root)
            else:
                messagebox.showerror(title="OTP Status", message="Wrong OTP", parent=self.root)
        except:
                self.error.configure(text="No text Found!!", text_color="red")



    



    def resend(self):
        self.random_otp = rad.randint(1000, 9999) 
        print(self.random_otp)

        time.sleep(2)
        self.response.configure(text=f"New OTP: {self.random_otp}", bg_color="gray", width=200)
        # self.mes = messagebox.showinfo(title="OTP Number", message=f"Your OTP Code is: {str(self.random_otp)}", parent=self.root)

        # time.sleep(10)
        # self.response.configure(text="----")
    
    def time(self):
            self.mes.after(100, time)
            
            # time.sleep(3)
            
            self.time()





if __name__ == "__main__":
    root = tk.Tk()
    Otp_form(root)
    root.mainloop()

