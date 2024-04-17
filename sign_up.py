import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from time import strftime
from tkinter import messagebox
import mysql.connector as mysql
import re
from tenant_main import Tenant_management_main
from random import choices
import string
import cv2




class Sign_up():
    def __init__(self,root1):
        self.root1 = root1
        self.root1.title("Login Management System")
        self.root1.geometry('820x560+230+50')

        # =====================variables =================
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_con_var = tk.StringVar()



        frame = tk.Frame(self.root1)
        frame.place(x=0, y=0, width=800, height=600)
        # self.root1.overrideredirect(1)
        bg_image = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/background.jpg")
        bg_image = bg_image.resize((790,532))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        bg = tk.Label(frame, image=self.bg_photo)
        bg.place(x=10, y=10, width=790,height=532)

        self.main_frame = ctk.CTkFrame(bg, width=300, fg_color="white", height=490)
        self.main_frame.place(x=448, y=40)

        ctk.CTkLabel(bg, text='REGISTRATION MANAGEMENT SYSTEM', width=740, bg_color='red', font=('Bookman Old Style',20)).place(x=0, y=2)

        # Time functionality

        def time():
            string = strftime("%H:%M:%S %p")
            self.clock.configure(text=string)
            self.clock.after(1000, time)
        self.clock = ctk.CTkLabel(bg, width=30,text_color='black', text='', bg_color='green', font=('Bookman Old Style',20))
        self.clock.place(x=673, y=2)
        time()

        # Username details
        ctk.CTkLabel(self.main_frame, text='Username', fg_color="white", font=('Bookman Old Style', 20)).place(x=90, y=5)

        username = ctk.CTkEntry(self.main_frame, width=260, corner_radius=0, border_width=0, height=35, textvariable=self.username_var, font=("Bookman Old style", 20))
        username.place(x=18, y=40)
        username.focus()

        username_idicator = tk.Label(self.main_frame,  bg="red")
        username_idicator.place(x=20, y=73,width=260, height=3)

        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/username2.png")
        icon = icon.resize((30, 30))
        self.user_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.main_frame, image=self.user_icon, bg='white').place(x=50, y=5)

        # Email details

        ctk.CTkLabel(self.main_frame, text='Email', fg_color="white", font=('Bookman Old Style', 20)).place(x=90, y=77)

        email = ctk.CTkEntry(self.main_frame, width=260, corner_radius=0, border_width=0, height=35, textvariable=self.email_var, font=("Bookman Old style", 20))
        email.place(x=20, y=115)
        # self.email_var.set(value="Example@gmail.com")

        
        email_idicator = tk.Label(self.main_frame,  bg="red")
        email_idicator.place(x=20, y=147,width=260, height=3)

        
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/email.jpg")
        icon = icon.resize((25, 25))
        self.pass_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.main_frame, image=self.pass_icon, bg='white').place(x=50, y=77)

        
        # Password details

        ctk.CTkLabel(self.main_frame, text='Password', fg_color="white", font=('Bookman Old Style', 20)).place(x=90, y=160)

        self.password = ctk.CTkEntry(self.main_frame, width=225, corner_radius=0, border_width=0, height=35, textvariable=self.password_var, show="*", font=("Bookman Old style", 20))
        self.password.place(x=20, y=195)

        # Icon to hide password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/openeye.png")
        icon = icon.resize((30, 30))
        self.open_eye = ImageTk.PhotoImage(icon)

        self.open_eye_btn = tk.Button(self.main_frame, bg='white', command=self.show_pass, image=self.open_eye, cursor="hand2", activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=247, y=195)

        # Icon to show  password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/closeye.png")
        icon = icon.resize((30, 30))
        self.close_eye = ImageTk.PhotoImage(icon)

        # self.close_eye_btn = tk.Button(bg, image=self.close_eye,command=self.hide_pass,cursor="hand2", bg='white', activebackground="white", borderwidth=0)
        # self.close_eye_btn.place(x=694, y=235)
        
        password_idicator = tk.Label(self.main_frame,  bg="red")
        password_idicator.place(x=20, y=227,width=260, height=3)

        
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/password1.png")
        icon = icon.resize((30, 30))
        self.email_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.main_frame, image=self.email_icon, bg='white').place(x=50, y=160)

        # Confirm  Password details

        ctk.CTkLabel(self.main_frame, text='Confirm Password', fg_color="white", font=('Bookman Old Style', 20)).place(x=90, y=240)

        self.password_confirm = ctk.CTkEntry(self.main_frame, width=225, corner_radius=0, border_width=0, height=35,show="*", textvariable=self.password_con_var, font=("Bookman Old style", 20))
        self.password_confirm.place(x=20, y=280)

        # Icon to show password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/openeye.png")
        icon = icon.resize((30, 30))
        self.open_eye_pass = ImageTk.PhotoImage(icon)

        self.open_eye_btn = tk.Button(self.main_frame, bg='white',image=self.open_eye_pass, command=self.show_pass_con,cursor="hand2", activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=247, y=280)

        # Icon to hide  password
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/closeye.png")
        icon = icon.resize((30, 30))
        self.close_eye_pass = ImageTk.PhotoImage(icon)
     
        password_idicator = tk.Label(self.main_frame,  bg="red")
        password_idicator.place(x=20, y=315,width=260, height=3)

        
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/password1.png")
        icon = icon.resize((30, 30))
        self.pass_con_icon = ImageTk.PhotoImage(icon)

        tk.Label(self.main_frame, image=self.pass_con_icon, bg='white').place(x=50, y=240)

        # Sign up button
        sign_up = ctk.CTkButton(self.main_frame, text="Sign Up", font=('Bookman Old Style', 20),hover_color="light green", text_color="black", width=275,fg_color="green", height=35, bg_color='white', cursor='hand2', command=self.sign_up)
        sign_up.place(x=15, y=400)

        # FaceBook  button
        #facebook_btn = ctk.CTkButton(bg, text="Sign Up", font=('Bookman Old Style', 20), width=120, height=50, bg_color='white', cursor='hand2') facebook_btn.place(x=460, y=370)

        # Facebok Icon 
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/facebook.png")
        icon = icon.resize((40, 40))
        self.facebook_icon = ImageTk.PhotoImage(icon)
        facebook_btn = tk.Button(self.main_frame,command=self.facebook, image=self.facebook_icon, bg="white", borderwidth=0,activebackground='white', cursor="hand2")
        facebook_btn.place(x=20, y=330)

        # Google Icon
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/google1.png")
        icon = icon.resize((40, 40))
        self.google_icon = ImageTk.PhotoImage(icon)
        google_btn = tk.Button(self.main_frame,command=self.google, image=self.google_icon, bg="white", borderwidth=0,activebackground='white', cursor="hand2")
        google_btn.place(x=90, y=330)

        # Instragram icon
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/instagram.png")
        icon = icon.resize((40, 40))
        self.instagram_icon = ImageTk.PhotoImage(icon)
        instagram_btn = tk.Button(self.main_frame,command=self.instagram, image=self.instagram_icon, bg="white", borderwidth=0,activebackground='white', cursor="hand2")
        instagram_btn.place(x=160, y=330)

        # Tiktok icon
        icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/tiktok.png")
        icon = icon.resize((40, 40))
        self.tiktok_icon = ImageTk.PhotoImage(icon)
        tiktok_btn = tk.Button(self.main_frame,command=self.tiktok, image=self.tiktok_icon, bg="white", borderwidth=0,activebackground='white', cursor="hand2")
        tiktok_btn.place(x=230, y=330)

        # # Remember me checkbox
        # remind_btn = ctk.CTkCheckBox(bg, text="Remember Me", font=('Bookman Old Style', 20),fg_color='blue', bg_color='white')
        # remind_btn.place(x=500, y=340)

        # # Forget password button
        # forget_btn = ctk.CTkButton(bg, text="Forget Password", font=('Bookman Old Style', 20), width=250, height=25, bg_color='white', cursor='hand2')
        # forget_btn.place(x=480, y=380)

        # # Create Account button
        # create_btn = ctk.CTkButton(bg, text="Create Account", font=('Bookman Old Style', 20), width=120, height=30, bg_color='white', cursor='hand2')
        # create_btn.place(x=540, y=420)
        
        # Train Data Buton
        train_btn = ctk.CTkButton(self.main_frame, text="Capture Face",command=self.train, corner_radius=0,hover_color="green", fg_color="black",bg_color="pink", font=("Bookman Old Style", 25), width=290)
        train_btn.place(x=5, y=450)


    def show_pass(self):
        self.close_eye_btn = tk.Button(self.main_frame, image=self.close_eye,command=self.hide_pass,cursor="hand2",  borderwidth=0, bg='white', activebackground="white",)
        self.close_eye_btn.place(x=247, y=195)
        self.password.configure(show="")
        
    def hide_pass(self):
        
        self.open_eye_btn = tk.Button(self.main_frame, image=self.open_eye,command=self.show_pass,cursor="hand2", bg='white', activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=247, y=195)
        self.password.configure(show="*")

    def show_pass_con(self):
        self.close_eye_btn = tk.Button(self.main_frame, image=self.close_eye,command=self.hide_pass_con,cursor="hand2",  borderwidth=0, bg='white', activebackground="white",)
        self.close_eye_btn.place(x=247, y=280)
        self.password_confirm.configure(show="")

    def hide_pass_con(self):
        self.open_eye_btn = tk.Button(self.main_frame, image=self.open_eye,command=self.show_pass_con,cursor="hand2", bg='white', activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=247, y=280)
        self.password_confirm.configure(show="*")

        

    
    def validate_email(self,email):
        # Define a regular expression pattern for a valid email address
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
    def sign_up(self):
        if self.username_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a username!', parent=self.root1)
        elif self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter an email!', parent=self.root1)
        elif self.password_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a password!', parent=self.root1)
        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        elif self.password_con_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please confirm the password!', parent=self.root1)
        elif self.password_var.get() != self.password_con_var.get():
            messagebox.showerror(title='Signup Status', message='Passwords do not match!', parent=self.root1)
        else:
            try:
                # Connect to MySQL Database
                def generate_tenant_code(length):
                    code = string.digits
                    tenant_code = "".join(choices(code, k=length))
                    return tenant_code
                length_code = 2
                random_no = generate_tenant_code(length_code)
                tenant_id = f"GRT0{random_no}"
                
                conn = mysql.connect(host="localhost", user="root", password="flivian254", database="mydb")
                cur = conn.cursor()

                # Check if the user already exists
                cur.execute("SELECT * FROM registration WHERE email=%s", (self.email_var.get(),))
                if cur.fetchone():
                    messagebox.showerror(title='Signup Status', message='Email already exists!', parent=self.root1)
                else:
                    # Insert a new record
                    cur.execute("INSERT INTO registration VALUES(%s, %s, %s, %s)", (
                        tenant_id,
                        self.username_var.get(),
                        self.email_var.get(),
                        self.password_var.get()
                    ))
                    conn.commit()
                    conn.close()
                    mess = messagebox.askyesno(title='Signup Status', message="Are you sure you want to Sign Up without Capturing  Face", parent=self.root1)
                    if mess == True:
                        self.app = tk.Toplevel(self.root1)
                        self.new_app = Tenant_management_main(self.app)
                                          
                        self.username_var.set("")
                        self.email_var.set("")
                        self.password_var.set("")
                        self.password_con_var.set("")
                    else:
                        pass

                    # self.new_window = tk.Toplevel(self.root1)
                    # self.app = Tenant_management_main(self.new_window)
            except Exception as es:
                messagebox.showerror(title="Error", message=f"Error due to {str(es)}", parent=self.root1)

    def train(self):
        if self.username_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a username!', parent=self.root1)
        elif self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter an email!', parent=self.root1)
        elif self.password_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a password!', parent=self.root1)
        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        elif self.password_con_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please confirm the password!', parent=self.root1)
        elif self.password_var.get() != self.password_con_var.get():
            messagebox.showerror(title='Signup Status', message='Passwords do not match!', parent=self.root1)
        else:
            try:
                # Connect to MySQL Database
                conn = mysql.connect(host="localhost", user="root", password="flivian254", database="mydb")
                cur = conn.cursor()

                # Check if the user already exists
                cur.execute("SELECT * FROM registration WHERE email=%s", (self.email_var.get(),))
                if cur.fetchone():
                    messagebox.showerror(title='Signup Status', message='Email already exists!', parent=self.root1)
                    self.email_var.set("")
                else:                
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (200, 200))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_path = f"data/tenant.{id}.{img_id}.jpg"
                            cv2.imwrite(file_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Capture Images", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Signup Status", "Generating dataset completed!")
                    messagebox.showinfo(title="Signup Status", message="DataSet captured Successfully", parent=self.root1)        
                    self.username_var.set("")
                    self.email_var.set("")
                    self.password_var.set("")
                    self.password_con_var.set("")
            except:
                pass

    def facebook(self):
        if self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a valid email Adress!\nTo sign up With Facebook', parent=self.root1)

        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        else:
            messagebox.showinfo(title="SignUp Status", message="Ooops!!! Facebook Underconstruction....", parent=self.root1)
    
    def google(self):
        if self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a valid email Adress!\nTo sign up With Google', parent=self.root1)

        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        else:
            messagebox.showinfo(title="SignUp Status", message="Ooops!!! Google Underconstruction....", parent=self.root1)
    
    def instagram(self):
        if self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a valid email Adress!\nTo sign up With Instagram', parent=self.root1)

        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        else:
            messagebox.showinfo(title="SignUp Status", message="Ooops!!! Instagram Underconstruction....", parent=self.root1)

    def tiktok(self):
        if self.email_var.get() == '':
            messagebox.showerror(title='Signup Status', message='Please enter a valid email Adress!To sign up With Tiktok', parent=self.root1)

        elif not self.validate_email(self.email_var.get()):
            messagebox.showerror(title='Signup Status', message='Please enter a valid email address!', parent=self.root1)
        else:
            messagebox.showinfo(title="SignUp Status", message="Ooops!!! Tiktok Underconstruction....", parent=self.root1)
            



if __name__ == '__main__':
    root1 = tk.Tk()
    obj = Sign_up(root1)
    root1.mainloop()