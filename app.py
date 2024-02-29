#   Main python file to run

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
import tkinter.font as font


width = 800
height= 600
lightThemeBg = "#26242f"
darkThemeBg = "#dee4e7"

win = Tk()
win.title("Diabetes Prediction")

# if 'posix' == os.name:
#     img = PhotoImage(file="imgs/appIcon.png")
#     win.iconphoto(True,img)
# else:
#     win.iconbitmap("imgs/appIcon.png")

win.iconbitmap("imgs/appIcon.ico")


#   Set window size

win.geometry("{}x{}".format(width, height)) # same as win.geometry("600x400")
win.config(bg = darkThemeBg)

#   Load images
lightState = PhotoImage(file="imgs/light.png")
darkState = PhotoImage(file="imgs/dark.png")



lightMode = True

#   Canvas that displays home image
canvas = Canvas(win, width=500,bd=0, highlightthickness=0, relief='ridge', height=350, bg = darkThemeBg)
canvas.place(x = 50,y =  20)
homeImg = PhotoImage(file="imgs/diabetesImg.png").subsample(4, 4)


# Create the image on the canvas without a box-like background
canvas.create_image(0, 0, anchor="nw", image=homeImg)

# Insert text beside the image
canvas.create_text(150, 50, anchor="nw", text="Diabetes Prediction", fill="black", font=("Courier", 18))



#   Display success message 
def displayMessageBox(title, description):
    messagebox.showinfo(title, description)    #   Show success message box

#   Switch mode on pressing light or dark button
def switchMode():
    global lightMode
    if lightMode:
        button.config(image = darkState, bg = lightThemeBg, activebackground=lightThemeBg)
        canvas.config(bg = lightThemeBg)

        win.config(bg = lightThemeBg)
        lightMode = False
    else:
        button.config(image = lightState, bg = darkThemeBg, activebackground=darkThemeBg)
        canvas.config(bg = darkThemeBg)

        win.config(bg = darkThemeBg)
        lightMode = True


#   Place theme button with light theme default
button = Button(win, image=lightState, bd = 0, bg = darkThemeBg, activebackground=darkThemeBg, command = switchMode)
button.pack(padx=50, pady = 50)
button.place(x = width - 150, y = 10)


# Use CTkButton instead of tkinter Button for compress and extract button
# compressButton = customtkinter.CTkButton(master=win, text_color=("black", "black"), text="Compress file",hover=True, hover_color="#0b6eca", width=170,height=50,border_width=0,corner_radius=0,font=("Courier", 12), command={})
# compressButton.place(x = 3*width/4 , y =height/2 - 30, anchor=CENTER)

# checkDiabetesButton = Button(win, text = "Extract File", command = openFileDialogForExtraction)
# checkDiabetesButton.place(x = 3*width/4 , y =height/2 + 50)


# Use CTkButton instead of tkinter Button
checkDiabetesButton = customtkinter.CTkButton(master=win, text="Diabetes Test Result",text_color=("black", "black"),hover=True, hover_color="#0b6eca", width=100,height=40,border_width=0,corner_radius=0,font=("Courier", 12), command={})
checkDiabetesButton.place(x = 1*width/2 , y =height- 50, anchor=CENTER)

win.mainloop()