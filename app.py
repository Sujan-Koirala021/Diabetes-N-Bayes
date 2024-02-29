#   Main python file to run

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter as ctk
import tkinter.font as font


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

canvas = Canvas(win, width=500, bd=0, highlightthickness=0, relief='ridge', height=350, bg=darkThemeBg)
canvas.place(x=50, y=20)
homeImg = PhotoImage(file="imgs/diabetesImg.png").subsample(4, 4)

canvas.create_image(0, 0, anchor="nw", image=homeImg)

canvas.create_text(150, 50, anchor="nw", text="Diabetes Prediction", fill="black", font=("Courier", 18))


def displayMessageBox(title, description):
    messagebox.showinfo(title, description)


def switchMode():
    global lightMode
    if lightMode:
        button.config(image=darkState, bg=lightThemeBg, activebackground=lightThemeBg)
        canvas.config(bg=lightThemeBg)
        win.config(bg=lightThemeBg)
        lightMode = False
    else:
        button.config(image=lightState, bg=darkThemeBg, activebackground=darkThemeBg)
        canvas.config(bg=darkThemeBg)
        win.config(bg=darkThemeBg)
        lightMode = True


button = Button(win, image=lightState, bd=0, bg=darkThemeBg, activebackground=darkThemeBg, command=switchMode)
button.pack(padx=50, pady=50)
button.place(x=width - 150, y=10)


# Labels setup
labels = [
    "Pregnancies:", "Glucose:", "Blood Pressure:", "Skin Thickness:",
    "Insulin:", "BMI:", "Diabetes Pedigree Function:", "Age:"
]

for i, label_text in enumerate(labels):
    label = ctk.CTkLabel(win, text=label_text, font=("Helvetica", 15))
    label.place(x=100, y=200 + i * 40)


entry_pregnancies = ctk.CTkEntry(master=win)
entry_glucose = ctk.CTkEntry(master=win )
entry_blood_pressure = ctk.CTkEntry(master=win )
entry_skin_thickness = ctk.CTkEntry(master=win )
entry_insulin = ctk.CTkEntry(master=win)
entry_bmi = ctk.CTkEntry(master=win )
entry_diabetes_pedigree_function = ctk.CTkEntry(master=win)
entry_age = ctk.CTkEntry(master=win)

entry_pregnancies.place(x=300, y=200)
entry_glucose.place(x=300, y=240)
entry_blood_pressure.place(x=300, y=280)
entry_skin_thickness.place(x=300, y=320)
entry_insulin.place(x=300, y=360)
entry_bmi.place(x=300, y=400)
entry_diabetes_pedigree_function.place(x=300, y=440)
entry_age.place(x=300, y=480)

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
    hover_color="#0b6eca",
    width=100,
    height=40,
    border_width=0,
    corner_radius=0,
    font=("Courier", 12),
    command={}
)
checkDiabetesButton.place(x=width / 2, y=height - 50, anchor=CENTER)

win.mainloop()
