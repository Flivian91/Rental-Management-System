import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from time import strftime
from tkinter import messagebox
from sign_up import Sign_up
import sys
import time as time
import re
import mysql.connector as mysql
from otp_form import Otp_form
import cv2
from datetime import date
from tkinter import PhotoImage
import os
from random import choices
import string


# Class Login Main WIndow to display
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

        # Main Frame
        frame = tk.Frame(self.root1)
        frame.place(x=0, y=0, width=800, height=600)

        # Backgrond Image inside main frame
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

        # indicator of the username
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

        # password Indicator
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
        
    # =======================================Function Definition====================================================================
    # show password function
    def show_pass(self):
        self.close_eye_btn = tk.Button(self.frame, image=self.close_eye,command=self.hide_pass,cursor="hand2",  borderwidth=0, bg='white', activebackground="white",)
        self.close_eye_btn.place(x=260, y=155)
        self.password.configure(show="")
        
    # hide password function
    def hide_pass(self):
        # ?self.show_pass()
        self.open_eye_btn = tk.Button(self.frame, image=self.open_eye,command=self.show_pass,cursor="hand2", bg='white', activebackground="white", borderwidth=0)
        self.open_eye_btn.place(x=260, y=155)
        self.password.configure(show="*")

    # validate password function
    def validate_password(self,password):
        # Define a regular expression pattern for a Password
        pattern = r'[a-zA-Z0-9.?!@#$%&*,]+'
        return re.match(pattern, password) is not None

    # login function
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
                # mysql connection
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
                    ask = messagebox.showinfo(title="Login Status", message="Login Successfully!!!", parent=self.root1)
                    
                    if ask == "ok":
                        username = self.username_var.get()
                        self.username_var.set("")
                        self.password_var.set("")
                        Tenant_management_main(tk.Toplevel(self.root1), username)
                    else:
                        if ask is None:
                            return 

            except Exception as es:
                messagebox.showerror(title='Login Status', message=f'Error Due to: {str(es)}', parent=self.root1)

    # Sign up option function
    def sign_up(self):
        results = messagebox.askyesno(title="Login Status", message="Are you sure you want to sign up", parent=self.root1)
        if results:
        #    sys.exit()
            self.app = tk.Toplevel(self.root1)
            self.new = Sign_up(self.app)
           
    # exit function  
    def exit(self):
        mess = messagebox.askyesno(title="Login Status", message="Are you sure you want to exit?")
        if mess > 0:
            self.root1.destroy()
        else:
            pass
    # Forget password Defination function
    def forget_pass(self):
        forget_pass_window = tk.Toplevel(self.root1)
        Second_window(forget_pass_window)

    # face recoginization function
    def face(self):
        face_window = tk.Toplevel(self.root1)
        Third_window(face_window)



# ?=========================================Tenant management system Home page=================== #
class Tenant_management_main():
   def __init__(self, root, username):
      self.root = root
      self.username = username
      self.root.geometry("1230x650+20+5")
      self.root.title ("Tenant Management System")
      # =================================Variables=================================


      # ======================Header Frame ==========================================
      self.header_frame = ctk.CTkFrame(self.root, fg_color="light green", width=1200, height=100)
      self.header_frame.place(x=4,y=1)

      # ====================Current Time Display===============================
      def time():
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, time)
      self.clock=ctk.CTkLabel(self.header_frame, corner_radius=0, width=200, text_color="red", font=("Bookman Old style", 30)) 
      self.clock.place(x=1000, y=12)
      time()
      
      # Rentals name or title
      self.name=ctk.CTkLabel(self.header_frame, corner_radius=0,text="KIRINYAGA UNIVERSITY RENTALS", text_color="red", font=("Bookman Old style,bold",25)) 
      self.name.place(x=400, y=16)
   
      # main frame for all buttons
      main_frame = tk.Frame(self.root, bg="#c3c3c3")
      main_frame.pack(side=tk.LEFT, padx=3)
      main_frame.pack_propagate(False)
      main_frame.configure(width=200, height=530)

      # tenant name icon
      img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\icons\username2.png")
      img = img.resize((50, 50))
      self.photoimg = ImageTk.PhotoImage(img)

      f_lbl = tk.Label(self.header_frame, image=self.photoimg, cursor="hand2", background="light green")
      f_lbl.place(x=5, y=5, width=50, height=50)

      # Tenant name label
      tenant_name_lb = tk.Label(self.header_frame, text=f"  {self.username}", font=("Bookman Old Style", 20), background="light green")
      tenant_name_lb.place(x=50, y=10)

      # ===================================buttons on main frame================================================ 

      # Rental View Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Rental View", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_rental, self.rental_view_fun))
      self.rental_view_btn.place(x=0, y=15)
      
      
      # rental View indicator with red background

      self.lb_indicator_rental = tk.Label(main_frame, text="Tenant Name", bg="#0beba1")
      self.lb_indicator_rental.place(x=0, y=15, width=5, height=60)

      # Payment  Button 

      self.payment_btn = ctk.CTkButton(main_frame, text="Payment", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_payment,self.payment_view_fun))
      self.payment_btn.place(x=0, y=96)

      # payment Indicator 
      self.lb_indicator_payment = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_payment.place(x=0, y=96, width=5, height=60)

      # Notifiaction Button 

      self.notification_btn = ctk.CTkButton(main_frame, text="Transaction", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_notification, self.notification_view_fun))
      self.notification_btn.place(x=0, y=180)

      # label to show current messages sent
      message_lb = ctk.CTkLabel(self.notification_btn, text="1",text_color="red",fg_color="white", width=30, font=("Bookman Old Style", 20), corner_radius=15, bg_color="#0beba1")
      message_lb.place(x=160, y=3)
      
      # Notification indicator
      self.lb_indicator_notification = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_notification.place(x=0, y=180, width=5, height=60)

      # Profile Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Profile", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_profile, self.profile_view_fun))
      self.rental_view_btn.place(x=0, y=260)

      # Profile indicator

      self.lb_indicator_profile = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_profile.place(x=0, y=260, width=5, height=60)

      # Contact Us Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Contact Us", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_contact, self.contact_view_fun))
      self.rental_view_btn.place(x=0, y=360)
      
      # contact Us indicator
      self.lb_indicator_contact = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_contact.place(x=0, y=360, width=5, height=60)

      # Logout  Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Loguot", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_logout, self.logout_view_fun))
      self.rental_view_btn.place(x=0, y=460)

      # logout Indicator
      self.lb_indicator_logout = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_logout.place(x=0, y=460, width=5, height=60)


      # =====================================main Window Frame======================================== 
      self.page_frame = tk.Frame(self.root, highlightthickness=0)
      self.page_frame.pack(side=tk.LEFT)
      self.page_frame.pack_propagate(False)
      self.page_frame.configure(width=1000, height=530)

      # ===================background Image for Rental Houses===========================
      image_left = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\rental4.jpg")
      image_left = image_left.resize((990, 530))
      self.bg_photo = ImageTk.PhotoImage(image_left)

      image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=530)
      
      # footer message
      self.footer_frame = ctk.CTkFrame(self.root, fg_color="light green", width=1200, height=50)
      self.footer_frame.place(x=4,y=595)

      ctk.CTkLabel(self.footer_frame, text="TAGLINE: The Way we see it, real wealth means having the money and the freedom to live life on your own terms", font=("BookMan Old Style", 20)).place(x=10, y=7)

      # ======================================function for indicators==========================================

   def indicator(self, lbl, page):
      self.hide_indicator()
      self.delete_page()
      lbl.config(bg="red")
      page()
      
   # Hide function to hide one button after the other is clicked
   def hide_indicator(self):
      self.lb_indicator_rental.config(bg="#0beba1")
      self.lb_indicator_payment.config(bg="#0beba1")
      self.lb_indicator_notification.config(bg="#0beba1")
      self.lb_indicator_profile.config(bg="#0beba1")
      self.lb_indicator_contact.config(bg="#0beba1")
      self.lb_indicator_logout.config(bg="#0beba1")


   # Rental view page
   def rental_view_fun(self):
      # rental frame contain all the other widget
      rental_main_frame = tk.Frame(self.page_frame, width=1000, height=800)
      rental_main_frame.place(x=10, y=10)

      # search labelframe with location, type, price

      search_frame = tk.LabelFrame(rental_main_frame, text="Search By",bg="light green", font=("Bookman Old Style", 20))
      search_frame.place(x=10, y=5, width=970, height=100)


      # location combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["a1", "a2", "a3"], state="readonly", width=200, fg_color="light yellow", dropdown_fg_color="#0beba1",font=("Bookman Old Style", 20), dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=4, y=5)
      location_cmb.set(value="Location")

      # Type of house combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["Single Room", "Bedsitter", "1 Bedroom", "2 Bedroom", "3 Bedroom"], state="readonly", width=250, fg_color="light yellow",font=("Bookman Old Style", 20), dropdown_fg_color="#0beba1", dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=250, y=5)
      location_cmb.set(value="Type")

      # Price of house combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["2000", "3000", "4000", "5000"], state="readonly", width=200, fg_color="light yellow", dropdown_fg_color="#0beba1",font=("Bookman Old Style", 20), dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=550, y=5)
      location_cmb.set(value="Price")

      # explore all button 
      explore_btn = ctk.CTkButton(search_frame, text="Explore All", width=150, fg_color="blue", height=50, font=("Bookman Old Style", 20))
      explore_btn.place(x=800, y=0)

      # text on screan label
      ctk.CTkLabel(rental_main_frame, text="Our Popular Rentals", font=("Bookman Old Style", 30)).place(x=40, y =105)

      # Create a Canvas widget inside a Frame
      frame = tk.Frame(rental_main_frame)
      self.canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0, width=1000, height=400)
      scrollbar_y = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
      scrollbar_x = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)

      scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
      scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
      self.canvas.place(x=2, y=2, width=1000, height=400)

      # Configure the canvas to work with the scrollbars
      self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
      self.canvas.bind("<Configure>", self.on_configure)

      frame.place(x=2, y=140, width=990, height=500)


      # frame to Hold all the Available houses 
      rental_frame = tk.LabelFrame(self.canvas, text="Availbale Rentals", width=1000, height=1000, bg="#0beba1")
      rental_frame.place(x=0, y=3, width=1000, height=1000)
      self.canvas.create_window((0, 0), window=rental_frame, anchor="nw")



      # ================================1st Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=0)
      # ===============BOOK 1 VARIABLES =============
      self.type_mode_var1 = tk.StringVar()
      self.type_mode_var1.set(value="Bedsitter")
      self.location_mode_var1 = tk.StringVar()
      self.location_mode_var1.set(value="a1")
      self.price_mode_var1 = tk.StringVar()
      self.price_mode_var1.set(value="4000")


      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, textvariable=self.type_mode_var1, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, textvariable=self.location_mode_var1, text="a2", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, textvariable=self.price_mode_var1, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn,command=self.book1, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================2nd Available House==================================

       # ===============BOOK 2 VARIABLES =============
      self.type_mode_var2 = tk.StringVar()
      self.type_mode_var2.set(value="Single")
      self.location_mode_var2 = tk.StringVar()
      self.location_mode_var2.set(value="12")
      self.price_mode_var2 = tk.StringVar()
      self.price_mode_var2.set(value="3000")


      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=0)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn,textvariable=self.type_mode_var2, text="Single", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a2",textvariable=self.location_mode_var2, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 3000",textvariable=self.price_mode_var2, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, command=self.book2, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================3rd Available house ==================================
            # ===============BOOK 3 VARIABLES =============
      self.type_mode_var3 = tk.StringVar()
      self.type_mode_var3.set(value="Bedsitter")
      self.location_mode_var3 = tk.StringVar()
      self.location_mode_var3.set(value="a3")
      self.price_mode_var3 = tk.StringVar()
      self.price_mode_var3.set(value="4000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=0)

      type_lb = ctk.CTkLabel(self.house_btn,textvariable=self.type_mode_var3, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var3, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var3, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn,command=self.book3, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================4th Available House  ==================================

            # ===============BOOK 4 VARIABLES =============
      self.type_mode_var4 = tk.StringVar()
      self.type_mode_var4.set(value="1 Bedroom")
      self.location_mode_var4 = tk.StringVar()
      self.location_mode_var4.set(value="a3")
      self.price_mode_var4 = tk.StringVar()
      self.price_mode_var4.set(value="5000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="1 Bedroom",textvariable=self.type_mode_var4, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var4, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 5000",textvariable=self.price_mode_var4, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn,command=self.book4, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================5th Available House==================================

            # ===============BOOK 5 VARIABLES =============
      self.type_mode_var5 = tk.StringVar()
      self.type_mode_var5.set(value="Bedsitter")
      self.location_mode_var5 = tk.StringVar()
      self.location_mode_var5.set(value="a3")
      self.price_mode_var5 = tk.StringVar()
      self.price_mode_var5.set(value="4000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter",textvariable=self.type_mode_var5, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var5, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var5, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book5, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================6th Available House ==================================

            # ===============BOOK 6 VARIABLES =============
      self.type_mode_var6 = tk.StringVar()
      self.type_mode_var6.set(value="2 Bedroom")
      self.location_mode_var6 = tk.StringVar()
      self.location_mode_var6.set(value="a1")
      self.price_mode_var6 = tk.StringVar()
      self.price_mode_var6.set(value="6000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn,textvariable=self.type_mode_var6, text="2 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a1",textvariable=self.location_mode_var6, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000",textvariable=self.price_mode_var6, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book6, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)


      # ================================7th Available House==================================

            # ===============BOOK 7 VARIABLES =============
      self.type_mode_var7 = tk.StringVar()
      self.type_mode_var7.set(value="3 Bedroom")
      self.location_mode_var7 = tk.StringVar()
      self.location_mode_var7.set(value="a2")
      self.price_mode_var7 = tk.StringVar()
      self.price_mode_var7.set(value="7000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="3 Bedroom",textvariable=self.type_mode_var7, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var7, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 7000",textvariable=self.price_mode_var7, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn,command=self.book7, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================8th Available House ==================================

      # ===============BOOK 8 VARIABLES =============
      self.type_mode_var8 = tk.StringVar()
      self.type_mode_var8.set(value="Bedsitter")
      self.location_mode_var8 = tk.StringVar()
      self.location_mode_var8.set(value="c1")
      self.price_mode_var8 = tk.StringVar()
      self.price_mode_var8.set(value="4000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter",textvariable=self.type_mode_var8, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="c4",textvariable=self.location_mode_var8, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK B RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var8, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book8, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================9th Available House ==================================

      # ===============BOOK 9 VARIABLES =============
      self.type_mode_var9 = tk.StringVar()
      self.type_mode_var9.set(value="2 Bedroom")
      self.location_mode_var9 = tk.StringVar()
      self.location_mode_var9.set(value="b1")
      self.price_mode_var9 = tk.StringVar()
      self.price_mode_var9.set(value="6000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="2 Bedroom",textvariable=self.type_mode_var9, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="b1",textvariable=self.location_mode_var9, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000",textvariable=self.price_mode_var9, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book9, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

       # ================================10th Available House ==================================
             # ===============BOOK 1 VARIABLES =============
      self.type_mode_var10 = tk.StringVar()
      self.type_mode_var10.set(value="Single")
      self.location_mode_var10 = tk.StringVar()
      self.location_mode_var10.set(value="c3")
      self.price_mode_var10 = tk.StringVar()
      self.price_mode_var10.set(value="3000")
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Single",textvariable=self.type_mode_var10, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="c3",textvariable=self.location_mode_var10, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK C RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var10, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book10, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================11th Available House==================================

            # ===============BOOK 11 VARIABLES =============
      self.type_mode_var11 = tk.StringVar()
      self.type_mode_var11.set(value="1 Bedroom")
      self.location_mode_var11 = tk.StringVar()
      self.location_mode_var11.set(value="a1")
      self.price_mode_var11 = tk.StringVar()
      self.price_mode_var11.set(value="4000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="1 Bedroom",textvariable=self.type_mode_var11, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="b2",textvariable=self.location_mode_var11, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK B RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 3000",textvariable=self.price_mode_var11, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book11, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================12th Available house ==================================

      # ===============BOOK 12 VARIABLES =============
      self.type_mode_var12 = tk.StringVar()
      self.type_mode_var12.set(value="Bedsitter")
      self.location_mode_var12 = tk.StringVar()
      self.location_mode_var12.set(value="a1")
      self.price_mode_var12 = tk.StringVar()
      self.price_mode_var12.set(value="4000")
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter",textvariable=self.type_mode_var12, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var12, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var12, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book12, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================13th Available House  ==================================

      # ===============BOOK 13 VARIABLES =============
      self.type_mode_var13 = tk.StringVar()
      self.type_mode_var13.set(value="1 Bedroom")
      self.location_mode_var13 = tk.StringVar()
      self.location_mode_var13.set(value="a1")
      self.price_mode_var13 = tk.StringVar()
      self.price_mode_var13.set(value="5000")
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="1 Bedroom",textvariable=self.type_mode_var13, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var13, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 5000",textvariable=self.price_mode_var13, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book13, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================14th Available House==================================

            # ===============BOOK 14 VARIABLES =============
      self.type_mode_var14 = tk.StringVar()
      self.type_mode_var14.set(value="Bedsitter")
      self.location_mode_var14 = tk.StringVar()
      self.location_mode_var14.set(value="a3")
      self.price_mode_var14 = tk.StringVar()
      self.price_mode_var14.set(value="4000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter",textvariable=self.type_mode_var14, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3",textvariable=self.location_mode_var14, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000",textvariable=self.price_mode_var14, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book14, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================15th Available House ==================================

            # ===============BOOK 15 VARIABLES =============
      self.type_mode_var15 = tk.StringVar()
      self.type_mode_var15.set(value="2 Bedroom")
      self.location_mode_var15 = tk.StringVar()
      self.location_mode_var15.set(value="a1")
      self.price_mode_var15 = tk.StringVar()
      self.price_mode_var15.set(value="6000")

      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="2 Bedroom",textvariable=self.type_mode_var15, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a1",textvariable=self.location_mode_var15, font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000",textvariable=self.price_mode_var15, font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now",command=self.book15, width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      ctk.CTkLabel(rental_frame, text="No more available Rentals....", font=("Bookman Old Style", 20), fg_color="#0beba1", text_color="red").place(x=200, y=930)
      

   # =======================================payment page===========================
   def payment_view_fun(self):
      # Payment Main frame
      payment_main_frame = tk.Frame(self.page_frame, width=1000, height=800)
      payment_main_frame.place(x=0, y=10)


      #==========================Payment variables==========================================
      self.name_var =tk.StringVar()
      self.phone_var =tk.StringVar()
      self.id_var =tk.StringVar()
      self.mpesa_var =tk.StringVar()
      self.paybill_var =tk.StringVar()


      # Image to show Money
      image_left = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\profile.jpg")
      image_left = image_left.resize((950, 100))
      self.bg_photo = ImageTk.PhotoImage(image_left)

      image_lbl = tk.Label(payment_main_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=100)


      # ==========================label frame to show methods of payment========================================


      payment_mode_frame = tk.LabelFrame(payment_main_frame, text="Select Mode Of payment", font=("Bookman Old Style", 20), bg='#ffd6ff') 
      payment_mode_frame.place(x=1, y=90, width=980, height=150)

      # Mpesa Button

      mpesa_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\lipa mpesa.png")
      mpesa_img = mpesa_img.resize((190, 60))
      self.mpesa_photo = ImageTk.PhotoImage(mpesa_img)
      mpesa_btn = tk.Button(payment_mode_frame,text="", image=self.mpesa_photo, width=200, background="green", height=60, cursor="hand2")
      mpesa_btn.place(x=30, y=35)

      mpesa_btn.config(background="red")
      # mpesa label
      ctk.CTkLabel(payment_mode_frame, text="M-pesa", fg_color="green", width=100).place(x=80, y=3)

      # Bank Button
      bank_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\kcb bank.png")
      bank_img = bank_img.resize((200, 60))
      self.bank_photo = ImageTk.PhotoImage(bank_img)
      self.bank_btn = tk.Button(payment_mode_frame,text="", image=self.bank_photo,background="green", width=200, height=60, cursor="hand2", command=self.bank)
      self.bank_btn.place(x=330, y=35)
      
      # bank label
      ctk.CTkLabel(payment_mode_frame, text="KCB Bank", fg_color="green", width=100).place(x=390, y=3)

      # ATM Button
      atm_img =Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\atm bank.png")
      atm_img = atm_img.resize((190, 60))
      self.atm_photo = ImageTk.PhotoImage(atm_img)
      self.atm_btn = tk.Button(payment_mode_frame,text="", image=self.atm_photo, background="green",width=200, height=60, cursor="hand2", command=self.atm)
      self.atm_btn.place(x=630, y=35)

      # ATM label
      ctk.CTkLabel(payment_mode_frame, text="ATM Card", fg_color="green", width=100).place(x=685, y=3)


      # =============================label frame to show details for payment=========================
      pay = tk.LabelFrame(payment_main_frame, text="Complete Payment", font=("Bookman Old Style", 20),bg='#ffd6ff') 
      pay.place(x=1, y=240, width=980, height=280)

      # ==================================================== Full Name ============================
      # names label
      ctk.CTkLabel(pay, text="FULL NAMES", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=146, y=3)

      # Names Entry fields
      names_entry = ctk.CTkEntry(pay, corner_radius=0, textvariable=self.name_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      names_entry.place(x=82, y=40)
      names_entry.focus()

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=245, y=0)

      
      # ==================================================== PHONE NUMBER ============================
      # names label
      ctk.CTkLabel(pay, text="Valid Phone Number", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=142, y=90)

      # Names Entry fields
      phone_entry = ctk.CTkEntry(pay, corner_radius=0,textvariable=self.phone_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      phone_entry.place(x=82, y=120)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=297, y=90)

            
      # ==================================================== ID Number ============================
      # names label
      ctk.CTkLabel(pay, text="Valid ID Number", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=142, y=160)

      # Names Entry fields
      id_entry = ctk.CTkEntry(pay, corner_radius=0,textvariable=self.id_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      id_entry.place(x=82, y=190)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=270, y=162)

      # ==================================================== Mode of Payment ============================
      # mpesa mode label
      ctk.CTkLabel(pay, text="M-PESA MODE", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=610, y=3)

      # Mpesa mode Entry fields
      mpesa_mode_cmb = ctk.CTkComboBox(pay, values=["LIPA NA MPESA", "SEND MONEY"],state="readonly",corner_radius=0, border_width=2, border_color="pink",variable=self.mpesa_var,dropdown_fg_color="#0beba1", width=300,height=40,button_color="#0beba1", button_hover_color="#0beca1" )
      mpesa_mode_cmb.set("LIPA NA MPESA")
      mpesa_mode_cmb.place(x=540, y=40)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=740, y=0)

      
      # ==================================================== Paybill NUMBER ============================

      """Only available when the mode of payment selected is Lipa na Mpesa"""

      # paybill label
      ctk.CTkLabel(pay, text="PAYBILL", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=590, y=90)

      # paybill Entry fields
      """
      Paybill is always disabled and it should be displayed
      """
      paybill_entry = ctk.CTkEntry(pay, corner_radius=0, placeholder_text="0354734", border_width=2, border_color="pink",state=tk.DISABLED,width=300,height=40, fg_color="#8d99ae", font=("Bookman Old Style", 20))
      paybill_entry.place(x=540, y=120)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=680, y=90)

      # back to home button

      back_home = ctk.CTkButton(pay, text="<< Back",text_color="black",command=self.back_home_payment,  height=40, fg_color="green", font=("Bookman Old Style", 20), hover_color="light green")
      back_home.place(x=430, y=190)

      # clear  button

      clear_home = ctk.CTkButton(pay, text="Clear",  height=40, fg_color="green",text_color="black", font=("Bookman Old Style", 20), hover_color="light green", command=self.clear_payment)
      clear_home.place(x=600, y=190)

      # Complete payment  button

      back_home = ctk.CTkButton(pay, text="Complete Payment",  height=40, fg_color="green",text_color="black", font=("Bookman Old Style", 20), hover_color="light green", command=self.complete_payment)
      back_home.place(x=770, y=190)


            

   # =========================Notification ============================================
   def notification_view_fun(self):
      # Main fram for notification bar
      profile = tk.Frame(self.page_frame, width=1000, height=500)
      notification_frame = tk.LabelFrame(profile, text="Transaction", font=("Bookman Old Style", 20), bg="#00f5d4")
      notification_frame.place(x=1, y=1, width=990, height=500)
      profile.place(x=10, y=10)
      
      notification_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\transaction.png")
      notification_img = notification_img.resize((200, 100))
      self.bank_photo = ImageTk.PhotoImage(notification_img)
      self.bank_btn = tk.Label(notification_frame,text="", image=self.bank_photo, width=200, height=100)
      self.bank_btn.place(x=10, y=10)

      #tk.Label(notification_frame,image=notification_photo).place(x=0, y=0, width=300)

      transation_frame = tk.Frame(notification_frame)
      transation_frame.place(x=2, y=150, width=960, height=340)


      # Label to show the performance of the Tenant

      # to be replaced in future Since they are not resposible
      payment_state_lb = ctk.CTkLabel(notification_frame, text="",fg_color="light green",width=300, height=130)
      payment_state_lb.place(x=240, y=0)

      ctk.CTkLabel(payment_state_lb, text="Payment Status", font=("Bookman Old Style", 30)).place(x=40, y=5)
      check_box = ctk.CTkCheckBox(payment_state_lb, text="Done", font=("Bookman Old style", 30))
      check_box.place(x=60, y=70)

      payment_state_lb = ctk.CTkLabel(notification_frame, text="",fg_color="lightgreen",width=300, height=130)
      payment_state_lb.place(x=640, y=0)

      ctk.CTkLabel(payment_state_lb, text="Balance Status", font=("Bookman Old Style", 30)).place(x=40, y=5)
      check_box = ctk.CTkCheckBox(payment_state_lb, text="4,000", font=("Bookman Old style", 30))
      check_box.place(x=60, y=70)



      # Showing the tree view with the transation
      self.transtion_details = ttk.Treeview(transation_frame,columns=["month", "name", "id", "payment", "ref_no", "amount", "date","balance"])
      self.transtion_details.place(x=1, y=1, width=960, height=330)

      # scrollbar
      scroll_x = tk.Scrollbar(transation_frame, orient=tk.HORIZONTAL)
      scroll_y = tk.Scrollbar(transation_frame, orient=tk.VERTICAL)

      scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
      scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
      scroll_x.config(command=self.transtion_details.xview)
      scroll_y.config(command=self.transtion_details.yview)

      # showing the Heading of each column
      self.transtion_details.heading("month", text="Month")
      self.transtion_details.heading("name", text="Ful Name")
      self.transtion_details.heading("id", text="ID_No")
      self.transtion_details.heading("payment", text="Payment Mode")
      self.transtion_details.heading("ref_no", text="Ref No.")
      self.transtion_details.heading("amount", text="Amount Paid")
      self.transtion_details.heading("date", text="Date Of Payment")
      self.transtion_details.heading("balance", text="Balance")
      self.transtion_details["show"] = "headings"

      # setting the display width of each of column

      self.transtion_details.column("month", width=100)
      self.transtion_details.column("name", width=150)
      self.transtion_details.column("id", width=80)
      self.transtion_details.column("payment", width=100)
      self.transtion_details.column("ref_no", width=100)
      self.transtion_details.column("amount", width=80)
      self.transtion_details.column("date", width=100)
      self.transtion_details.column("balance", width=80)
   # profile  page

   # =============================================Profile decralation function=============================
   def profile_view_fun(self):

      # ==================================Profile variables ===============================================
      self.f_name_var = tk.StringVar() 
      self.l_name_var = tk.StringVar()
      self.email_var = tk.StringVar()
      self.f_phone_var = tk.StringVar()
      self.l_phone_var = tk.StringVar()
      self.dob_var = tk.StringVar()
      self.county_var = tk.StringVar()
      self.gender_var = tk.StringVar()
      self.house_var = tk.StringVar()
      self.id_no_var = tk.StringVar()

      # emergency 
      self.f_name_em_var = tk.StringVar()
      self.l_name_em_var = tk.StringVar()
      self.f_phone_em_var = tk.StringVar()
      self.l_phone_em_var = tk.StringVar()
      self.email_em_var = tk.StringVar()

      # Acceptance
      self.check_accept_var = tk.StringVar()
      self.check_terms_var = tk.StringVar()

      profile_frame = tk.Frame(self.page_frame, bg="green", width=1000, height=560)
      profile_frame.pack()

      # header frame to show the House icon and Description of the Page
      header_frame = tk.Frame(profile_frame)
      header_frame.place(x=4, y=2, width=990, height=100)

      # house Icon on the left side

      house_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\house_profile.png")
      house_img = house_img.resize((150, 80))
      self.bank_photo = ImageTk.PhotoImage(house_img)
      self.bank_btn = tk.Label(header_frame, image=self.bank_photo, width=200, height=100)
      self.bank_btn.place(x=1, y=0)

      # House icon on the right side
      house_img1 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\house_profile.png")
      house_img1 = house_img1.resize((150, 80))
      self.house_photo = ImageTk.PhotoImage(house_img1)
      self.bank_btn = tk.Label(header_frame, image=self.house_photo, width=200, height=100)
      self.bank_btn.place(x=800, y=0)

      # Label to show tenant need to Updte presonal Information

      ctk.CTkLabel(header_frame, text="TENANT PROFILE UPDATE FORM", font=("Bookman Old Style", 30)).place(x=250, y=35)

      #========================================= Personal information frame======================================

      personal_frame = tk.LabelFrame(profile_frame, text="Tenant Personal Details",bg='#ffd6ff', font=("Bookman Old Style", 15))
      personal_frame.place(x=4, y=110, width=500, height=415)

      # names label 
      ctk.CTkLabel(personal_frame, text="First Name", font=("Bookman Old Style", 15)).place(x=40, y=3)
      ctk.CTkLabel(personal_frame, text="Last Name", font=("Bookman Old Style", 15)).place(x=230, y=3)

      # Name Entry Fields
      f_name = ctk.CTkEntry(personal_frame ,textvariable=self.f_name_var, border_color="pink", corner_radius=0, width=160)
      f_name.place(x=10, y=27)

      # Last name field

      l_name = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.l_name_var, corner_radius=0, width=160)
      l_name.place(x=230, y=27)

      # Email Address
      ctk.CTkLabel(personal_frame, text="Email Address", font=("Bookman Old Style", 15)).place(x=80, y=60)

      email_address = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.email_var, corner_radius=0, width=300)
      email_address.place(x=10, y=90)

      # Phone Number label 
      ctk.CTkLabel(personal_frame, text="Phone Number", font=("Bookman Old Style", 15)).place(x=40, y=120)
      ctk.CTkLabel(personal_frame, text="Other Number", font=("Bookman Old Style", 15)).place(x=230, y=120)

      # Phone Number Entry Fields
      f_phone = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.f_phone_var, corner_radius=0, width=160)
      f_phone.place(x=10, y=150)

      # Last Phone number field

      l_phone= ctk.CTkEntry(personal_frame , border_color="pink", corner_radius=0,textvariable=self.l_phone_var, width=160)
      l_phone.place(x=230, y=150)

      # date of birth Address
      ctk.CTkLabel(personal_frame, text="Date of Birth", font=("Bookman Old Style", 15)).place(x=80, y=180)

      dob = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.dob_var, corner_radius=0, width=300)
      dob.place(x=10, y=210)

      # Home county field
      ctk.CTkLabel(personal_frame, text="Home County", font=("Bookman Old Style", 15)).place(x=40, y=240)

      home_county = ctk.CTkComboBox(personal_frame , border_color="pink", corner_radius=0,variable=self.county_var, width=180)
      home_county.configure(values=["Baringo",
         "Bomet","Bungoma","Busia","Elgeyo""-Marakwet","Embu","Garissa","Homa"" Bay","Isiolo","Kajiado","Kakamega","Kericho","Kiambu","Kilifi","Kirinyaga","Kisii","Kisumu",
         "Kitui","Kwale","Laikipia","Lamu","Machakos","Makueni","Mandera","Marsabit","Meru","Migori","Mombasa","Murang\'a","Nairobi"" City","Nakuru","Nandi","Narok","Nyamira",
         "Nyandarua","Nyeri","Samburu","Siaya","Taita","-Taveta","Tana River","Tharaka-Nithi","Trans Nzoia","Turkana","Uasin Gishu","Vihiga","Wajir","West Pokot"])
      home_county.set("Select Home County")
      home_county.place(x=10, y=270)

      # gender field
      ctk.CTkLabel(personal_frame, text="Gender ", font=("Bookman Old Style", 15)).place(x=40, y=300)

      gender = ctk.CTkComboBox(personal_frame , border_color="pink",values=["Male", "Female"],variable=self.gender_var, corner_radius=0, width=180)
      gender.place(x=10, y=330)
      gender.set("Male")

      # Type Of House

      ctk.CTkLabel(personal_frame, text="Type Of House ", font=("Bookman Old Style", 15)).place(x=250, y=240)

      house= ctk.CTkComboBox(personal_frame , border_color="pink",values=["a1", "a2", "a3"],variable=self.house_var, corner_radius=0, width=150)
      house.set("Select House Type")
      house.place(x=250, y=270)

      # Id number field
      ctk.CTkLabel(personal_frame, text="ID Number", font=("Bookman Old Style", 15)).place(x=250, y=300)

      id_no = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.id_no_var, corner_radius=0, width=200)
      id_no.place(x=250, y=330)

      

      # ===========================emergency information frame========================================

      emergency_frame = tk.LabelFrame(profile_frame, text="Emergency Details",bg='#ffd6ff', font=("Bookman Old Style", 15))
      emergency_frame.place(x=520, y=110, width=475, height=210)

      # names label 
      ctk.CTkLabel(emergency_frame, text="First Name", font=("Bookman Old Style", 15)).place(x=40, y=3)
      ctk.CTkLabel(emergency_frame, text="Last Name", font=("Bookman Old Style", 15)).place(x=230, y=3)

      # Name Entry Fields
      f_name_emergency = ctk.CTkEntry(emergency_frame ,textvariable=self.f_name_em_var, border_color="pink", corner_radius=0, width=160)
      f_name_emergency.place(x=10, y=27)

      # Last name field

      l_name_emergency = ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=160,textvariable=self.l_name_em_var)
      l_name_emergency.place(x=230, y=27)

      # Phone Number label 
      ctk.CTkLabel(emergency_frame, text="Phone Number", font=("Bookman Old Style", 15)).place(x=40, y=60)
      ctk.CTkLabel(emergency_frame, text="Other Number", font=("Bookman Old Style", 15)).place(x=230, y=60)

      # Phone Number Entry Fields
      f_phone_emergency = ctk.CTkEntry(emergency_frame , border_color="pink",textvariable=self.f_phone_em_var, corner_radius=0, width=160)
      f_phone_emergency.place(x=10, y=90)

      # Last Phone number field

      l_phone_emergency= ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=160,textvariable=self.l_phone_em_var)
      l_phone_emergency.place(x=230, y=90)

      # Email address field
      ctk.CTkLabel(emergency_frame, text="Email Address", font=("Bookman Old Style", 15)).place(x=10, y=120)

      email_emergency = ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=300,textvariable=self.email_em_var)
      email_emergency.place(x=10, y=145)




      # ===============================Acceptance  information frame========================================
      acceptance_frame = tk.LabelFrame(profile_frame, text="Acceptance And Signing off",bg='#ffd6ff', font=("Bookman Old Style", 15))
      acceptance_frame.place(x=520, y=323, width=475, height=100)

      # check box for acceptance
      check_accept = ctk.CTkCheckBox(acceptance_frame, text="I Accept to follow All Stipulated Rules of the House", font=("Bookman Old Style", 17), onvalue="yes", offvalue="no",variable=self.check_accept_var)
      check_accept.place(x=5, y=4)

      check_terms = ctk.CTkCheckBox(acceptance_frame, text="I Accept All terms And Conditions", font=("Bookman Old Style", 20), onvalue="yes", offvalue="no",variable=self.check_terms_var)
      check_terms.place(x=5, y=40)

      submit_frame = tk.Frame(profile_frame, bg='#ffd6ff')
      submit_frame.place(x=520, y=425, width=475, height=100)

      # back Changes Button
      clear_profile_btn = ctk.CTkButton(submit_frame,font=("Bookman Old style", 20),text="Clear", height=40, text_color="black", command=self.clear_profile)
      clear_profile_btn.place(x=20, y=30)

      # submit button

      submit_btn = ctk.CTkButton(submit_frame,font=("Bookman Old style", 20),text="Submit", height=40, fg_color="green", hover_color="#0beba1", text_color="black", command=self.submit_profile)
      submit_btn.place(x=260, y=30)

      

   # ====================================contact us page=====================================================
   def contact_view_fun(self):
      # contact Main Frame
      font = ("Bookman Old Style", 12)
      contact_frame = tk.Frame(self.page_frame, bg="green", width=1000, height=560)
      contact_frame.pack()

      # ========================Contact us variables========================================================
      self.tenant_id_var = tk.StringVar()
      self.email_contact = tk.StringVar()
      self.phone_contact = tk.StringVar()
      self.id_no_contact = tk.StringVar()
      self.username_contact = tk.StringVar()
      self.subject_var = tk.StringVar()
      self.message_var = tk.StringVar()




      # conatct Image
      contact_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\contact us.jpeg")
      contact_img = contact_img.resize((700, 140))
      self.contact_photo = ImageTk.PhotoImage(contact_img)

      ttk.Label(contact_frame, image=self.contact_photo, text="").place(x=10, y=10)

      text=ctk.CTkLabel(contact_frame, text="",fg_color="#bc6c25",corner_radius=20, width=240, height=150)
      text.place(x=730, y=2)

      # admin Name Inside a text Label
      ttk.Label(text, text="Admin Name:",background="#bc6c25", font=font).place(x=60, y=3)
      ttk.Label(text, text="Flivian",font=font).place(x=80, y=26)

      # admin Email
      ttk.Label(text, text="Admin Email:",background="#bc6c25", font=font).place(x=60, y=50)
      ttk.Label(text, text="flivian@gmail.com",font=font).place(x=50, y=70)

      # Admin Phone number

      ttk.Label(text, text="Admin Cell No:", background="#bc6c25",font=font).place(x=50, y=100)
      ttk.Label(text, text="0718017191",font=font).place(x=60, y=120)

      # label frame for Queries
      ticket_frame = tk.LabelFrame(contact_frame, text="Ticket Information",font=("Bookman Old Style", 20), width=960, height=370, bg="#80ffdb")
      ticket_frame.place(x=5, y=160)
      
      # Tenant Id Field
      ctk.CTkLabel(ticket_frame, text="Tenant Id", font=("Bookman Old Style", 20)).place(x=5, y=3)
      tenant_id = ctk.CTkEntry(ticket_frame, width=270,corner_radius=0, state=tk.DISABLED,textvariable=self.tenant_id_var, fg_color="#8d99ae")
      tenant_id.place(x=5, y=30)

      # Email address Field
      ctk.CTkLabel(ticket_frame, text="Email Address", font=("Bookman Old Style", 20)).place(x=5, y=60)
      email_contact = ctk.CTkEntry(ticket_frame,corner_radius=0,textvariable=self.email_contact, border_color="#c9184a", width=270)
      email_contact.place(x=5, y=90)
      email_contact.focus()

      # Phone Number Field
      ctk.CTkLabel(ticket_frame, text="Phone Number", font=("Bookman Old Style", 20)).place(x=5, y=120)
      phone_contact = ctk.CTkEntry(ticket_frame, width=270,corner_radius=0,textvariable=self.phone_contact, border_color="#c9184a")
      phone_contact.place(x=5, y=150)

      # Id Number Field
      ctk.CTkLabel(ticket_frame, text="National ID", font=("Bookman Old Style", 20)).place(x=5, y=180)
      id_no_contact = ctk.CTkEntry(ticket_frame, width=270, corner_radius=0,textvariable=self.id_no_contact, border_color="#c9184a")
      id_no_contact.place(x=5, y=210)

      # username Field
      ctk.CTkLabel(ticket_frame, text="Username", font=("Bookman Old Style", 20)).place(x=5, y=240)
      username_contact = ctk.CTkEntry(ticket_frame, width=270,textvariable=self.username_contact, corner_radius=0, border_color="#c9184a")
      username_contact.place(x=5, y=270)

      # text box widget for subject
      ctk.CTkLabel(ticket_frame, text="---------------------- Subject Matter -------------------------------", font=("Bookman Old Style", 20)).place(x=290, y=5)
      subject_text = ctk.CTkTextbox(ticket_frame, height=50, width=600, font=("Bookman Old style", 20))
      subject_text.place(x=300, y=30)
      #subject_text.focus()


      # text box widget
      ctk.CTkLabel(ticket_frame, text="---------------------- Message -------------------------------------", font=("Bookman Old Style", 20)).place(x=290, y=80)
      message_text = ctk.CTkTextbox(ticket_frame, height=150,fg_color="#e7ecef", width=600, corner_radius=0, font=("Bookman Old style", 20))
      #message_text.focus()
      message_text.place(x=300, y=140)

      # frame for button to change property in textbox
      icon_frame = ctk.CTkFrame(ticket_frame, width=600, height=40, fg_color="white", corner_radius=0)
      icon_frame.place(x=300, y=105)

      # icons
      # bold icon
      bold_img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\bold.png")
      bold_img = bold_img.resize((20, 25))
      self.bold_photo = ImageTk.PhotoImage(bold_img)

      bold_btn = tk.Button(icon_frame, image=self.bold_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      bold_btn.place(x=4, y=7)

      # italic icon
      italic_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\italic.png")
      italic_icon = italic_icon.resize((15, 18))
      self.italic_photo = ImageTk.PhotoImage(italic_icon)

      italic_btn = tk.Button(icon_frame, image=self.italic_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      italic_btn.place(x=45, y=10)

      # copy icon
      copy_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\copy.jpg")
      copy_icon = copy_icon.resize((30, 25))
      self.copy_photo = ImageTk.PhotoImage(copy_icon)

      copy_btn = tk.Button(icon_frame, image=self.copy_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      copy_btn.place(x=80, y=5)

      # paste icon
      paste_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\paste.png")
      paste_icon = paste_icon.resize((30, 25))
      self.paste_photo = ImageTk.PhotoImage(paste_icon)

      paste_btn = tk.Button(icon_frame, image=self.paste_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      paste_btn.place(x=120, y=5)

      # font icon
      font_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\font.png")
      font_icon = font_icon.resize((30, 25))
      self.font_photo = ImageTk.PhotoImage(font_icon)

      font_btn = tk.Button(icon_frame, image=self.font_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      font_btn.place(x=170, y=5)

      # center icon
      center_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\center.png")
      center_icon = center_icon.resize((30, 25))
      self.center_photo = ImageTk.PhotoImage(center_icon)

      center_btn = tk.Button(icon_frame, image=self.center_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      center_btn.place(x=210, y=5)

      # copy icon
      justify_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\justify.png")
      justify_icon = justify_icon.resize((30, 25))
      self.justify_photo = ImageTk.PhotoImage(justify_icon)

      justify_btn = tk.Button(icon_frame, image=self.justify_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      justify_btn.place(x=250, y=5)

      # attach icon
      attach_icon = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\attach file.png")
      attach_icon = attach_icon.resize((30, 25))
      self.attach_photo = ImageTk.PhotoImage(attach_icon)

      ctk.CTkLabel(icon_frame, text="Attach File", font=('Bookman Old style', 20)).place(x=490, y=5)
      attach_btn = tk.Button(icon_frame, image=self.attach_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      attach_btn.place(x=440, y=5)

      # Submit Button
      clear_ticket_btn = ctk.CTkButton(ticket_frame, text="Clear",text_color="black" ,font=('Bookman Old style', 20), height=35, cursor="hand2", command=self.clear_contact)
      clear_ticket_btn.place(x=500, y=295)

      # Submit Button
      submit_ticket_btn = ctk.CTkButton(ticket_frame, text="Submit",hover_color="#55a630", font=('Bookman Old style', 20),fg_color="green", height=35, text_color="black" ,cursor="hand2", command=self.submit_contact)
      submit_ticket_btn.place(x=700, y=295)
      
           

   # logout page
   def logout_view_fun(self):

      # ===================background Image for Rental Houses when exiting===========================
      image_left = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\rental.jpg")
      image_left = image_left.resize((990, 530))
      self.bg_photo = ImageTk.PhotoImage(image_left)

      image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=530)
      time.sleep(1)
      respose = messagebox.askquestion(title="Logout Status", message="Are you sure you want to Exit? ", parent=self.root)
      if respose == "yes":
         time.sleep(0)
         self.root.destroy()
      else:
         self.rental_view_fun()

   # to delete the current packed frame and load the next
   def delete_page(self):
      for frame in self.page_frame.winfo_children():
         frame.destroy()

   # ====================================Functtions for House ===================================
   def house_btn_click(self):
      self.house_btn.configure(border_width=2, border_color="red")

   def on_configure(self,event):
      self.canvas.configure(scrollregion=self.canvas.bbox("all"))


   def change(self,lb):
      lb.config(bg="red")


   # ==============================Payment Function Decration========================================
   def complete_payment(self):
      if self.name_var.get() == "":
         messagebox.showerror(title="Payment status", message="Full names must be Filled!!!", parent=self.root)
      elif self.phone_var.get() == "":
         messagebox.showerror(title="Payment status", message="Phone Number must be Filled!!!", parent=self.root)
      elif len(self.phone_var.get()) < 10:
         messagebox.showerror(title="Payment status", message="Phone Number must be More Than 9 !!", parent=self.root)
      elif len(self.phone_var.get()) > 14:
         messagebox.showerror(title="Payment status", message="phone Number should be Less Than 14!!!", parent=self.root)
      elif self.id_var.get() == "":
         messagebox.showerror(title="Payment status", message="Id Number must be Filled!!!", parent=self.root)
      elif len(self.id_var.get()) != 8:
         messagebox.showerror(title="Payment status", message="Id Number Must be 8 Characters!!!", parent=self.root)
      elif self.mpesa_var.get() =="":
         messagebox.showerror(title="Payment status", message="Mpesa Mode Must be Filled!!!", parent=self.root)
      else:
         try:
            #Need to connect With the database to record data there
            pass
         except:
            pass
   #==========================clear records================================
   def clear_payment(self):
      self.name_var.set("")
      self.phone_var.set("")
      self.id_var.set("")
      self.mpesa_var.set("LIPA NA MPESA")

   def back_home_payment(self):
      answer = messagebox.askyesno(title="Payment Status", message="Are You sure You want to Exit payment page", parent=self.root)
      if answer == True:
         self.hide_indicator()
         # ===================background Image for Rental Houses when exiting===========================
         image_left = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\RENTAL MANAGEMENT SYSTEM\images\rental.jpg")
         image_left = image_left.resize((990, 530))
         self.bg_photo = ImageTk.PhotoImage(image_left)

         image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
         image_lbl.place(x=0, y=0, width=1000, height=530)
      else:
         pass
   
   # ===========================Profile Function Declaration =============================================
   def submit_profile(self):
      if self.f_name_var.get() == "":
         messagebox.showerror(title="Profile Status", message="First Name Must be Filled!!", parent=self.root)
      elif self.l_name_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Last Name Must be Filled!!", parent=self.root)
      elif self.email_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Email Address Must be Filled!!", parent=self.root)
      elif self.f_phone_var.get() == "" and self.l_phone_var.get() == "":
         messagebox.showerror(title="Profile Status", message="One Phone Number Must be Filled!!", parent=self.root)
      elif len(self.f_phone_var.get() and self.l_phone_var.get()) > 14:
         messagebox.showerror(title="Profile Status", message="Phone Number Should Be Less than 14 characters!!", parent=self.root)
      elif len(self.f_phone_var.get() and self.l_phone_var.get()) < 10:
         messagebox.showerror(title="Profile Status", message="Phone Number Should Be more than 9 characters!!", parent=self.root)
      elif self.dob_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Date of Birth Must be Filled!!", parent=self.root)
      elif self.gender_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Gender Must be Selected!!", parent=self.root)
      elif self.house_var.get() == "":
         messagebox.showerror(title="Profile Status", message="House Type must be selected!!", parent=self.root)
      elif self.id_no_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Id Number Must be Filled!!", parent=self.root)
      elif len(self.id_no_var.get()) != 8:
         messagebox.showerror(title="Profile Status", message="Id Number Must be 8 Characters!!", parent=self.root)
      # emergency
      elif self.f_name_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency First Name Must be Filled!!", parent=self.root)
      elif self.l_name_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency Last Name Must be Filled!!", parent=self.root)
      elif self.f_phone_em_var.get() == "" and self.l_phone_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Phone Number Must be Filled On Emergency!!", parent=self.root)
      elif len(self.f_phone_em_var.get() and self.l_phone_em_var.get()) > 14:
         messagebox.showerror(title="Profile Status", message="Emergency Phone Number Should Be Less than 14 characters!!", parent=self.root)
      elif len(self.f_phone_em_var.get() and self.l_phone_em_var.get()) < 10:
         messagebox.showerror(title="Profile Status", message="Emergency Phone Number Should Be more than 9 characters!!", parent=self.root)
      elif self.email_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency Email Address Must be Filled!!", parent=self.root)
      #Acceptance
      elif self.check_accept_var.get() != "yes":
         messagebox.showerror(title="Profile Status", message="You need To Accept stipulated Rules before proceeding!!", parent=self.root)

      elif self.check_terms_var.get() != "yes":
         messagebox.showerror(title="Profile Status", message="You need To Accept Terms and conditions  before proceeding!!", parent=self.root)

      else:
         try:
            conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
            # print(conn)
            cur = conn.cursor()
            cur.execute("INSERT INTO tenant_personal_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                 self.f_name_var.get(),
                                 self.l_name_var.get(),
                                 self.email_var.get(),
                                 self.f_phone_var.get(),
                                 self.l_phone_var.get(),
                                 self.dob_var.get(),
                                 self.county_var.get(),
                                 self.gender_var.get(),
                                 self.house_var.get(),
                                 self.id_no_var.get(),
                                 self.check_accept_var.get(),
                                 self.check_terms_var.get()
            ))

            conn1 = mysql.connect(host="localhost",username="root", password="flivian254", database="mydb")
            cur1 = conn1.cursor()
            cur1.execute("INSERT INTO tenant_emergency_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                                 self.f_name_var.get(),
                                 self.l_name_var.get(),
                                 self.email_var.get(),
                                 self.f_name_em_var.get(),
                                 self.l_name_em_var.get(),
                                 self.f_phone_em_var.get(),
                                 self.l_phone_em_var.get(),
                                 self.email_em_var.get()
            ))

            update = messagebox.askyesno(title="Profile Status", message=f"{self.f_name_var.get()}, Do you want to submit This information? ", parent=self.root)
            if update > 0:
               conn.commit()
               conn1.commit()
               conn.close()
               conn1.close()
               messagebox.showinfo(title="Profile Status", message="Record Updated Successfully", parent= self.root)
            else:
               pass
         except Exception as es:
            error = messagebox.showerror(title="Profile Status", message=f"Error Due to: {str(es)}", parent= self.root)
            # print(str(es))

   def clear_profile(self):
      self.f_name_var.set("")
      self.l_name_var.set("")
      self.email_var.set("")
      self.f_phone_var.set("")
      self.l_phone_var.set("")
      self.dob_var.set("")
      self.county_var.set("Select Home  County")
      self.gender_var.set("")
      self.house_var.set("Select House Type")
      self.id_no_var.set("")
      self.f_name_em_var.set("")
      self.l_name_em_var.set("")
      self.f_phone_em_var.set("")
      self.l_phone_em_var.set("")
      self.email_em_var.set("")
      self.check_accept_var.set("no")
      self.check_terms_var.set("no")

   #====================== Contact us function declaration============================
   def submit_contact(self):
      """
        if self.tenant_id_var.get() == "":
         messagebox.
      """
      if self.email_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Email Address Must be Filled!!!", parent=self.root)
      elif self.phone_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Phone Number Must be Filled!!!", parent=self.root)
      elif len(self.phone_contact.get()) < 10:
         messagebox.showerror(title="Contact status", message="Phone Number should be more than 9 characters!!!", parent=self.root)
      elif len(self.phone_contact.get()) > 14:
         messagebox.showerror(title="Contact status", message="Phone Number should be less than 14 characters!!!", parent=self.root)
      elif self.id_no_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Id Number Must be Filled!!!", parent=self.root)
      elif len(self.id_no_contact.get()) != 8:
         messagebox.showerror(title="Contact status", message="Phone Number Must be Filled!!!", parent=self.root)
      elif self.username_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Username Must be Filled!!!", parent=self.root)
         """
         self.subject_var(self) == "":
         self.message-var(self) == "":
         
         """
      else:
         try:
            # Connect with database to save the records, Send the email to the company Email
            pass
         except:
            pass

   # ========clear contact ===========================
   def clear_contact(self):
      self.email_contact.set("")
      self.phone_contact.set("")
      self.id_no_contact.set("")
      self.username_contact.set("")

   def bank(self):
      messagebox.showwarning(title="Bank Status", message="Opps An Error Occured When Loading Bank Option!!!", parent = self.root)

   def atm(self):
      messagebox.showwarning(title="Atm Status", message="Opps An Error Occured When Loading ATM Option!!!", parent = self.root)


   # ======================================================== BOOK1 OPTIONS =================================================
   def book1(self):
      type_book1 = self.type_mode_var1.get()
      location_book1 = self.location_mode_var1.get()
      price_book1 = self.price_mode_var1.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book1_window = tk.Toplevel(self.root)
      Second_window(book1_window, type_book1,location_book1,price_book1, payment)
   
   # ======================================================== BOOK2 OPTIONS =================================================
   def book2(self):
      type_book2 = self.type_mode_var2.get()
      location_book2 = self.location_mode_var2.get()
      price_book2 = self.price_mode_var2.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book2_window = tk.Toplevel(self.root)
      Second_window(book2_window, type_book2,location_book2,price_book2, payment)

   
   # ======================================================== BOOK3 OPTIONS =================================================
   def book3(self):
      type_book3 = self.type_mode_var3.get()
      location_book3 = self.location_mode_var3.get()
      price_book3 = self.price_mode_var3.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book3_window = tk.Toplevel(self.root)
      Second_window(book3_window, type_book3,location_book3,price_book3, payment)
   
   # ======================================================== BOOK4 OPTIONS =================================================
   def book4(self):
      type_book4 = self.type_mode_var4.get()
      location_book4 = self.location_mode_var4.get()
      price_book4 = self.price_mode_var4.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book4_window = tk.Toplevel(self.root)
      Second_window(book4_window, type_book4,location_book4,price_book4, payment)

   
   # ======================================================== BOOK5 OPTIONS =================================================
   def book5(self):
      type_book5 = self.type_mode_var5.get()
      location_book5 = self.location_mode_var5.get()
      price_book5 = self.price_mode_var5.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book5_window = tk.Toplevel(self.root)
      Second_window(book5_window, type_book5,location_book5,price_book5, payment)

   
   # ======================================================== BOOK6 OPTIONS =================================================
   def book6(self):
      type_book6 = self.type_mode_var6.get()
      location_book6 = self.location_mode_var6.get()
      price_book6 = self.price_mode_var6.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book6_window = tk.Toplevel(self.root)
      Second_window(book6_window, type_book6,location_book6,price_book6, payment)
   
   # ======================================================== BOOK7 OPTIONS =================================================
   def book7(self):
      type_book7 = self.type_mode_var7.get()
      location_book7 = self.location_mode_var7.get()
      price_book7 = self.price_mode_var7.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book7_window = tk.Toplevel(self.root)
      Second_window(book7_window, type_book7,location_book7,price_book7, payment)
   
   
   # ======================================================== BOOK2 OPTIONS =================================================
   def book8(self):
      type_book8 = self.type_mode_var8.get()
      location_book8 = self.location_mode_var8.get()
      price_book8 = self.price_mode_var8.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book8_window = tk.Toplevel(self.root)
      Second_window(book8_window, type_book8,location_book8,price_book8, payment)
   
   
   # ======================================================== BOOK2 OPTIONS =================================================
   def book9(self):
      type_book9 = self.type_mode_var9.get()
      location_book9 = self.location_mode_var9.get()
      price_book9 = self.price_mode_var9.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book9_window = tk.Toplevel(self.root)
      Second_window(book9_window, type_book9,location_book9,price_book9, payment)

   
   # ======================================================== BOOK2 OPTIONS =================================================
   def book10(self):
      type_book10 = self.type_mode_var10.get()
      location_book10 = self.location_mode_var10.get()
      price_book10 = self.price_mode_var10.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book10_window = tk.Toplevel(self.root)
      Second_window(book10_window, type_book10,location_book10,price_book10, payment)

   # ======================================================== BOOK2 OPTIONS =================================================
   def book11(self):
      type_book11 = self.type_mode_var11.get()
      location_book11 = self.location_mode_var11.get()
      price_book11 = self.price_mode_var11.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book11_window = tk.Toplevel(self.root)
      Second_window(book11_window, type_book11,location_book11,price_book11, payment)

   # ======================================================== BOOK2 OPTIONS =================================================
   def book12(self):
      type_book12 = self.type_mode_var12.get()
      location_book12 = self.location_mode_var12.get()
      price_book12 = self.price_mode_var12.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book12_window = tk.Toplevel(self.root)
      Second_window(book12_window, type_book12,location_book12,price_book12, payment)

   # ======================================================== BOOK2 OPTIONS =================================================
   def book13(self):
      type_book13 = self.type_mode_var13.get()
      location_book13 = self.location_mode_var13.get()
      price_book13 = self.price_mode_var13.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book13_window = tk.Toplevel(self.root)
      Second_window(book13_window, type_book13,location_book13,price_book13, payment)

   # ======================================================== BOOK2 OPTIONS =================================================
   def book14(self):
      type_book14 = self.type_mode_var14.get()
      location_book14 = self.location_mode_var14.get()
      price_book14 = self.price_mode_var14.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book14_window = tk.Toplevel(self.root)
      Second_window(book14_window, type_book14,location_book14,price_book14, payment)

   # ======================================================== BOOK2 OPTIONS =================================================
   def book15(self):
      type_book15 = self.type_mode_var15.get()
      location_book15 = self.location_mode_var15.get()
      price_book15 = self.price_mode_var15.get()
      payment = self.payment_view_fun()
      # tenant = self.tenant_view_fun()

      book15_window = tk.Toplevel(self.root)
      Second_window(book15_window, type_book15,location_book15,price_book15, payment)


# ===========================New window to show the book1 =================================================================
class Second_window():
   def __init__(self,root, type_book1,location_book1,price_book1, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book1}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book1}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book1}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)


      
   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()
   # if __name__ == '__main__':
   #    root = tk.Toplevel()
   #    Second_window(root)
   #    root.mainloop()



# ===========================New window to show the book2 =================================================================
class Second_window():
   def __init__(self,root, type_book2,location_book2,price_book2, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book2}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book2}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book2}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)


      
   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()


# ===========================New window to show the book3 =================================================================
class Second_window():
   def __init__(self,root, type_book3,location_book3,price_book3, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book3}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book3}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book3}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)


      
   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()

# ===========================New window to show the book4 =================================================================
class Second_window():
   def __init__(self,root, type_book4,location_book4,price_book4, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book4}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book4}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book4}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)
   
   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()5

   

# ===========================New window to show the book5 =================================================================
class Second_window():
   def __init__(self,root, type_book5,location_book5,price_book5, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book5}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book5}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book5}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()5

# ===========================New window to show the book6 =================================================================
class Second_window():
   def __init__(self,root, type_book6,location_book6,price_book6, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book6}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book6}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book6}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()


# ===========================New window to show the book7 =================================================================
class Second_window():
   def __init__(self,root, type_book7,location_book7,price_book7, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book7}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book7}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book7}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()

# ===========================New window to show the book8 =================================================================
class Second_window():
   def __init__(self,root, type_book8,location_book8,price_book8, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book8}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book8}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book8}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()8

# ===========================New window to show the book9 =================================================================
class Second_window():
   def __init__(self,root, type_book9,location_book9,price_book9, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book9}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book9}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book9}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()9

# ===========================New window to show the book10 =================================================================
class Second_window():
   def __init__(self,root, type_book10,location_book10,price_book10, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book10}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book10}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book10}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(1)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()

# ===========================New window to show the book6 =================================================================
class Second_window():
   def __init__(self,root, type_book11,location_book11,price_book11, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book11}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book11}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book11}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()11

# ===========================New window to show the book12 =================================================================
class Second_window():
   def __init__(self,root, type_book12,location_book12,price_book12, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book12}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book12}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book12}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()

# ===========================New window to show the book6 =================================================================
class Second_window():
   def __init__(self,root, type_book13,location_book13,price_book13, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book13}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book13}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book13}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()

# ===========================New window to show the book6 =================================================================
class Second_window():
   def __init__(self,root, type_book14,location_book14,price_book14, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book14}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book14}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book14}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()14

# ===========================New window to show the book6 =================================================================
class Second_window():
   def __init__(self,root, type_book15,location_book15,price_book15, payment):
      self.root = root
      self.root.title("Book Now")
      self.root.geometry("720x400+300+100")
      # Left frame
      left_frame = tk.Frame(self.root, bg="white")
      left_frame.place(x=0, y=3, width=400, height=380)

      ctk.CTkLabel(left_frame, text="Book Now", width=400, bg_color="yellow", height=60, font=("Bookman Old Style", 20)).place(x=0, y=2)

      ctk.CTkLabel(left_frame, text="Type of House", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=80)
      ctk.CTkLabel(left_frame, text=f"{type_book15}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=120)

      
      ctk.CTkLabel(left_frame, text="House Location", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=155)
      ctk.CTkLabel(left_frame, text=f"{location_book15}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=190)

      ctk.CTkLabel(left_frame, text="House Price", width=400,fg_color="green", font=("Bookman Old Style", 20)).place(x=0, y=240)
      ctk.CTkLabel(left_frame, text=f"{price_book15}", bg_color="light gray", text_color="black", width=400, height=30, font=("Bookman Old style", 20)).place(x=0, y=280)

      back_book_btn = ctk.CTkButton(left_frame,  text="back",command=self.back_book, fg_color="black", corner_radius=0)
      back_book_btn.place(x=10, y=330)

      back_book_btn = ctk.CTkButton(left_frame,command=self.proceed_book1,  text="Proceed", fg_color="green", corner_radius=0)
      back_book_btn.place(x=250, y=330)




      right_frame = tk.Frame(self.root)
      right_frame.place(x=410, y=3, width=300, height=380)
      try:
         image_left = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/rental2.jpg").convert("RGB")
         image_left = image_left.resize((290,330))
         self.bg_photo = ImageTk.PhotoImage(image_left)
         # print(image_left.size)
      
         image_left_label = ttk.Label(right_frame, image=self.bg_photo)
         image_left_label.place(x=0, y=0)
      except Exception as e:
         print(f"Error loading image: {e}")

      # backward icon to scroll images
      back_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/back.png").convert("RGB")
      back_icon = back_icon.resize((50,30))
      self.backward_icon = ImageTk.PhotoImage(back_icon)
      backward_lbl = ttk.Button(right_frame, image=self.backward_icon)
      backward_lbl.place(x=10, y=340)

      # forward icon to scroll images
      forward_icon = Image.open("C:/Users/Flivian/Desktop/PROJECTS/RENTAL MANAGEMENT SYSTEM/images/forward.png").convert("RGB")
      forward_icon = forward_icon.resize((50,30))
      self.forward_icon = ImageTk.PhotoImage(forward_icon)
      forward_lbl = ttk.Button(right_frame, image=self.forward_icon)
      forward_lbl.place(x=200, y=340)

   def back_book(self):
      time.sleep(2)
      self.root.destroy()
      # self.root.destroy()
   def proceed_book1(self):
      self.root.destroy()
      #self.payment = self.payment_view_fun()15




# =======================================Sign up ==================================================
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
                length_code = 3
                random_no = generate_tenant_code(length_code)
                tenant_id = f"GRT1{random_no}"
                
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
                        username = self.username_var.get()
                        self.app = tk.Toplevel(self.root1)
                        self.new_app = Tenant_management_main(self.app, username)
                                          
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
    obj = Login(root1)
    root1.mainloop()