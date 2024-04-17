from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
import os
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import Label, PhotoImage
from PIL import ImageTk, Image


#global variable
left_x=200
right_x=700

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


profile=tk.Tk()
profile.title("profile_window")
profile.geometry("1080x800")
profile.config(bg="#0069D9")
#profile.resizable(False,False)


label1=ttk.Label(profile,text="TENANT PROFILE UPDATE FORM",font="times 27",background="#0069D9").pack(pady=20)
#logo
image = Image.open(resource_path("pic2.png"))
image = image.resize((100, 70))  # Adjust the size according to your needs
photo = ImageTk.PhotoImage(image)
label = Label(profile, image=photo, bg="#0069D9",fg="green")
label.place(x=30,y=60)

image2 = Image.open(resource_path("pic2.png"))
image2 = image.resize((100, 70))  # Adjust the size according to your needs
photo2 = ImageTk.PhotoImage(image2)
label2 = Label(profile, image=photo, bg="#0069D9",fg="green")
label2.place(x=50,y=60)
#frame for personal details

first=tk.Label(profile,text="First Name",font="arial 20",bg="#0069D9")
first.place(x=left_x,y=90)
first_entry=ctk.CTkEntry(master=profile,text_color="black",width=180,height=33)
first_entry.place(x=left_x,y=130)
#must
image3 = Image.open(resource_path("star.png"))
image3 = image.resize((50,50))  # Adjust the size according to your needs
photo3 = ImageTk.PhotoImage(image3)
label3 = Label(profile, image=photo, bg="#0069D9",fg="green")
label3.place(x=1200,y=60)

#must
'''
image4 = Image.open(resource_path("star.png"))
image4 = image.resize((50, 50))  # Adjust the size according to your needs
photo4 = ImageTk.PhotoImage(image4)
label4 = Label(profile, image=photo, bg="#0069D9",fg="green")
label4.place(x=1200,y=60)
'''
second=tk.Label(profile,text="Last Name",font="arial 20",bg="#0069D9")
second.place(x=410,y=90)
second_entry=ctk.CTkEntry(master=profile,text_color="black",width=190,height=33)
second_entry.place(x=410,y=130)

email_add=tk.Label(text="Email Address",font="arial 20",bg="#0069D9")
email_add.place(x=left_x,y=180)
email_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
email_entry.place(x=left_x,y=220)

dob=tk.Label(text="Date of Birth",font="arial 20",bg="#0069D9")
dob.place(x=left_x,y=270)
dob_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
dob_entry.place(x=left_x,y=310)

homecountry=tk.Label(text="Home County",font="arial 20",bg="#0069D9")
homecountry.place(x=left_x,y=360)
homecountry_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
homecountry_entry.place(x=left_x,y=400)

radial_var = tk.StringVar()
gender=tk.Label(text="Select gender",font="arial 20",bg="#0069D9")
gender.place(x=left_x,y=450)
gender_check1=ttk.Radiobutton(text="Male",value="btn1")
gender_check1.place(x=left_x,y=500)
gender_check2=ttk.Radiobutton(text="Female",value="btn2")
gender_check2.place(x=280,y=500)
gender_check3=ttk.Radiobutton(text="Rather not say",value="btn3")
gender_check3.place(x=370,y=500)

idnumber=tk.Label(text="ID number",font="arial 20",bg="#0069D9")
idnumber.place(x=left_x,y=540)
idnumber_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
idnumber_entry.place(x=left_x,y=590)

typehouse=tk.Label(text="Types of House",font="arial 20",bg="#0069D9")
typehouse.place(x=left_x,y=630)
typehouse_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
typehouse_entry.place(x=left_x,y=670)

#emergency details

first2=tk.Label(profile,text="First Name",font="arial 20",bg="#0069D9")
first2.place(x=right_x,y=90)
first_entry2=ctk.CTkEntry(master=profile,text_color="black",width=180,height=33)
first_entry2.place(x=right_x,y=130)

second2=tk.Label(profile,text="Last Name",font="arial 20",bg="#0069D9")
second2.place(x=910,y=90)
second_entry2=ctk.CTkEntry(master=profile,text_color="black",width=190,height=33)
second_entry2.place(x=910,y=130)

phonenumber=tk.Label(text="Phone number 1",font="arial 20",bg="#0069D9")
phonenumber.place(x=right_x,y=180)
phonenumber_entry=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
phonenumber_entry.place(x=right_x,y=220)

phonenumber2=tk.Label(text="Phone number 2",font="arial 20",bg="#0069D9")
phonenumber2.place(x=right_x,y=270)
phonenumber_entry2=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
phonenumber_entry2.place(x=right_x,y=310)

email_add2=tk.Label(text="Email address",font="arial 20",bg="#0069D9")
email_add2.place(x=right_x,y=360)
email_entry2=ctk.CTkEntry(master=profile,text_color="black",width=400,height=33)
email_entry2.place(x=right_x,y=400)

accept_label=tk.Label(text="Acceptance and Signoff",font="arial 20",bg="#0069D9",fg="white")
accept_label.place(x=740,y=460)
follow_rules=tk.Label(text="Accept to follow all rules of house",font="arial 20",bg="#0069D9")
follow_rules.place(x=680,y=500)

radial_var2 = tk.StringVar()
yes_check4=ttk.Radiobutton(text="Yes",variable=radial_var2,value="radial4")
yes_check4.place(x=800,y=550)
no_check5=ttk.Radiobutton(text="No",variable=radial_var2,value="radial5")
no_check5.place(x=900,y=550)

terms_conditions=tk.Label(text="Accept all terms and conditions",font="arial 20",bg="#0069D9")
terms_conditions.place(x=680,y=580)
radial_var3 = tk.StringVar()
accept_check4=ttk.Radiobutton(text="Accept",variable=radial_var3,value="accept")
accept_check4.place(x=700,y=630)

def submit_fxn():
    messagebox.showinfo("records","Profile details saved and submitted successfully")
def back_home():
    messagebox.showinfo("To home","Program looped to home")

btnsubmit=tk.Button(text="Submit",font="arial 15",width=10,bg="#48596b",fg="white",command=submit_fxn)
btnsubmit.place(x=770,y=670)
btnback=tk.Button(text="Back Home",font="arial 15",width=10,bg="#48596b",fg="white",command=back_home)
btnback.place(x=920,y=670)

#window loop
def toggle_fullscreen(event=None):
    print("virus function")
    profile.attributes("-fullscreen", not profile.attributes("-fullscreen"))


profile.bind("<F11>", toggle_fullscreen)
profile.bind("<Escape>", toggle_fullscreen)
profile.attributes("-fullscreen", True)
center_window(profile)
profile.mainloop()


