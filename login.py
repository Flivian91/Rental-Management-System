import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from time import strftime
from tkinter import messagebox
from tenant_main import Tenant_management_main
from sign_up import Sign_up
import sys
import time as time
import re
import mysql.connector as mysql
from otp_form import Otp_form
import cv2


# import subprocess




class Login():
    def __init__(self,root1):
        self.root1 = root1
        self.root1.title("Login Management System")
        self.root1.geometry('820x530+230+50')
        self.root1.resizable(False, False)
        # self.root1.overrideredirect(True)

        # =====================variables =================
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()



        frame = tk.Frame(self.root1)
        frame.place(x=0, y=0, width=800, height=600)
        # self.root1.overrideredirect(1)
        self.frame_image = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/background.jpg")
        self.frame_image = self.frame_image.resize((790,512))
        self.frame_photo = ImageTk.PhotoImage(self.frame_image)
        
        self.bg= tk.Label(frame, image=self.frame_photo)
        self.bg.place(x=10, y=10, width=790,height=512)

        self.frame = ctk.CTkFrame(self.bg, fg_color="white", width=300,bg_color="white", height=450, corner_radius=10)
        self.frame.place(x=448, y=40)

        ctk.CTkLabel(self.bg, text='LOGIN MANAGEMENT SYSTEM', width=760, bg_color='red', font=('Bookman Old Style',20)).place(x=0, y=2)

        # Time functionality

        def time():
            string = strftime("%H:%M:%S %p")
            self.clock.configure(text=string)
            self.clock.after(1000, time)
        self.clock = ctk.CTkLabel(self.bg, width=30,text_color='black', text='', bg_color='green', font=('Bookman Old Style',20))
        self.clock.place(x=668, y=2)
        time()

        # Username details
        ctk.CTkLabel(self.frame, text='Username', fg_color="white", font=('Bookman Old Style', 20)).place(x=65, y=28)

        username = ctk.CTkEntry(self.frame, width=260,font=('Bookman Old Style', 20), corner_radius=0, border_width=0, height=35, textvariable=self.username_var)
        username.place(x=20, y=60)
        username.focus()

        username_idicator = tk.Label(self.frame,  bg="red")
        username_idicator.place(x=20, y=94,width=260, height=3)

        

        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/username2.png")
        icon = icon.resize((30, 30))
        self.user_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.frame, image=self.user_icon, bg='white').place(x=25, y=26)

        # Password details

        ctk.CTkLabel(self.frame, text='Password', fg_color="white", font=('Bookman Old Style', 20)).place(x=65, y=120)

        self.password = ctk.CTkEntry(self.frame, width=240, corner_radius=0, font=('Bookman Old Style', 20), border_width=0, height=35, textvariable=self.password_var, show="*")
        self.password.place(x=20, y=155)

        # Icon to show password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/openeye.png")
        icon = icon.resize((30, 30))
        self.open_eye = ImageTk.PhotoImage(icon)

        self.open_eye_btn = tk.Button(self.frame, bg='white',image=self.open_eye, command=self.show_pass,cursor="hand2", activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=260, y=155)

        # Icon to hide  password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/closeye.png")
        icon = icon.resize((30, 30))
        self.close_eye = ImageTk.PhotoImage(icon)

        # self.close_eye_btn = tk.Button(self.frame, image=self.close_eye,command=self.hide_pass,cursor="hand2", self.frame='white', activebackground="white", borderwidth=0)
        # self.close_eye_btn.place(x=694, y=200)

        
        password_idicator = tk.Label(self.frame,  bg="red")
        password_idicator.place(x=20, y=190,width=240, height=3)

        
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/password1.png")
        icon = icon.resize((30, 30))
        self.pass_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.frame, image=self.pass_icon, bg='white').place(x=30, y=115)

        # Login button
        login_btn = ctk.CTkButton(self.frame, text="Login",corner_radius=2,fg_color="green", font=('Bookman Old Style', 20), width=120, height=35, bg_color='white', cursor='hand2', command=self.login)
        login_btn.place(x=160, y=230)

        # Sign up button
        signup_btn = ctk.CTkButton(self.frame, text="Sign Up",command=self.sign_up,fg_color="green", corner_radius=2, font=('Bookman Old Style', 20), width=120, height=35, bg_color='white', cursor='hand2')
        signup_btn.place(x=20, y=230)

        # Facial Login Button
        face_btn = ctk.CTkButton(self.frame, text="Facial Login",command=self.face, corner_radius=2, font=('Bookman Old Style', 20), width=250, height=35, bg_color='white', cursor='hand2')
        face_btn.place(x=25, y=285)

        # Forget password button
        forget_btn = ctk.CTkButton(self.frame, text="Forget Password",command=self.forget_pass, corner_radius=1, font=('Bookman Old Style', 20), width=250, height=30, bg_color='white', cursor='hand2')
        forget_btn.place(x=25, y=340)

        # Exit button
        create_btn = ctk.CTkButton(self.frame, text="Exit",command=self.exit,corner_radius=2, font=('Bookman Old Style', 20), width=120, height=30, bg_color='white',fg_color="black", cursor='hand2')
        create_btn.place(x=80, y=400)



    def show_pass(self):
        self.close_eye_btn = tk.Button(self.frame, image=self.close_eye,command=self.hide_pass,cursor="hand2",  borderwidth=0, bg='white', activebackground="white",)
        self.close_eye_btn.place(x=260, y=155)
        self.password.configure(show="")
        

    def hide_pass(self):
        # ?self.show_pass()
        
        self.open_eye_btn = tk.Button(self.frame, image=self.open_eye,command=self.show_pass,cursor="hand2", bg='white', activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=260, y=155)
        self.password.configure(show="*")


    def validate_password(self,password):
        # Define a regular expression pattern for a Password
        pattern = r'[a-zA-Z0-9.?!@#$%&*,]+'
        return re.match(pattern, password) is not None

    def login(self):
        if self.username_var.get() == '':
            messagebox.showerror(title='Login Status', message='Please Username Field Must be Filled!!!', parent=self.root1)
        elif self.password_var.get() == '':
            messagebox.showerror(title='Login Status', message='Please Password Field Must be Filled!!!', parent=self.root1)
        elif not self.validate_password(self.password_var.get()):
            messagebox.showerror(title='Login Status', message='Invalid Password!!!', parent=self.root1)
            
        elif self.password_var.get() == 'admin' and self.password_var.get() == 'admin':
            messagebox.showinfo(title='Login status', message='Are you sure you are the admin', parent=self.root1)
            #self.root1.destroy()
            self.app = tk.Toplevel(self.root1)
            password = "admin"
            self.new =Tenant_management_main(self.app, password)
            self.username_var.set("")
            self.password_var.set("")
        else:
            try:
                conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
                cur = conn.cursor()
                cur.execute("SELECT * FROM registration WHERE username=%s and password=%s", (self.username_var.get(), self.password_var.get(),))
                row = cur.fetchone()
                # for res in range(3):
                if row == None:
                    res = messagebox.showerror(title="Login Status", message="Invalid username or password", parent= self.root1)
                    # self.root1.destroy()
                    self.password_var.set("")
                else:
                    ask = messagebox.askyesno(title="Login Status", message="Are you sure you want to login", parent=self.root1)
                    if ask > 0:
                        # username = self.username_var.get()
                        self.username_var.set("")
                        self.password_var.set("")
                        username = self.username_var.get()
                        self.app = tk.Toplevel(self.root1)
                        self.new =Tenant_management_main(self.app, username)
                    else:
                        if ask is None:
                            return 

            except Exception as es:
                messagebox.showerror(title='Login Status', message=f'Error Due to: {str(es)}', parent=self.root1)

    def sign_up(self):
        results = messagebox.askyesno(title="Login Status", message="Are you sure you want to sign up", parent=self.root1)
        if results:
        #    sys.exit()
            self.app = tk.Toplevel(self.root1)
            self.new = Sign_up(self.app)
           
           
    def exit(self):
        mess = messagebox.askyesno(title="Login Status", message="Are you sure you want to exit?")

        if mess > 0:

            self.root1.destroy()
        else:
            pass
    def forget_pass(self):
        forget_pass_window = tk.Toplevel(self.root1)
        Second_window(forget_pass_window)

    def face(self):
        face_window = tk.Toplevel(self.root1)
        Third_window(face_window)

class Second_window():
    def __init__(self, root1):
        self.root1 = root1
        self.root1.geometry("530x350+350+100")
        self.root1.title("Forget Password Panel")
        self.root1.resizable(False, False)
        self.root1.config(background="white")

        # Title label for Forget Password Panel
        ctk.CTkLabel(self.root1, text="FORGET PASSWORD PANEL", font=("Bookman Old Style", 20), width=550, height=35, fg_color="red").place(x=0, y=3)
        ctk.CTkLabel(self.root1, text="To Reset Password Provide the Email Used for Registration", font=("Bookman Old Style", 18), width=550, height=35, fg_color="light gray").place(x=0, y=45)

        ctk.CTkLabel(self.root1, text="Enter Valid Email Address ", font=("Bookman Old Style", 20), width=550, height=35).place(x=0, y=90)

        # Entry For Email
        self.forget = tk.StringVar()
        forget_entry = ctk.CTkEntry(self.root1, border_width=1,textvariable=self.forget, border_color="pink",height=40, corner_radius=5,width=400, font=("Bookman Old Style", 20))
        forget_entry.place(x=60, y=140)
        
        # Label to display Respose When Email is Input
        self.response = ctk.CTkLabel(self.root1, text="", font=("Bookman Old Style", 20), width=550, height=35)
        self.response.place(x=0, y=180)

        # Back Button to Login
        back_btn = ctk.CTkButton(self.root1, text="Back",command=self.back, fg_color="black",height=50, font=("Bookman Old Style", 20), corner_radius=0)
        back_btn.place(x=10, y=250)

        # Login Button to Go Back to Login Page
        login_btn = ctk.CTkButton(self.root1, text="Login",command=self.login_forget, fg_color="black",height=50, font=("Bookman Old Style", 20), corner_radius=0)
        login_btn.place(x=200, y=250)

        # Send Request Button to display The OTP Form 
        send_btn = ctk.CTkButton(self.root1, text="Send",command=self.send, fg_color="black",height=50, font=("Bookman Old Style", 20), corner_radius=0)
        send_btn.place(x=380, y=250)

    # ==============================Fuction Definition For the Forget password =====================================================
    def back(self):
        ask = messagebox.askyesno(title="Forget Password Status", message="Are You sure you want To Leave?", parent=self.root1)
        # print(ask)
        if ask == True:
            self.root1.destroy()
        else:
            pass
    def login_forget(self):
        ask = messagebox.askyesno(title="Forget Password Status", message="Confirm You are Moving to Login Page?", parent=self.root1)

        if ask == True:
            Login(self.root1)
        else:
            pass
            # self.root1.destroy()
    def validate_email(self,email):
        # Define a regular expression pattern for a valid email address
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def send(self):
        if self.forget.get() == '':
            self.response.configure(text="Please Fill valid Email!!", fg_color="white", text_color="red")

        elif not self.validate_email(self.forget.get()):
            # messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
            self.response.configure(text="Invalid Email!! (example@gmial.com)", fg_color="white", text_color="red")

        else:
            try:
                conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
                cur = conn.cursor()
                cur.execute("SELECT * FROM registration WHERE email=%s", (self.forget.get(),))
                data = cur.fetchone()
                if data == None:
                    messagebox.showerror(title="Error", message="Email Doesn`t Exit!!", parent=self.root1)
                else:
                    mess = messagebox.askyesno(title="Forget Password Status", message="Are You sure you Want to reset Password", parent=self.root1)
                    if mess == True:
                        # SEND THE OTP MESSAGE TO THE GMAIL.
                        self.app = tk.Toplevel(self.root1)
                        self.new = Otp_form(self.app)
                    else:
                        pass
            except Exception as es:
                messagebox.showerror(title="Database Status", message=f"Error Due to: {str(es)}", parent=self.root1)


class Third_window():
    def __init__(self, root1):
        self.root1 = root1

        # Opencv variables
        self.videp_capture = cv2.VideoCapture(0)
        self.current_image = None
        # self.videp_capture.release()

        # create a webcam display  
        self.canvas = tk.Canvas(self.root1, width=640, height=480)
        self.canvas.pack()

        # Start Webcam
        # self.update_webcam()

    

        










if __name__ == '__main__':
    root1 = tk.Tk()
    obj = Login(root1)
    root1.mainloop()