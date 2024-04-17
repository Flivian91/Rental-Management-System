from tkinter import messagebox
import tkinter as tk
import customtkinter as ctk
import mysql.connector as mysql
# from login import Login


#  Window for changing Password
class Password_change():
    def __init__(self, root):
        self.root = root
        self.root.geometry("470x340+300+120")
        self.root.title("Change Password Panel")
        #  Main Title of the Window

        ctk.CTkLabel(self.root, text="RESET PASSWORD PANEL", font=("Bookman Old Style", 27), width=480, height=35, fg_color="red").place(x=0, y=5)
        
        ctk.CTkLabel(self.root, text="Enter New Password", font=("Bookman Old Style", 18),  height=35).place(x=150, y=50)

        # New password Entry Field
        self.password_var = tk.StringVar()
        new_password = ctk.CTkEntry(self.root, border_color="pink",width=360,textvariable=self.password_var, height=40, border_width=1, font=("Bookman Old Style", 20), corner_radius=2)
        new_password.place(x=50, y=90)
        new_password.focus()

        ctk.CTkLabel(self.root, text="Confirm New Password", font=("Bookman Old Style", 18),  height=35).place(x=150, y=150)

        # Confirmation Password Entry Field
        self.password_var_con = tk.StringVar()
        new_password_con = ctk.CTkEntry(self.root, border_color="pink",width=360,textvariable=self.password_var_con, height=40, border_width=1, font=("Bookman Old Style", 20), corner_radius=2)
        new_password_con.place(x=50, y=190)

        # Back button
        back_btn = ctk.CTkButton(self.root,command=self.back, text="Back",fg_color="black",width=150,height=40, corner_radius=1, cursor='hand2', border_width=0)
        back_btn.place(x=30, y=280)

        # Submit Button
        submit_btn = ctk.CTkButton(self.root, command=self.submit, text="Submit",font=("Bookman Old Style", 20), fg_color="green",width=150,height=40, corner_radius=1, cursor='hand2', border_width=0)
        submit_btn.place(x=290, y=280)


    def back(self):
        self.root.destroy()
        # Login()
    
    def submit(self):
        if self.password_var.get() == "":
            messagebox.showerror(title="Change Password Status",message="Please New Password Must be filled!!", parent=self.root)
        elif self.password_var.get() != self.password_var_con.get():
            messagebox.showerror(title="Change Password Status", message="Please New Password and Confirm password Does Not Match", parent=self.root)
        elif self.password_var_con.get() == "":
            messagebox.showerror(title="Change Password Status",message="Please Confirm New Password Must be filled!!", parent=self.root)
        else:
            messagebox.showinfo(title="Login Status", message="Password Updated Succesfully", parent=self.root)
            self.root.destroy()
            # try:
            #     conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
            #     print(conn)
            #     cur = conn.cursor()
            #     cur.execute("UPDATE registration SET password=%s WHERE tenant_id=%s", (self.password_var.get(), tenant_id))
            #     conn.commit()
            #     conn.close()
            #     messagebox.showinfo(title="Database Status", message="Record Updated Successfully!")
                
            # except Exception as es:
            #     messagebox.showerror(title="Database Status", message=f"Error Due to: {str(es)}", parent=self.root)







if __name__ == "__main__":
    root = tk.Tk()
    Password_change(root)
    root.mainloop()