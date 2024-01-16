import tkinter 
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kindergarten_system"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

number_of_subject = 100

def calculate_net_salary(number_of_subject, monthly_teaching_day, kwsp, socso, income_tax, other):
    # Calculate gross salary
    gross_salary = (number_of_subject * 100) * monthly_teaching_day
    # Calculate net salary
    net_salary = gross_salary - kwsp - socso - income_tax - other
    return gross_salary, net_salary

def save_information():
    # Get the information
    number_of_subject = int(number_of_subject_combobox.get())
    monthly_teaching_day = int(monthly_teaching_day_combobox.get())
    kwsp = float(kwsp_entry.get())
    socso = float(socso_entry.get())
    income_tax = float(tax_entry.get())
    other = float(other_entry.get())

    if not number_of_subject or not monthly_teaching_day or not kwsp or not socso or not income_tax:
        # Display an error message 
        messagebox.showerror("Error", "Please fill in all the required fields")
        return
    
    else: 
        # Calculate the gross salary and net salary
        gross_salary, net_salary = calculate_net_salary(number_of_subject, monthly_teaching_day, kwsp, socso, income_tax, other)

        # Display the results
        gross_salary_output_label.config(text=f"Your Gross Salary(RM): {gross_salary:.2f}")
        net_salary_output_label.config(text=f"Your Net Salary(RM): {net_salary:.2f}")

        # Display a success message
        messagebox.showinfo("Success", "Your information saved successfully. Gross and Net Salary calculated.")

        # To insert your data into your database
        sql = "INSERT INTO teacher_calculator (number_of_subject, monthly_teaching_day, gross_salary, kwsp_contributions, socso, income_tax, other_pay, net_salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (number_of_subject, monthly_teaching_day, gross_salary, kwsp, socso, income_tax, other, net_salary)
        mycursor.execute(sql, val)
        mydb.commit()

def update_information():
    # Get the information
    number_of_subject = int(number_of_subject_combobox.get())
    monthly_teaching_day = int(monthly_teaching_day_combobox.get())
    kwsp = float(kwsp_entry.get())
    socso = float(socso_entry.get())
    income_tax = float(tax_entry.get())
    other = float(other_entry.get())

    if not number_of_subject or not monthly_teaching_day or not kwsp or not socso or not income_tax:
        # Display an error message 
        messagebox.showerror("Error", "Please fill in all the required fields")
        return
    
    
    else: 
        # Calculate the gross salary and net salary
        gross_salary, net_salary = calculate_net_salary(number_of_subject, monthly_teaching_day, kwsp, socso, income_tax, other)

        # Display the results
        gross_salary_output_label.config(text=f"Your Gross Salary(RM): {gross_salary:.2f}")
        net_salary_output_label.config(text=f"Your Net Salary(RM): {net_salary:.2f}")

        # Display a success message
        messagebox.showinfo("Success", "Your information updated successfully and have recalculated.")

        # Update the data in your database
        sql = "UPDATE teacher_calculator SET gross_salary = %s, kwsp_contributions = %s, socso = %s, income_tax = %s, other_pay = %s, net_salary = %s WHERE number_of_subject = %s AND monthly_teaching_day = %s"
        val = (gross_salary, kwsp, socso, income_tax, other, net_salary, number_of_subject, monthly_teaching_day)
        mycursor.execute(sql, val)
        mydb.commit()

def delete_information():
    # Get the information
    number_of_subject = int(number_of_subject_combobox.get())
    monthly_teaching_day = int(monthly_teaching_day_combobox.get())

    if not number_of_subject or not monthly_teaching_day:
        # Display an error message 
        messagebox.showerror("Error", "Please select the number of subjects and monthly teaching day")
        return
    
    else: 
        # Display a success message
        messagebox.showinfo("Success", "Your information deleted successfully.")

        # Delete the data from your database
        sql = "DELETE FROM teacher_calculator WHERE number_of_subject = %s AND monthly_teaching_day = %s"
        val = (number_of_subject, monthly_teaching_day)
        mycursor.execute(sql, val)
        mydb.commit()

# Create the main root
root = tkinter.Tk()
root.title("Teacher Salary Calculator")
root.geometry("400x600")
root.configure(bg='#BFEFFF')


teacher_gross_salary_calculator_frame = tkinter.LabelFrame(root, text="Calculate Your Gross Salary Here!", bg='#8EE5EE')
teacher_gross_salary_calculator_frame.grid(padx=30, pady=20)

number_of_subject_label = tkinter.Label(teacher_gross_salary_calculator_frame, text="Number of Teaching Subject")
number_of_subject_combobox = ttk.Combobox(teacher_gross_salary_calculator_frame, values=[1, 2, 3])
number_of_subject_label.grid(row=0, column=0)
number_of_subject_combobox.grid(row=0, column=1)

monthly_teaching_day_label = tkinter.Label(teacher_gross_salary_calculator_frame, text="Monthly Teaching Day")
monthly_teaching_day_combobox = ttk.Combobox(teacher_gross_salary_calculator_frame, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
monthly_teaching_day_label.grid(row=1, column=0)
monthly_teaching_day_combobox.grid(row=1, column=1)

gross_salary_label = tkinter.Label(root, text="Your Gross Salary(RM):")
gross_salary_label.grid(row=4, column=0)
gross_salary_output_label = ttk.Label(root, text="")
gross_salary_output_label.grid()

for widget in teacher_gross_salary_calculator_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

teacher_net_salary_calculator_frame = tkinter.LabelFrame(root, text="Calculate Your Net Salary Here!", bg='#8EE5EE')
teacher_net_salary_calculator_frame.grid(padx=30, pady=20)

kwsp_label = tkinter.Label(teacher_net_salary_calculator_frame, text="KWSP Contributions (%):")
kwsp_label.grid(row=3, column=0)
kwsp_entry = ttk.Entry(teacher_net_salary_calculator_frame, width=20)
kwsp_entry.grid(row=3, column=1)

socso_label = tkinter.Label(teacher_net_salary_calculator_frame, text= "SOCSO (%):")
socso_label.grid(row=4, column=0)
socso_entry = ttk.Entry(teacher_net_salary_calculator_frame, width=20 )
socso_entry.grid(row=4, column=1)

tax_label = tkinter.Label(teacher_net_salary_calculator_frame, text= "Income Tax (%):")
tax_label.grid(row=5, column=0)
tax_entry = ttk.Entry(teacher_net_salary_calculator_frame, width=20 )
tax_entry.grid(row=5, column=1)

other_label = tkinter.Label(teacher_net_salary_calculator_frame, text= "Other Pay (RM):")
other_label.grid(row=6, column=0)
other_entry = ttk.Entry(teacher_net_salary_calculator_frame, width=20 )
other_entry.grid(row=6, column=1)

net_salary_label = tkinter.Label(root, text="Your Net Salary(RM):")
net_salary_label.grid(row=8, column=0)
net_salary_output_label = ttk.Label(root, text="")
net_salary_output_label.grid()

for widget in teacher_net_salary_calculator_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

save_button = ttk.Button(root, text="Save Information & Calculate Salary", command=save_information,)
save_button.grid()

update_button = ttk.Button(root, text="Update Information" ,command=update_information)
update_button.grid()

delete_button = ttk.Button(root, text="Delete Information",  command=delete_information)
delete_button.grid()

root.mainloop()