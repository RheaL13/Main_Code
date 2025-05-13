# All the code for the literacy area question
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

class LiteracyQuestion:
    """The code for the literacy inquiry question."""
    def __init__(self, parent):
        """Basic code for the display of the question window."""
        self.parent=parent
        self.question_window=tk.Toplevel()
        self.question_window.title("Question Window")
        self.question_window.configure(bg="oldlace")
        self.question_window.resizable(False, False)

        # Calculate center position
        w_w=600  # Window width
        w_h=320  # Window height
        screen_width=self.question_window.winfo_screenwidth()
        screen_height=self.question_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.question_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        # Headings for the different entries
        title=tk.Label(self.question_window, text="Questions", 
                       font=("Helvetica", 20, "bold"), 
                       fg="black", bg="oldlace")
        title.pack(pady=20)

        title1=tk.Label(self.question_window, text="First Name", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title1.pack(pady=2)

        self.first_name=self.create_entry("First Name")

        title2=tk.Label(self.question_window, text="Username", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title2.pack(pady=2)

        self.username=self.create_entry("Username")

        next_button=tk.Button(self.question_window, text="NEXT", width=7,
                              font=("Helvetica", 15, "bold"), 
                              height=1, fg="green", bg="white", 
                              command=self.question)
        next_button.pack(pady=20)

    def create_entry(self, placeholder, show=None):
        """Display what the entry is for."""
        entry=tk.Entry(self.question_window, show=show, 
                       font=("Helvetica", 12))
        entry.pack(pady=10)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry, 
                   p=placeholder:self.on_entry_click(event, e, p))
        entry.bind("<FocusOut>", lambda event, e=entry, 
                   p=placeholder:self.on_focusout(event, e, p))
        entry.config(fg="grey")
        return entry

    def on_entry_click(self, event, entry, placeholder):
        """Show the text they input."""
        if entry.get()==placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focusout(self, event, entry, placeholder):
        """The colour of what the entry line is for."""
        if entry.get()=="":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    def validate_fields(self):
        """Validating all the users details they input."""
        first_name=self.first_name.get().strip()
        username=self.username.get().strip()

        if (first_name=="First Name" or username=="Username"):
            mb.showwarning("Incomplete Fields", "Please fill out all "+
                           "the fields.", parent=self.question_window)
            return False

    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)


    # Saving the data if all the entries is correctly inputted
    def question(self):
        """Saving the data and telling the user that."""
        if not self.validate_fields():
            return
        
        first_name=self.first_name.get().strip()
        username=self.username.get().strip()
        
        with open(f"{username}.txt", "w") as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Username: {username}\n")

        self.parent.store_pending_user_info(first_name, username)

        mb.showinfo("Success", "Your data has been saved. Please login"+
                        " next time with your exact details. Thank you :)", 
                        parent=self.question_window)
        self.question_window.destroy()
        self.open_dashboard()


class DashboardWindow:
    """Code for the window after user had logged in."""
    def __init__(self, master):
        """Basic functionality and display for the window."""
        self.master=master
        # self.user_info=user_info
        self.dashboard_window=tk.Toplevel(master)
        self.dashboard_window.title("Dashboard")
        self.dashboard_window.configure(bg="oldlace")
        self.dashboard_window.resizable(False, False)

        # Calculate center position
        w_w=1200  # Window width
        w_h=750  # window height
        screen_width=self.dashboard_window.winfo_screenwidth()
        screen_height=self.dashboard_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.dashboard_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")


# To run the entire program (from beginning)
root=tk.Tk()
app=LiteracyQuestion(root)
root.mainloop()