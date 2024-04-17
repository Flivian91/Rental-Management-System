from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql
import random as re
import string


class Loan():
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1000x600+120+20")

        # Generate random Employee Id.
        def generate_random_id(length):
            numbers =string.digits
            random_number = "".join(re.choices(numbers , k=length))
            return random_number
        length_random = 2
        number_generated = generate_random_id(length_random)
        self.random_id = f"AK{number_generated}"
        # print(self.random_id)

        # =======================================Variables======================================================================
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.role_var = StringVar()
        self.gender_var = StringVar()
        self.status_var = StringVar()

        Label(self.root, text="EMPLOYEE MANAGEMENT SYSTEM", font=("Bookman Old Style", 25), bg="red").place(x=0, y=5, width=1000)
        
        # left frame Section
        left_frame = Frame(self.root, width=400, height=450)
        left_frame.place(x=2, y=50)

        # right frame section
        right_frame = Frame(self.root, width=580, height=450, relief=RIDGE)
        right_frame.place(x=410, y=50)

        # Botton Frame Section
        bottom_frame = Frame(self.root, width=990, height=80)
        bottom_frame.place(x=3, y=510)
        
        # Labels Details
        Label(left_frame, text="ID", font=("Bookman Old Style", 17)).place(x=5, y=5)
        Label(left_frame, text="Name", font=("Bookman Old Style", 17)).place(x=5, y=80)
        Label(left_frame, text="Role", font=("Bookman Old Style", 17)).place(x=5, y=160)
        Label(left_frame, text="Gender", font=("Bookman Old Style", 17)).place(x=5, y=240)
        Label(left_frame, text="Status", font=("Bookman Old Style", 17)).place(x=5, y=320)

        # Entry Fields
        #  Id Field
        id = CTkEntry(left_frame,textvariable=self.id_var,state="disabled", font=("Bookman Old style", 15), height=40, width=250, border_width=1, border_color="red", corner_radius=3)
        id.place(x=120, y=5)
        self.id_var.set(value=self.random_id)


        # name field
        name = CTkEntry(left_frame,textvariable=self.name_var, font=("Bookman Old style", 15), height=40, width=250, border_width=1, border_color="red", corner_radius=3)
        name.place(x=120, y=80)
        name.focus()

        # Role field
        role = CTkEntry(left_frame,textvariable=self.role_var, font=("Bookman Old style", 15), height=40, width=250, border_width=1, border_color="red", corner_radius=3)
        role.place(x=120, y=160)

        # Gender field
        gender = CTkComboBox(left_frame,variable=self.gender_var,state="readonly", font=("Bookman Old style", 15),values=["Male", "Female"], height=40, width=250, border_width=1, border_color="red", corner_radius=3)
        gender.place(x=120, y=240)
        self.gender_var.set(value="Male")

        # Status field
        status = CTkEntry(left_frame,textvariable=self.status_var, font=("Bookman Old style", 15), height=40, width=250, border_width=1, border_color="red", corner_radius=3)
        status.place(x=120, y=320)

        # Add Employee Button
        add_employee = CTkButton(left_frame, text="Add Employee",command=self.add_employee, font=("Bookmane Old Style", 20), corner_radius=20, border_width=1,border_color="orange",text_color="white",state="ridge", width=230, height=40, fg_color="green", cursor="hand2")
        add_employee.place(x=100, y=400)

        style = ttk.Style(right_frame)
        style.theme_use("clam")
        style.configure("Treeview", font=("Bookman Old Style", 10), foreground="#fff", background="#000", fieldbackground="#313837")
        style.map("Treeview", background=[("selected", "#1A8F2D")])
        # TreeView Diagram
        self.employee_view = ttk.Treeview(right_frame,height=110, columns=["Id", "Name", "Role", "Gender", "Status"])
        self.employee_view.heading("Id", text="Id")
        self.employee_view.heading("Name", text="Name")
        self.employee_view.heading("Role", text="Role")
        self.employee_view.heading("Gender", text="Gender")
        self.employee_view.heading("Status", text="Status")
        self.employee_view["show"] = "headings"
        self.employee_view.place(x=2, y=3)

        # Treeview Settings
        self.employee_view.column("#0", width=10, stretch=NO)
        self.employee_view.column("Id", width=100)
        self.employee_view.column("Name", width=120)
        self.employee_view.column("Role", width=150)
        self.employee_view.column("Gender", width=80)
        self.employee_view.column("Status", width=120)
        self.fetch_data()

        # Bottom Button
        # New Employee Button
        new_employee = CTkButton(bottom_frame, text="New Employee", font=("Bookmane Old Style", 20), corner_radius=20, border_width=3,border_color="orange",text_color="white", width=230, height=40, fg_color="black", cursor="hand2")
        new_employee.place(x=50, y=10)

        # Update Employee Button
        update_employee = CTkButton(bottom_frame, text="Update Employee", font=("Bookmane Old Style", 20), corner_radius=20, border_width=3,border_color="orange",text_color="white", width=230, height=40, fg_color="black", cursor="hand2")
        update_employee.place(x=350, y=10)

        # Delete Employee Button
        delete_employee = CTkButton(bottom_frame, text="Delete Employee", font=("Bookmane Old Style", 20), corner_radius=20, border_width=0, width=230, height=40, fg_color="red", cursor="hand2")
        delete_employee.place(x=650, y=10)


        # ===========================================Functions Declarations ========================================================
    def add_employee(self):
        if self.id_var.get() == "":
            messagebox.showerror(title="Error", message="Please Fill Id Field!!", parent=self.root)
        elif self.name_var.get() == "":
            messagebox.showerror(title="Error", message="Please Fill Name Field!!", parent=self.root)
        elif self.role_var.get() == "":
            messagebox.showerror(title="Error", message="Please Fill Role Field!!", parent=self.root)
        elif self.gender_var.get() == "":
            messagebox.showerror(title="Error", message="Please Fill Gender Field!!", parent=self.root)
        elif self.status_var.get() == "":
            messagebox.showerror(title="Error", message="Please Fill Status Field!!", parent=self.root)
        else:
            # Connect with the database
            try:
                conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
                # print(conn)
                cur = conn.cursor()
                cur.execute("INSERT INTO loan VALUES(%s,%s,%s,%s,%s)",(
                                    self.id_var.get(),
                                    self.name_var.get(),
                                    self.role_var.get(),
                                    self.gender_var.get(),
                                    self.status_var.get()
                ))
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo(title="Success", message="Record Saved Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(title="Database Error", message=f"Error Due to: {str(es)}")

    def fetch_data(self):
            try:
                conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
                # print(conn)
                cur = conn.cursor()
                cur.execute("SELECT * FROM loan")
                data = cur.fetchall()
                if len(data) != 0:
                    self.employee_view.delete(*self.employee_view.get_children())
                    for i in data:
                        self.employee_view.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(title="Database Error", message=f"Error Due to: {str(es)}")

if __name__ == "__main__":
    root = Tk()
    Loan(root)
    root.mainloop()
