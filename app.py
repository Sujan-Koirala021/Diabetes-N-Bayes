#   Main python file to run

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk
import tkinter.font as font
import random
global label_text_color 

width = 800
height= 600
lightThemeBg = "#26242f"
darkThemeBg = "#dee4e7"

win = Tk()
win.title("Diabetes Prediction")

win.iconbitmap("imgs/appIcon.ico")


win.geometry("{}x{}".format(width, height))
win.config(bg=darkThemeBg)

lightState = PhotoImage(file="imgs/light.png")
darkState = PhotoImage(file="imgs/dark.png")

lightMode = True

result_label = None

# Get values
# Function to perform diabetes classification
def classify_diabetes():
    global result_label
    
    # Remove previous result message if exists
    if result_label:
        result_label.destroy()
    
    # Retrieve input values from Entry widgets
    pregnancies = entry_pregnancies.get()
    glucose = entry_glucose.get()
    blood_pressure = entry_blood_pressure.get()
    skin_thickness = entry_skin_thickness.get()
    insulin = entry_insulin.get()
    bmi = entry_bmi.get()
    diabetes_pedigree_function = entry_diabetes_pedigree_function.get()
    age = entry_age.get()

    # Check if any of the fields is empty
    if '' in (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # If all fields are filled, proceed with classification
    pregnancies = int(pregnancies)
    glucose = int(glucose)
    blood_pressure = int(blood_pressure)
    skin_thickness = int(skin_thickness)
    insulin = int(insulin)
    bmi = float(bmi)
    diabetes_pedigree_function = float(diabetes_pedigree_function)
    age = int(age)

    # Make changes here for classification
    # Currently predicts based on random
    random_number = random.choice([0, 1])

    # Display result message
    if random_number == 1:
        result_message = "The person is diabetic."
        result_color = "red"
    else:
        result_message = "The person is not diabetic."
        result_color = "green"

    result_label = Label(win, text=result_message, font=("Courier", 12), fg=result_color)
    result_label.place(x=width / 2, y=height - 100, anchor=CENTER)




canvas = Canvas(win, width=500, bd=0, highlightthickness=0, relief='ridge', height=350, bg=darkThemeBg)
canvas.place(x=50, y=20)
homeImg = PhotoImage(file="imgs/diabetesImg.png").subsample(4, 4)

canvas.create_image(0, 0, anchor="nw", image=homeImg)

canvas.create_text(150, 50, anchor="nw", text="Diabetes Prediction", fill="black", font=("Courier", 18))


def displayMessageBox(title, description):
    messagebox.showinfo(title, description)


# def switchMode():
#     global lightMode
#     if lightMode:
#         button.config(image=darkState, bg=lightThemeBg, activebackground=lightThemeBg)
#         canvas.config(bg=lightThemeBg)
#         win.config(bg=lightThemeBg)
#         lightMode = False
#     else:
#         button.config(image=lightState, bg=darkThemeBg, activebackground=darkThemeBg)
#         canvas.config(bg=darkThemeBg)
#         win.config(bg=darkThemeBg)
#         lightMode = True
#     label_text_color = "black" if lightMode else "white"



# button = Button(win, image=lightState, bd=0, bg=darkThemeBg, activebackground=darkThemeBg, command=switchMode)
# button.pack(padx=50, pady=50)
# button.place(x=width - 150, y=10)

# Labels setup
labels = [
    "Pregnancies:", "Glucose:", "Blood Pressure:", "Skin Thickness:",
    "Insulin:", "BMI:", "Diabetes Pedigree Function:", "Age:"
]

label_text_color = "black" if lightMode else "white"

for i, label_text in enumerate(labels):
    label = ctk.CTkLabel(win, text=label_text, font=("Helvetica", 15), text_color=label_text_color)
    label.place(x=100, y=160 + i * 40)

entry_pregnancies = ctk.CTkEntry(master=win, fg_color="white", text_color="black")
entry_glucose = ctk.CTkEntry(master=win, fg_color="white", text_color="black" )
entry_blood_pressure = ctk.CTkEntry(master=win, fg_color="white", text_color="black" )
entry_skin_thickness = ctk.CTkEntry(master=win, fg_color="white", text_color="black" )
entry_insulin = ctk.CTkEntry(master=win, fg_color="white", text_color="black")
entry_bmi = ctk.CTkEntry(master=win, fg_color="white", text_color="black" )
entry_diabetes_pedigree_function = ctk.CTkEntry(master=win, fg_color="white", text_color="black")
entry_age = ctk.CTkEntry(master=win, fg_color="white", text_color="black")

entry_pregnancies.place(x=300, y=160)
entry_glucose.place(x=300, y=200)
entry_blood_pressure.place(x=300, y=240)
entry_skin_thickness.place(x=300, y=280)
entry_insulin.place(x=300, y=320)
entry_bmi.place(x=300, y=360)
entry_diabetes_pedigree_function.place(x=300, y=400)
entry_age.place(x=300, y=440)

# Clear entries

def clear_entries():
    entry_pregnancies.delete(0, 'end')
    entry_glucose.delete(0, 'end')
    entry_blood_pressure.delete(0, 'end')
    entry_skin_thickness.delete(0, 'end')
    entry_insulin.delete(0, 'end')
    entry_bmi.delete(0, 'end')
    entry_diabetes_pedigree_function.delete(0, 'end')
    entry_age.delete(0, 'end')

clear_button = ctk.CTkButton(
    master=win,
    text="Clear Entries",
    text_color=("black", "black"),
    hover=True,
    fg_color= "#a881af",	
    hover_color="#0b6eca",
    width=100,
    height=40,
    border_width=0,
    corner_radius=0,
    font=("Courier", 12),
    command=clear_entries
)
clear_button.place(x=140, y=height - 50, anchor=CENTER)


checkDiabetesButton = ctk.CTkButton(
    master=win,
    text="Diabetes Test Result",
    text_color=("black", "black"),
    hover=True,
    fg_color= "#a881af",	
    hover_color="#0b6eca",
    width=100,
    height=40,
    border_width=0,
    corner_radius=0,
    font=("Courier", 12),
    command=classify_diabetes
)
checkDiabetesButton.place(x=width / 2, y=height - 50, anchor=CENTER)

win.mainloop()
