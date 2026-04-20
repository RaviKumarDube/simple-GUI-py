import tkinter as tk
from tkinter import messagebox
import datetime
import csv

from flask import config
app = tk.Tk()
app.title("age_calculator")
app.geometry("400x290")
app.config(bg="lightblue")
def calculate_age():

    try:
        current_year=datetime.datetime.now().year
        birth_year = int(entry.get())
        age = current_year - birth_year
        if age <0:
            messagebox.showerror("Invalid Input", "Birth year cannot be in the future.")
            return
        
        label.config(text=f"Your age is: {age}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year.")  
def save_data():
    if not entry1.get() or not entry.get():
        messagebox.showerror("Input Error", "Please fill in all fields before saving.")
        return
    name = entry1.get()
    birth_year = entry.get()
    with open('dubeverse_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, birth_year])              
label=tk.Label(app, text="Welcome to the Dubeverse collect data").pack(padx=10, pady=10)
label=tk.Label(app, text="Enter your Fullname:").pack()
entry1 =tk.Entry(app)
entry1.pack(padx=10, pady=10)  
label=tk.Label(app,text="Enter your birth year:")
label.pack()     
entry=tk.Entry(app)
entry.pack(padx=10, pady=10)     
button=tk.Button(app,text="Calculate Age",command=calculate_age)
button.pack(padx=10, pady=10)
label=tk.Label(app,text="")
label.pack()

button=tk.Button(app, text="Save Data", command=save_data, fg="white", bg="black").pack()

label=tk.Label(app, text="Created by Ravi Kumar Dube")
label.pack()
app.mainloop()

