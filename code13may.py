# Importing all the modules for the program
"""Provides functions for creating and removing a directory / folder."""
import os
"""Allows intergers / values to be manipulated randomly."""
import random
"""For using regular expressions."""
import re
"""The ability to open websites on web browser."""
import webbrowser
"""Allows the current date and time to be imported."""
from datetime import datetime

"""Imports tkinter library."""
import tkinter as tk
"""Allows access to the Tk themed widget set."""
from tkinter import ttk
"""Holds integer data where we can set integer data and can retrieve it"""
from tkinter import IntVar
"""Importing the tkinter text style."""
from tkinter import Text
"""Allowing the text to be inserted in a canvas."""
from tkinter import INSERT
"""Import the specific font style from the tkinter library."""
from tkinter import font
"""Allows the tkinter style of message box that pops up."""
from tkinter import messagebox as mb
"""Imports the tkinter style of image that are saved to display and modify."""
from PIL import Image
"""Imports the tkinter style of image that are saved to display and modify.."""
from PIL import ImageTk

# Data of questions and answers and options
# ...

# The Main Window (the first one users will see)
class MainWindow:
    """Main window code."""
    def __init__(self, master):
        """Basic code for the display of the window."""
        self.master=master
        self.master.title("EcoSmart")
        self.master.configure(bg="oldlace")
        self.master.resizable(False, False)

        # Calculate center position
        w_w=1200
        w_h=750
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()

        x_position=(screen_width-w_w)//2
        y_position=(screen_height-w_h)//4

        # Set window geometry
        self.master.geometry(f"{w_w}x{w_h}+{x_position}+{y_position}")

        self.firstwindow=tk.Frame(self.master, bg="oldlace")
        self.firstwindow.pack(fill="both", expand=True)

        # Title and headings of the window
        label=tk.Label(self.firstwindow, 
                       text="EcoSmart\nOverconsumption Quiz", 
                       font=("Helvetica", 28, "bold"), 
                       fg="green", bg="oldlace")
        label.pack(pady=40)

        description=tk.Label(self.firstwindow, text="Welcome!\nThis "+
                             "program is to teach and test you on "+
                             "your knowledge about \nover-consumption. "+
                             "If you are new here, please sign up, "+
                             "otherwise login.",font=("Helvetica", 15), 
                             fg="green", bg="oldlace")
        description.place(x=290, y=140)

        # Buttons on the window, that do different things
        signup_button=tk.Button(self.firstwindow, text="SIGN UP", width=10, 
                                height=2, fg="green", bg="white",
                                font=("Helvetica", 10, "bold"),
                                command=self.signup)
        signup_button.place(x=1090, y=50)

        login_button=tk.Button(self.firstwindow, text="LOGIN", width=10, 
                               height=2, fg="green", bg="white",
                               font=("Helvetica", 10, "bold"),
                               command=self.login)
        login_button.place(x=985, y=50)

        exit_button=tk.Button(self.firstwindow, text='EXIT', width=10, 
                              height=2, fg="black", bg="white", 
                              font=("Helvetica", 10, "bold"),
                              command=self.check_exit)
        exit_button.place(x=1090, y=685)

        # ADD A PICTURE FOR THE FRONT (or something to fill in the space)

    # The other buttons on the window (sidebar) and will always be there
    def create_sidebar(self):
        """The buttons on the side of the window (will always be there)."""
        buttons=[
            ("HOME", self.open_popup),
            ("USER\nMANUAL", self.open_popup),
            ("QUIZ", self.open_popup),
            ("LEARN", self.open_popup),
            ("ALTERNATIVE\nPRODUCTS", self.open_popup),
            ("ABOUT", self.open_popup),
            ("HELP", self.open_popup)
        ]

        for i, (text, command) in enumerate(buttons):
            btn=tk.Button(self.master, text=text, width=11, height=2,
                            font=("Helvetica", 10, "bold"), fg="green", 
                            bg="white", command=command)
            btn.place(x=50, y=50+i*100)

    def check_exit(self):
        """Ask if they want to exit (verify)."""
        result=mb.askquestion("Exit", "Are you sure you want to exit"+
                              " the program now?")
        if result=="yes":
            self.master.destroy()

    def open_popup(self):
        """Tell user to sign in / login first if side bar buttons are 
        clicked.
        """
        mb.showwarning("Warning", "Please login or sign up first please.")

    # Open the different windows when the specific button is clicked
    def signup(self):
        """Open sign up window."""
        self.signup_window=SignUpWindow(self)
    
    def login(self):
        """Open login window."""
        self.login_window=LoginWindow(self)

    # This function stores all the users info. Will be called everywhere
    def store_pending_user_info(self, first_name, username, password, 
                                date_of_birth):
        """Storing users details."""
        self.pending_user_info={
            "username":username,
            "password":password,
            "first_name":first_name,
            "date_of_birth":date_of_birth
        }
        self.user_info=self.pending_user_info


# All the code for the sign up window
class SignUpWindow:
    """Code for sign up window."""
    def __init__(self, parent):
        """Basic code for the display of the sign up window."""
        self.parent=parent
        self.signup_window=tk.Toplevel()
        self.signup_window.title("Signup Window")
        self.signup_window.configure(bg="oldlace")
        self.signup_window.resizable(False, False)

        # Calculate center position
        w_w=600  # Window width
        w_h=550  # Window height
        screen_width=self.signup_window.winfo_screenwidth()
        screen_height=self.signup_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.signup_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

# All the code for the login window
class LoginWindow:
    """The code for the login window."""
    def __init__(self, parent):
        """The basic code for the main display of the login window."""
        self.parent=parent
        self.login_window=tk.Toplevel()
        self.login_window.title("Login Window")
        self.login_window.configure(bg="oldlace")
        self.login_window.resizable(False, False)

        # Calculate center position
        w_w=600  # Window width
        w_h=320  # window height
        screen_width=self.login_window.winfo_screenwidth()
        screen_height=self.login_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.login_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")


# To run the entire program (from beginning)
root=tk.Tk()
app=MainWindow(root)
root.mainloop()