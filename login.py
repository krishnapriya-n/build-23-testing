### Dummy code that does nothing yet, tiny login page box

import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import partial

def validate_login(username, password):
    print("Username entered : ", username.get())
    print("Password entered : ", password.get())
    return

# UI window
tkWindow = Tk()
tkWindow.geometry('200x150')
tkWindow.title('AICrop')

# Username label and text entry box
username_label = Label(tkWindow, text="Username").grid(row=0, column=0)
username = StringVar()
username_entry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# Password label and text entry box
password_label = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
password_emtry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

# Login button
login_button = Button(tkWindow, text="Login", command=validate_login).grid(row=4, column=0)

# Mainloop for login
tkWindow.mainloop()
