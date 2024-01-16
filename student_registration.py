import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector

# To connect with the sql database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kindergarten_system"
)

#  Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# To store the student information 
students_data = []

# Function to calculate the age by using the birth year and current year
def calculate_age(*args):
    try:
        birth_year = int(birth_year_combobox.get())
        current_year = int(entry_current_year.get())
        age = current_year - birth_year
        entry_age.config(state='normal')
        entry_age.delete(0, tk.END)
        entry_age.insert(0, str(age))
        entry_age.config(state='readonly')
    except ValueError:
        entry_age.config(state='normal')
        entry_age.delete(0, tk.END)
        entry_age.config(state='readonly')

# Function to handle the database 
def submit_registration():
    try:
        stu_id = int(entry_stu_id.get())
        stu_name = entry_stu_name.get()
        birth_year = int(birth_year_combobox.get())
        gender = gender_combobox.get()
        current_year = int(entry_current_year.get())
        age = current_year - birth_year
        class_name = class_name_combobox.get()
        parents_name = entry_parent_name.get()
        contact_num = entry_contact_num.get()

 # To insert the data into the database with 9 attributes.( 8 Attributes and 1 derived attributes which is age)
        sql = "INSERT INTO student (Stu_Id, Stu_Name, Birth_Year, Stu_Gender, Current_Year, Stu_Age, Stu_Class, Parent_Name, Contact_Num) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"
        val = (stu_id, stu_name, birth_year, gender, current_year, age, class_name, parents_name, contact_num)
        mycursor.execute(sql, val)
        mydb.commit()

# To show the data entry is successful or not. 
        if not stu_id or not stu_name or not birth_year or not current_year or not gender or not age or class_name == "Select your class" or not parents_name or not str(contact_num).isdigit() or len(str(contact_num)) != 10:
            messagebox.showerror("Error", "Please fill in all fields and enter a valid contact number.")
            return

        messagebox.showinfo("Success", "Student data submitted successfully.")
        clear_entry_fields()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values for id number, current year, and phone number.")
        return

# Function to save the student information and calculate the age
def submit_button_command():
    calculate_age()
    submit_registration()

# Function to reset or clear the data
def clear_entry_fields():
    entry_stu_id.delete(0, tk.END)
    entry_stu_name.delete(0, tk.END)
    birth_year_combobox.set("2000")
    gender_combobox.set("Select your gender")
    entry_current_year.delete(0, tk.END)
    entry_age.config(state='normal')
    entry_age.delete(0, tk.END)
    entry_age.config(state='readonly')
    class_name_combobox.set("Select your class")
    entry_parent_name.delete(0, tk.END)
    entry_contact_num.delete(0, tk.END)

# Function to update the information
def update_student():
    try:
        stu_id = int(entry_stu_id.get())
        new_class_name = class_name_combobox.get()
        new_contact_num = entry_contact_num.get()

        # Use placeholders in the SQL query for the fields that need to be updated
        sql = "UPDATE student SET Stu_Class=%s, Contact_Num=%s WHERE Stu_Id=%s"
        val = (new_class_name, new_contact_num, stu_id)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Student information updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to delete the information
def delete_student():
    try:
        stu_id = int(entry_stu_id.get())
        sql = "DELETE FROM student WHERE Stu_Id=%s"
        val = (stu_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Student data deleted successfully.")
        clear_entry_fields()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid numeric value for id number.")
        return


# For main Window 
root = tk.Tk()
root.title("Student Registration")
root.geometry('400x600')
root.configure(bg='#FFE4C4')

# Title of the page in the main window
label = tk.Label(root, text="Student Registration", font=("Sans", 14, "bold"), bg=('#FFA07A'))
label.grid(row=0, column=0, columnspan=3, pady=10, padx=15)  

# Create the ID label 
label_stu_id = tk.Label(root, text="ID", bg=('#FFA07A'))
label_stu_id.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_stu_id = tk.Entry(root)
entry_stu_id.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# To create the student name entry
label_stu_name = tk.Label(root, text="Name",bg=('#FFA07A'))
label_stu_name.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_stu_name = tk.Entry(root)
entry_stu_name.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

# To create the birth year spinbox 
label_birth_year = tk.Label(root, text="Birth Year",bg=('#FFA07A'))
label_birth_year.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
birth_year_combobox = ttk.Combobox(root, values=list(range(2000, 2023)))
spinbox_birth_year = tk.Spinbox(root, from_=2000, to=2022, textvariable=birth_year_combobox)
spinbox_birth_year.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

# To create the gender combobox 
label_gender = tk.Label(root, text="Gender",bg=('#FFA07A'))
label_gender.grid(row=4, column=0)
gender_combobox = ttk.Combobox(root, values=["Female", "Male"])
gender_combobox.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

# To create the current year entry
label_current_year = tk.Label(root, text="Today's Year",bg=('#FFA07A'))
label_current_year.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
entry_current_year = tk.Entry(root)
entry_current_year.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

# To display the age from the calculation of current year and birth year the age is a derived attributes 
label_age = tk.Label(root, text="Age", bg=('#FFA07A'))
label_age.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
entry_age = tk.Entry(root, state='readonly')
entry_age.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

# to create the class name selection
label_class_name = tk.Label(root, text="Class",bg=('#FFA07A') )
label_class_name.grid(row=7, column=0)
class_name_combobox = ttk.Combobox(root, values=["Class Alpha", "Class Beta", "Class Charlie"])
class_name_combobox.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

# To create the parent name entry
label_parent_name = tk.Label(root, text="Parent Name", bg=('#FFA07A'))
label_parent_name.grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)
entry_parent_name = tk.Entry(root)
entry_parent_name.grid(row=8, column=1, padx=10, pady=5, sticky=tk.W)

# To create the contact number entry
label_contact_num = tk.Label(root, text="Contact Number",bg=('#FFA07A'))
label_contact_num.grid(row=9, column=0, padx=10, pady=5, sticky=tk.E)
entry_contact_num = tk.Entry(root)
entry_contact_num.grid(row=9, column=1, padx=10, pady=5, sticky=tk.W)

# The button to submit the data entry into sql
submit_button = tk.Button(root, text="Submit",  bg=('#FFA07A'),command=submit_button_command)
submit_button.grid(row=10, column=0 )

# Create and place the update button
update_button = tk.Button(root, text="Update", bg=('#FFA07A'),command=update_student)
update_button.grid(row=10, column=1)

delete_button = tk.Button(root, text ="Delete", bg=('#FFA07A'), command= delete_student)
delete_button.grid(row= 10, column=2)

root.mainloop()