from tkinter.ttk import *
from tkinter import *
import mysql.connector
from datetime import datetime

# MySQL Database Connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  # Update with your MySQL host
        user="root",  # Replace 'root' with your MySQL username
        password="1234",  # Replace with your MySQL password
        database="hostel_management"  # Replace with your database name
    )

# Function to get the current date and time
def date():
    now = datetime.now()
    return now.strftime("%H:%M,%Y-%m-%d")

# Initialize the main Tkinter window
base = Tk()
base.title("HOSTEL MANAGEMENT SYSTEM")
base.geometry(f'{1535}x{790}+{0}+{0}')
heading = Label(base, text="HOSTEL MANAGEMENT SYSTEM", font=("Arial 30 bold"), bg="lightseagreen", fg="white", padx=490, pady=20)
heading.pack()

# Placeholder canvas for the main menu
canvas = Canvas(base, bg='silver', height=575, width=800)
canvas.place(x=330, y=130)

# Main functionality
def main():
    # Sidebar for main menu buttons
    canvas = Canvas(base, bg='lightseagreen', height=675, width=310)
    canvas.place(x=-1, y=100)
    can = Canvas(base, bg='silver', height=675, width=1500)
    can.place(x=320, y=105)

    # Functionality for adding a student
    def add_stud():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        
        Label(base, text="Student ID", font=("Arial 15 bold"), bg='silver', fg="black").place(x=400, y=460)
        student_id_entry = Entry(base, width=15, font=("Arial 15"))
        student_id_entry.place(x=400, y=490)
        student_id_entry.focus()

        Label(base, text="First Name", font=("Arial 15 bold"), bg='silver', fg="black").place(x=400, y=180)
        fir_name_entry = Entry(base, width=15, font=("Arial 15"))
        fir_name_entry.place(x=400, y=210)

        Label(base, text="Last Name", font=("Arial 15 bold"), bg="silver", fg="black").place(x=610, y=180)
        last_name_entry = Entry(base, width=15, font=("Arial 15"))
        last_name_entry.place(x=610, y=210)

        Label(base, text="Father Name", font=("Arial 15 bold"), bg="silver", fg="black").place(x=400, y=250)
        fathr_name_entry = Entry(base, width=15, font=("Arial 15"))
        fathr_name_entry.place(x=400, y=280)

        Label(base, text="Mother Name", font=("Arial 15 bold"), bg="silver", fg="black").place(x=610, y=250)
        mther_name_entry = Entry(base, width=15, font=("Arial 15"))
        mther_name_entry.place(x=610, y=280)

        Label(base, text="DOB", font=("Arial 15 bold"), bg="silver", fg="black").place(x=400, y=320)
        dob_entry = Entry(base, width=15, font=("Arial 15 bold"))
        dob_entry.place(x=400, y=350)

        Label(base, text="Contact", font=("Arial 15 bold"), bg="silver", fg="black").place(x=610, y=320)
        cont_entry = Entry(base, width=15, font=("Arial 15 bold"))
        cont_entry.place(x=610, y=350)

        Label(base, text="Email", font=("Arial 15 bold"), bg="silver", fg="black").place(x=400, y=390)
        email_entry = Entry(base, width=15, font=("Arial 15 bold"))
        email_entry.place(x=400, y=420)

        Label(base, text="Address", font=("Arial 15 bold"), bg="silver", fg="black").place(x=610, y=390)
        addrs_entry = Entry(base, width=15, font=("Arial 15 bold"))
        addrs_entry.place(x=610, y=420)

        Label(base, text="Room No.", font=("Arial 15 bold"), bg="silver", fg="black").place(x=610, y=460)
        room_no_entry = Entry(base, width=15, font=("Arial 15 bold"))
        room_no_entry.place(x=610, y=490)

        Label(base, text="Gender", font=("Arial 15 bold"), bg="silver", fg="black").place(x=400, y=530)
        
        def selected():
            global G
            if c1.get() == 1:
                G = 1
            elif c1.get() == 2:
                G = 2
            elif c1.get() == 0:
                G = 0
            else:
                G = 1
        
        c1 = IntVar()
        Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected).place(x=490, y=530)
        Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected).place(x=580, y=530)
        Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected).place(x=680, y=530)

        def save_student():
            global G
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                data = {
                    "student_id": student_id_entry.get(),
                    "first_name": fir_name_entry.get(),
                    "last_name": last_name_entry.get(),
                    "father_name": fathr_name_entry.get(),
                    "mother_name": mther_name_entry.get(),
                    "dob": dob_entry.get(),
                    "contact": cont_entry.get(),
                    "email": email_entry.get(),
                    "address": addrs_entry.get(),
                    "room_no": room_no_entry.get(),
                    "gender": "Male" if G == 1 else ("Female" if G == 2 else "Other"),
                    "date_added": datetime.now()
                }

                query = """
                INSERT INTO students (student_id, first_name, last_name, father_name, mother_name, dob, contact, email, address, room_no, gender, date_added)
                VALUES (%(student_id)s, %(first_name)s, %(last_name)s, %(father_name)s, %(mother_name)s, %(dob)s, %(contact)s, %(email)s, %(address)s, %(room_no)s, %(gender)s, %(date_added)s)
                """
                cursor.execute(query, data)
                conn.commit()

                Label(base, text="Student added successfully!", font=("Arial 15 bold"), bg="silver", fg="green").place(x=1000, y=620)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error saving student", font=("Arial 15 bold"), bg="silver", fg="red").place(x=1000, y=620)
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

        Button(base, text="Add Student", font=("Arial 20 bold"), bg="white", command=save_student).place(x=600, y=700)

    # Functionality for adding a new room
    def add_room():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)

        Label(base, text="New Room No.", font=("Arial 20 bold"), bg="silver").place(x=500, y=300)
        room_number_entry = Entry(base, width=20, font=("Arial 15 bold"))
        room_number_entry.place(x=750, y=303)

        Label(base, text="Gender", font=("Arial 20 bold"), bg="silver").place(x=500, y=350)
        room_gender_var = IntVar(value=1)  # Default: Male
        Radiobutton(base, text="Male", variable=room_gender_var, value=1, font=("Arial 15"), bg="silver").place(x=750, y=350)
        Radiobutton(base, text="Female", variable=room_gender_var, value=2, font=("Arial 15"), bg="silver").place(x=850, y=350)
        Radiobutton(base, text="Other", variable=room_gender_var, value=0, font=("Arial 15"), bg="silver").place(x=950, y=350)

        def save_room():
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                room_data = {
                    "room_number": room_number_entry.get(),
                    "gender": "Male" if room_gender_var.get() == 1 else ("Female" if room_gender_var.get() == 2 else "Other"),
                    "date_added": datetime.now()
                }

                if not room_data["room_number"]:
                    Label(base, text="Room number is required!", font=("Arial 15 bold"), bg="silver", fg="red").place(x=600, y=500)
                    return

                query = """
                INSERT INTO rooms (room_number, gender, date_added)
                VALUES (%(room_number)s, %(gender)s, %(date_added)s)
                """
                cursor.execute(query, room_data)
                conn.commit()

                Label(base, text="Room added successfully!", font=("Arial 15 bold"), bg="silver", fg="green").place(x=600, y=500)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error saving room!", font=("Arial 15 bold"), bg="silver", fg="red").place(x=600, y=500)
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

        Button(base, text="Save Room", font=("Arial 20 bold"), bg="white", command=save_room).place(x=600, y=600)

    # Functionality for recording in and out time
    def in_out_time():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)

        Label(base, text="Enter Student ID", font=("Arial 20 bold"), bg="silver").place(x=400, y=150)
        student_id_entry = Entry(base, width=20, font=("Arial 15"))
        student_id_entry.place(x=650, y=150)

        Label(base, text="Select Action", font=("Arial 20 bold"), bg="silver").place(x=400, y=220)
        action_var = StringVar(value="IN")
        Radiobutton(base, text="IN", variable=action_var, value="IN", font=("Arial 15"), bg="silver").place(x=650, y=220)
        Radiobutton(base, text="OUT", variable=action_var, value="OUT", font=("Arial 15"), bg="silver").place(x=750, y=220)

        def record_time():
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                data = {
                    "student_id": student_id_entry.get(),
                    "action": action_var.get(),
                    "timestamp": datetime.now()
                }

                if not data["student_id"]:
                    Label(base, text="Student ID is required!", font=("Arial 15 bold"), bg="silver", fg="red").place(x=600, y=400)
                    return

                query = """
                INSERT INTO in_out_time (student_id, action, timestamp)
                VALUES (%(student_id)s, %(action)s, %(timestamp)s)
                """
                cursor.execute(query, data)
                conn.commit()

                Label(base, text="Recorded successfully!", font=("Arial 15 bold"), bg="silver", fg="green").place(x=600, y=400)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error recording time!", font=("Arial 15 bold"), bg="silver", fg="red").place(x=600, y=400)
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

        Button(base, text="Record", font=("Arial 20 bold"), bg="white", command=record_time).place(x=600, y=300)
        
    def visitor():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)

        Label(base, text="Visitor's Name", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=150)
        visitor_name_entry = Entry(base, width=20, font=("Arial 15"))
        visitor_name_entry.place(x=650, y=150)

        Label(base, text="Contact", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=220)
        visitor_contact_entry = Entry(base, width=20, font=("Arial 15"))
        visitor_contact_entry.place(x=650, y=220)

        Label(base, text="Reason", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=290)
        visitor_reason_entry = Entry(base, width=20, font=("Arial 15"))
        visitor_reason_entry.place(x=650, y=290)

        Label(base, text="Student ID", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=360)
        student_id_entry = Entry(base, width=20, font=("Arial 15"))
        student_id_entry.place(x=650, y=360)

        def save_visitor():
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                data = {
                    "visitor_name": visitor_name_entry.get(),
                    "visitor_contact": visitor_contact_entry.get(),
                    "reason": visitor_reason_entry.get(),
                    "student_id": student_id_entry.get(),
                    "date": datetime.now()
                }

                query = """
                INSERT INTO visitors (visitor_name, visitor_contact, reason, student_id, date)
                VALUES (%(visitor_name)s, %(visitor_contact)s, %(reason)s, %(student_id)s, %(date)s)
                """
                cursor.execute(query, data)
                conn.commit()

                Label(base, text="Visitor added successfully!", font=("Arial 15 bold"), bg="silver", fg="green").place(x=1000, y=500)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error saving visitor", font=("Arial 15 bold"), bg="silver", fg="red").place(x=1000, y=500)
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

        Button(base, text="Add Visitor", font=("Arial 20 bold"), bg="white", command=save_visitor).place(x=650, y=450)

    def view_info():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)

        Label(base, text="Room No.", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=150)
        room_no_entry = Entry(base, width=20, font=("Arial 15"))
        room_no_entry.place(x=650, y=150)

        def search_students():
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                room_no = room_no_entry.get()

                query = "SELECT first_name, last_name, contact FROM students WHERE room_no = %s"
                cursor.execute(query, (room_no,))
                results = cursor.fetchall()

                Label(base, text="Name", font=("Arial 15 bold"), bg="silver", fg="black").place(x=400, y=350)
                Label(base, text="Contact", font=("Arial 15 bold"), bg="silver", fg="black").place(x=600, y=350)

                y_pos = 400
                for row in results:
                    Label(base, text=f"{row[0]} {row[1]}", font=("Arial 12"), bg="silver", fg="black").place(x=400, y=y_pos)
                    Label(base, text=row[2], font=("Arial 12"), bg="silver", fg="black").place(x=600, y=y_pos)
                    
                    y_pos += 50

            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error fetching information", font=("Arial 15 bold"), bg="silver", fg="red").place(x=1000, y=500)
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

        Button(base, text="Search", font=("Arial 20 bold"), bg="white", command=search_students).place(x=650, y=220)

    def leave_application():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)

        Label(base, text="Student ID", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=150)
        student_id_entry = Entry(base, width=20, font=("Arial 15"))
        student_id_entry.place(x=650, y=150)

        Label(base, text="Reason", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=220)
        leave_reason_entry = Entry(base, width=20, font=("Arial 15"))
        leave_reason_entry.place(x=650, y=220)

        Label(base, text="Return Date", font=("Arial 20 bold"), bg="silver", fg="black").place(x=400, y=290)
        return_date_entry = Entry(base, width=20, font=("Arial 15"))
        return_date_entry.place(x=650, y=290)

        def save_leave():
            try:
                conn = connect_to_db()
                cursor = conn.cursor()

                data = {
                    "student_id": student_id_entry.get(),
                    "reason": leave_reason_entry.get(),
                    "return_date": return_date_entry.get(),
                    "date_added": datetime.now()
                }

                query = """
                INSERT INTO leave_applications (student_id, reason, return_date, date_added)
                VALUES (%(student_id)s, %(reason)s, %(return_date)s, %(date_added)s)
                """
                cursor.execute(query, data)
                conn.commit()

                Label(base, text="Leave application submitted!", font=("Arial 15 bold"), bg="silver", fg="green").place(x=1000, y=500)
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                Label(base, text="Error saving leave application", font=("Arial 15 bold"), bg="silver", fg="red").place(x=1000, y=500)
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

        Button(base, text="Submit", font=("Arial 20 bold"), bg="white", command=save_leave).place(x=650, y=360)

    # Buttons in the main menu
    Button(base, text="Add Student", font=("Arial 20 bold"), padx=15, bg="white", command=add_stud).place(x=50, y=150)
    Button(base, text="Add New Room", font=("Arial 20 bold"), bg="white", command=add_room).place(x=50, y=250)
    Button(base, text="In And Out Time", font=("Arial 20 bold"), bg="white", command=in_out_time).place(x=50, y=350)
    Button(base, text="Visitor", font=("Arial 20 bold"), bg="white", padx=55, command=visitor).place(x=50, y=450)
    Button(base, text="View Information", font=("Arial 18 bold"), bg="white", command=view_info).place(x=50, y=535)
    Button(base, text="Leave Application", font=("Arial 18 bold"), bg="white", command=leave_application).place(x=50, y=620)
    Button(base, text="EXIT", font=("Arial 18 bold"), bg="white", padx=70, command=quit).place(x=50, y=700)

# Login functionality
def login():
    id = user_entry.get()
    key = pass_entry.get()
    if id == "Prasad" and key == "123":
        main()
    else:
        user_entry.focus()
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        Label(base, text="Wrong Username Or Password...!", font=("Arial 30 bold"), bg="silver", fg="red").place(x=450, y=540)

# Login Page
Label(base, text="Username", font=("Arial 25 bold"), bg="silver", fg="black").place(x=470, y=240)
user_entry = Entry(base, width=17, font=("Arial 20"))
user_entry.place(x=650, y=245)
user_entry.focus()

Label(base, text="Password", font=("Arial 25 bold"), bg="silver", fg="black").place(x=470, y=350)
pass_entry = Entry(base, width=17, font="Arial 20", show='*')
pass_entry.place(x=650, y=355)

Button(base, text="Login", font=("Arial 25 bold"), bg="lightseagreen", fg="white", command=login).place(x=650, y=440)

base.mainloop()
