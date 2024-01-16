import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kindergarten_system"
)

# Create a cursor object to interact with the database
cursor = mydb.cursor()

def subject_data():
    student_id = int(student_id_entry.get())
    student_name = student_name_entry.get()
    student_age = student_age_spinbox.get()

    selected_subjects = [subject_name[i] for i, is_selected in enumerate(subject_selected) if is_selected.get()]

    # Begin the transaction
    try:
        mydb.start_transaction()

        # Inserting data into a table for each selected subject
        for subject in selected_subjects:
            sql = "INSERT INTO subject_registration (student_id, student_name, student_age, subject_name) VALUES (%s, %s, %s, %s)"
            val = (student_id, student_name, student_age, subject)
            cursor.execute(sql, val)
            print(f"Data inserted successfully for {subject}")

        # Commit the transaction after all data is inserted
        mydb.commit()
        print("All data inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

        # Rollback the transaction in case of an error
        mydb.rollback()

    # Clear the entry fields after each insertion
    student_id_entry.delete(0, tk.END)
    student_name_entry.delete(0, tk.END)
    student_age_spinbox.delete(0, tk.END)
    for var in subject_selected:
        var.set(False)

def insert_data_in_loop():
    while True:
        subject_data()
        answer = messagebox.askquestion("Continue", "Do you want to insert data for another student?")
        if answer != 'yes':
            break

# Tkinter GUI
root = tk.Tk()
root.title("SUBJECT REGISTRATION")
root.geometry("400x600")
root.configure(bg='#C1FFC1')

# Page Title
label = tk.Label(root, text='SUBJECT REGISTRATION', font=("Sans", 14, "bold"), bg='#698B69')
label.pack(ipadx=10, ipady=15)

label_student_id = tk.Label(root, text="Student ID")
label_student_id.pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()

label_student_name = tk.Label(root, text="Student Name")
label_student_name.pack()
student_name_entry = tk.Entry(root)
student_name_entry.pack()

# Student Age
age_label = tk.Label(root, text="Student Age :")
age_label.pack(pady=10)
student_age_spinbox = tk.Spinbox(root, from_=4, to=6)
student_age_spinbox.pack()

# Subject Name with Checkbuttons
label_subject = tk.Label(root, text="Select Subjects")
label_subject.pack(pady=10)

subject_name = [
    "ART",
    "SCIENCE",
    "READING",
    "WRITING",
    "MATHEMATICS",
]

subject_selected = [tk.BooleanVar() for _ in subject_name]

for i, subject in enumerate(subject_name):
    checkbox = tk.Checkbutton(root, text=subject, variable=subject_selected[i])
    checkbox.pack(pady=3)

# Button to insert data in a loop until the user decides to stop
insert_button_loop = tk.Button(root, text="Insert Data in Loop",  bg='#9BCD9B',command=insert_data_in_loop)
insert_button_loop.pack(pady=10)


root.mainloop()