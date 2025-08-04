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
"""import json to use json file for data"""
import json

import tkinter.simpledialog as sd

from tkinter import messagebox
from PIL import Image, ImageTk



# The Main Window (the first one users will see)
class MainWindow:
    """Main window code."""
    def __init__(self, master):
        """Basic code for the display of the window."""
        self.master=master
        self.master.title("Page By Page")
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
                       text="Page By Page\nLiteracy Quiz", 
                       font=("Helvetica", 28, "bold"), 
                       fg="lightseagreen", bg="oldlace")
        label.pack(pady=40)

        description=tk.Label(self.firstwindow, text="Welcome!\nThis "+
                             "program is to teach and test you on "+
                             "your knowledge on \nyour literacy skills "+
                             "(spelling, grammar, and vocabulary). "+
                             "\nIf you are new here, please sign up, "+
                             "otherwise login.",font=("Helvetica", 15), 
                             fg="lightseagreen", bg="oldlace")
        description.place(x=330, y=140)

        # Buttons on the window, that do different things
        signup_button=tk.Button(self.firstwindow, text="SIGN UP", width=10, 
                                height=2, fg="lightseagreen", bg="white",
                                font=("Helvetica", 10, "bold"),
                                command=self.signup)

        login_button=tk.Button(self.firstwindow, text="LOGIN", width=10, 
                               height=2, fg="lightseagreen", bg="white",
                               font=("Helvetica", 10, "bold"),
                               command=self.login)

        exit_button=tk.Button(self.firstwindow, text='EXIT', width=10, 
                              height=2, fg="black", bg="white", 
                              font=("Helvetica", 10, "bold"),
                              command=self.check_exit)
        
        signup_button.place(x=1090, y=50)
        login_button.place(x=985, y=50)
        exit_button.place(x=1090, y=685)

        # Code to add a picture to the window
        # Read the Image
        image=Image.open("imagehome.jpg")

        # Resize the image using resize() method
        resize_image=image.resize((800, 400))

        img=ImageTk.PhotoImage(resize_image)

        # Create a label and add resize image
        label1=tk.Label(image=img)
        label1.image=img
        label1.place(x=200, y=270)

        self.pending_user_info={}
        self.create_sidebar()

    # The other buttons on the window (sidebar) and will always be there
    def create_sidebar(self):
        """The buttons on the side of the window (will always be there)."""
        buttons=[
            ("HOME", self.open_popup),
            ("USER\nMANUAL", self.open_popup),
            ("QUIZ", self.open_popup),
            ("LEARN", self.open_popup),
            ("ABOUT", self.open_popup),
            ("HELP", self.open_popup)
        ]

        for i, (text, command) in enumerate(buttons):
            btn=tk.Button(self.master, text=text, width=11, height=2,
                            font=("Helvetica", 10, "bold"), fg="lightseagreen", 
                            bg="white", command=command)
            btn.place(x=50, y=50+i*100)

    def open_popup(self):
        """Tell user to sign in / login first if side bar buttons are 
        clicked.
        """
        mb.showwarning("Warning", "Please login or sign up first.")

    def check_exit(self):
        """Ask if they want to exit (verify)."""
        result=mb.askquestion("Exit", "Are you sure you want to exit"+
                              " the program now?")
        if result=="yes":
            self.master.destroy()

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

    def open_dashboard(self):
        """This method will open the Dashboard window when called."""
        self.dashboard_window = DashboardWindow(self.master, self.pending_user_info)


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

        # Headings for the different entries
        title=tk.Label(self.login_window, text="Login", 
                       font=("Helvetica", 20, "bold"), 
                       fg="black", bg="oldlace")
        title.pack(pady=20)

        title1=tk.Label(self.login_window, text="Username", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title1.pack(pady=2)

        self.username=self.create_entry("Username")

        title2=tk.Label(self.login_window, text="Password", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title2.pack(pady=2)
        
        self.password=self.create_entry("Password", show="*")

        next_button=tk.Button(self.login_window, text="NEXT", width=7, 
                              height=1, fg="lightseagreen", bg="white", 
                              font=("Helvetica", 15, "bold"),
                              command=self.login)
        next_button.pack(pady=20)

        # Button that changes between the sign up and login windows
        def change():
            """Change between the sign up and login windows, when button 
            clicked.
            """
            SignUpWindow(self.parent)
            self.login_window.destroy()

        signup_change_button=tk.Button(self.login_window, text="SIGN UP", 
                                       font=("Helvetica", 15, "bold"), 
                                       width=7, height=1, fg="lightseagreen", 
                                       bg="white", command=change)
        signup_change_button.place(x=480, y=20)

        back_button=tk.Button(self.login_window, text="EXIT", 
                              font=("Helvetica", 15, "bold"), width=7, 
                              height=1, fg="black", bg="white", 
                              command=self.login_window.destroy)
        back_button.place(x=480, y=260)

    def create_entry(self, placeholder, show=None):
        """Display what the entry is for."""
        entry=tk.Entry(self.login_window, show=show, 
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

    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)

    # Validating all the entry fields (data collected from user)
    def validate_login(self, username, password):
        """Validating all the users details they input."""
        if os.path.exists(f"{username}.txt"):
            with open(f"{username}.txt", "r") as file:
                lines=file.readlines()
                stored_username=lines[3].split(": ")[1].strip()
                stored_password=lines[4].split(": ")[1].strip()
                if username==stored_username and password==stored_password:
                    self.parent.store_pending_user_info(
                        first_name=lines[1].split(": ")[1].strip(),
                        username=stored_username,
                        password=stored_password,
                        date_of_birth=lines[2].split(": ")[1].strip()
                    )
                    return True
        return False

    # Saving the data if all the entries is correctly inputted
    def login(self):
        """Saving the data and telling the user that."""
        username=self.username.get()
        password=self.password.get()

        if self.validate_login(username, password):
            self.login_window.destroy()
            self.open_dashboard()
        else:
            mb.showwarning("Error", "Invalid credentials, please fill out all the fields", 
                           parent=self.login_window)


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

        # Headings for the different entries
        title=tk.Label(self.signup_window, text="Sign Up", 
                       font=("Helvetica", 20, "bold"), 
                       fg="black", bg="oldlace")
        title.pack(pady=20)

        title1=tk.Label(self.signup_window, text="First Name", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title1.pack(pady=2)

        self.first_name=self.create_entry("First Name")

        title2=tk.Label(self.signup_window, text="Username", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title2.pack(pady=2)

        self.username=self.create_entry("Username")

        title3=tk.Label(self.signup_window, text="Password", 
                        font=("Helvetica", 13, "bold"), 
                        fg="black", bg="oldlace")
        title3.pack(pady=2)

        self.password=self.create_entry("Password", show="*")

        title4=tk.Label(self.signup_window, text="Confirm Password", 
                        font=("Helvetica", 13, "bold"), fg="black", 
                        bg="oldlace")
        title4.pack(pady=2)

        self.confirm_password=self.create_entry("Password", show="*")

        title5=tk.Label(self.signup_window, 
                        text="Date of Birth (DD/MM/YYYY)", 
                        font=("Helvetica", 13, "bold"), fg="black", 
                        bg="oldlace")
        title5.pack(pady=2)

        self.date_of_birth=self.create_entry("(DD/MM/YYYY)")

        next_button=tk.Button(self.signup_window, text="NEXT", width=7,
                              font=("Helvetica", 15, "bold"), 
                              height=1, fg="lightseagreen", bg="white", 
                              command=self.signup)
        next_button.pack(pady=20)

        # Button that changes between the sign up and login windows
        def change2():
            """Changing between the sign up and login window."""
            LoginWindow(parent)
            self.signup_window.destroy()

        login_change_button=tk.Button(self.signup_window, text="LOGIN", 
                                      font=("Helvetica", 15, "bold"),
                                      width=7, height=1, fg="lightseagreen", 
                                      bg="white", command=change2)
        login_change_button.place(x=480, y=20)

        back_button=tk.Button(self.signup_window, text="EXIT", width=7,
                              font=("Helvetica", 15, "bold"),
                              height=1, fg="black", bg="white", 
                              command=self.signup_window.destroy)
        back_button.place(x=480, y=485)

    def create_entry(self, placeholder, show=None):
        """Display what the entry is for."""
        entry=tk.Entry(self.signup_window, show=show, 
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

    def validate_date_of_birth(self, date_of_birth):
        """Validate the birthdate with the current time and date."""
        try:
            birthdate=datetime.strptime(date_of_birth, "%d/%m/%Y")
            return birthdate
        except ValueError:
            return None

    # Validating all the entry fields (data collected from user)
    def validate_fields(self):
        """Validating all the users details they input."""
        first_name = self.first_name.get().strip()
        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm_password = self.confirm_password.get().strip()
        date_of_birth = self.date_of_birth.get().strip()

        # Check for placeholders (unfilled inputs)
        if (first_name == "First Name" or username == "Username" or 
            password == "Password" or confirm_password == "Confirm Password" or 
            date_of_birth == "Date of Birth (DD/MM/YYYY)" or
            not first_name or not username or not password or not confirm_password or not date_of_birth):
            mb.showwarning("Incomplete Fields", "Please fill out all the fields.",
                        parent=self.signup_window)
            return False

        # Length limits
        if len(first_name) > 10 or len(username) > 10 or len(password) > 10:
            mb.showwarning("Invalid Input", "First name, username, and password must be 10 characters or less.", 
                        parent=self.signup_window)
            return False

        # Only letters in first name
        if not first_name.isalpha():
            mb.showwarning("Invalid First Name", "First name can only contain letters.",
                        parent=self.signup_window)
            return False

        # Username: letters and numbers only
        if not re.match("^[A-Za-z0-9]+$", username):
            mb.showwarning("Invalid Username", "Username can only contain letters and numbers (no spaces).",
                        parent=self.signup_window)
            return False

        # Passwords match
        if password != confirm_password:
            mb.showerror("Error", "Passwords do not match.", parent=self.signup_window)
            return False

        # Validate date format and calculate age
        birthdate = self.validate_date_of_birth(date_of_birth)
        if not birthdate:
            mb.showerror("Invalid Date Of Birth", "Please enter a valid date of birth using format DD/MM/YYYY.",
                        parent=self.signup_window)
            return False

        age = (datetime.today() - birthdate).days // 365
        if age < 0 or age > 90:
            mb.showerror("Invalid Date Of Birth", "Please enter a realistic date of birth (age must be between 0-90).",
                        parent=self.signup_window)
            return False

        # Age warning if outside 5–15 range
        if age < 5 or age > 15:
            age_maybe = mb.askquestion("Age Notice", f"Your age is {age}. This program is designed for ages 5-15. Continue anyway?",
                                    parent=self.signup_window)
            if age_maybe.lower() != "yes":
                return False

        print(age)  # Optional debug
        return True
    
    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)
    
    # Saving the data if all the entries is correctly inputted
    def signup(self):
        """Saving the data and telling the user that."""
        if not self.validate_fields():
            return

        first_name=self.first_name.get().strip()
        username=self.username.get().strip()
        password=self.password.get().strip()
        date_of_birth=self.date_of_birth.get().strip()
        birthdate=self.validate_date_of_birth(date_of_birth)

        if os.path.exists(f"{username}.txt"):
            mb.showwarning("Warning", "Your username already exists. "+
                           "Please choose another one or if you have "+
                           "already signed up before, please login "+
                           "(click the button on the top right)", 
                           parent=self.signup_window)
            return

        with open(f"{username}.txt", "w") as file:
            file.write("Profile Data:\n")
            file.write(f"First Name: {first_name}\n")
            file.write(f"Birthdate: {birthdate.strftime('%d/%m/%Y')}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")

        self.parent.store_pending_user_info(first_name, username, 
                                            password, date_of_birth)
        
        mb.showinfo("Success", "Your data has been saved. Please login"+
                    " next time with your exact details. Thank you :)", 
                    parent=self.signup_window)
        #self.signup_window.destroy()

        # Open the QuestionWindow on top of SignUpWindow
        word_list = ["Grammar", "Spelling", "Vocabulary"]
        # In the signup method, instead of directly calling QuestionWindow with word_list, pass user_info as well!!!!!!!!!!!!!!!!!
        self.question_window = QuestionWindow(self.parent, word_list, self.signup_window, self.parent.user_info)


# All the code for the literacy area question                                
class QuestionWindow:
    """The Question Window that appears after sign up."""
    def __init__(self, parent, word_list, signup_window, user_info):
        self.signup_window = signup_window  # The signup window reference
        self.parent = parent  # MainWindow object passed here
        self.user_info = user_info  # Store the user_info passed from MainWindow
        self.window = tk.Toplevel()  # Modal-like window on top
        self.window.title("Question Window")
        self.window.configure(bg="oldlace")
        self.window.resizable(False, False)
        #self.opt_selected = IntVar()

        # Calculate center position
        w_w=600  # Window width
        w_h=330  # Window height
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        # Headings for the different entries
        label=tk.Label(self.window, text="Question", 
                        font=("Helvetica", 20, "bold"), 
                        fg="black", bg="oldlace")
        label.pack(pady=20)

        title=tk.Label(self.window, text="What areas do you need help with?", 
                                font=("Helvetica", 12, "bold"), 
                                fg="black", bg="oldlace")
        title.pack(pady=2)

        self.word_vars = {}
        for word in word_list:
            self.word_vars[word] = tk.BooleanVar()
            cb = tk.Checkbutton(self.window, text=word, variable=self.word_vars[word], bg="oldlace", font=("Helvetica", 11, "bold"))
            cb.pack(anchor="c")

        self.check_button = tk.Button(self.window, text="Next", bg="white", width=7, 
                                font=("Helvetica", 13, "bold"), 
                                fg="lightseagreen", command=self.finish)
        self.check_button.pack()

        title1=tk.Label(self.window, text="\nThere will be a short quiz that will see what "+ 
                                    "level you are at, when\n you click next. Try "+ 
                                    "your best :)", 
                                font=("Helvetica", 12, "bold"), 
                                fg="black", bg="oldlace")
        title1.pack(pady=1)                                                    

    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)
        
    def open_level_quiz(self):                                                
        """Open level quiz window when all completed."""
        levelquizwindow=tk.Toplevel()
        levelquizwindow.title("Level Quiz")
        levelquizwindow.resizable(False, False)

        # Calculate center position
        window_w=1050  # Window width  
        window_h=650   # Window height
        screen_width=levelquizwindow.winfo_screenwidth()
        screen_height=levelquizwindow.winfo_screenheight()

        x_position=(screen_width-window_w)//2
        y_position=(screen_height-window_h)//4

        # Set window geometry
        levelquizwindow.geometry(f"{window_w}x{window_h}+{x_position}+{y_position}")

        levelquizwindow.attributes('-topmost', True)  # keep window on top
        LevelQuiz(levelquizwindow, self.user_info)  # Now this works correctly, passing user_info

    def finish(self):  # Here is your finish method
        checked_words = [word for word, var in self.word_vars.items() if var.get()]

        # Check if no areas are selected
        if not checked_words:
            mb.showwarning("Warning", "Please select at least one area before proceeding.", parent=self.window)
            return

        # Saving result to the user's file
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data:
            data.write("\nLiteracy Area: \n")
            data.write(f"{checked_words}\n")

        print("Checked words:", checked_words)

        # Close both SignUpWindow and QuestionWindow
        self.signup_window.destroy()
        self.window.destroy()

        # Open Dashboard
        self.open_dashboard()  # This will now call the open_dashboard() method of MainWindow
        # Open Level Quiz
        self.open_level_quiz()  # Now it can access user_info correctly


class LevelQuiz:
    """Code for the window of the level quiz."""
    def __init__(self, root, user_info):
        self.root = root
        self.root.configure(bg="oldlace")
        self.q_no = 0
        self.correct = 0
        self.user_info = user_info

        # Load the data from the JSON file
        with open('data.json') as f:
            self.data = json.load(f)

        self.data_size = len(self.data['question'])

        self.display_title()
        self.display_question()
        self.opt_selected = tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()

        # Progress bar setup
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='lightseagreen')
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, maximum=100, length=300, 
                                             variable=self.progress_var, 
                                             style="green.Horizontal." +
                                             "TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    def next_btn(self):
        """Tell the user that they need to click an option (answer)."""
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option before proceeding.", parent=self.root)
            return

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Progress bar to 100%
            self.root.after(100, self.display_result)  
        else:
            self.update_progress_bar()
            self.display_question()
            self.display_options()

    def display_result(self):
        """Displaying the correct, wrong, and overall score of the quiz."""
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Calculate level based on score
        if self.correct < 6:
            level = "Level 1"
            levelnumber = "1"
        elif self.correct > 6 and self.correct < 12:
            level = "Level 2"
            levelnumber = "2"
        else:
            level = "Level 3"
            levelnumber = "3"

        # Show result message
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}\n{level}", parent=self.root)

        # Saving result to the user's file
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data:
            data.write("\nLevel Quiz scores: \n")
            data.write(f"Date: {date}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")
            data.write("\nLearning Level: \n")
            data.write(f"Level: {levelnumber}")

        self.root.destroy()

    def check_ans(self, q_no):
        """Checking the answers of the options the user clicked."""
        return self.opt_selected.get() == self.data['answer'][q_no]

    def buttons(self):
        """Important buttons for the quiz."""
        next_button = tk.Button(self.root, text="NEXT", command=self.next_btn,
                                bg="white", fg="black", width=7, height=1, 
                                font=("Helvetica", 16, "bold"))
        next_button.place(x=470, y=550)

    def display_options(self):
        """Displaying the options for the different questions."""
        val = 0
        self.opt_selected.set(0)
        for option in self.data['options'][self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        """Displaying the questions for the quiz."""
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label = tk.Label(self.root, text=self.data['question'][self.q_no],
                                width=100, font=('Helvetica', 20, 'bold'),
                                anchor='w', wraplength=900, justify='left',
                                bg="oldlace", fg="black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        """Title of the quiz."""
        title = tk.Label(self.root, text="Level Quiz",
                         width=50, bg="lightseagreen", fg="white", height=2,
                         font=("Helvetica", 26, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        """How the options are shown and clicked by the user (radio buttons)."""
        q_list = []
        y_pos = 250
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self.root, text=" ",
                                       variable=self.opt_selected,
                                       value=len(q_list) + 1,
                                       font=("Helvetica", 18),
                                       fg="black", bg="oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 60
        return q_list
    
    def update_progress_bar(self, final=False):
        """Updating the progress bar when moving onto the next question."""
        if final or self.q_no >= self.data_size:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no/self.data_size) * 100)


# All the code for the Main Quiz
class MainQuiz:
    """Code for the main quiz that displays questions, options, and keeps track of progress."""
    
    def __init__(self, root, quiz_data, user_info, quiz_topic, quiz_level):
        """Initialize the quiz window and display questions based on quiz_data."""
        self.root = root
        self.quiz_data = quiz_data  # Loaded quiz data (questions, options, answers)
        self.user_info = user_info
        self.quiz_topic = quiz_topic
        self.quiz_level = quiz_level
        self.q_no = 0  
        self.correct = 0  
        self.display_title() 
        self.display_question()  
        self.opt_selected = IntVar()  
        self.opts = self.radio_buttons()  
        self.display_options()  
        self.buttons()  
        self.data_size = len(self.quiz_data['question'])  # Total number of questions

        # Calculate center position
        window_w=1050  # Window width  
        window_h=650   # Window height
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()

        x_position=(screen_width-window_w)//2
        y_position=(screen_height-window_h)//4

        # Set window geometry
        root.geometry(f"{window_w}x{window_h}+{x_position}+{y_position}")
        
        # Progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='lightseagreen')
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, maximum=100, length=300, 
                                             variable=self.progress_var, 
                                             style="green.Horizontal." +
                                             "TProgressbar")
        self.progress_bar.place(x=50, y=95)
        self.update_progress_bar()

    def next_btn(self):
        """Handle the 'Next' button click to move to the next question."""
        if self.opt_selected.get() == 0:
            mb.showwarning("Warning", "Please select an option before proceeding.", parent=self.root)
            return

        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.update_progress_bar(final=True)  # Progress bar to 100%
            self.root.after(100, self.display_results)  
        else:
            self.update_progress_bar()
            self.display_question()
            self.display_options()

    def display_results(self):
        """Display the quiz result after the user finishes all questions."""
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Show result message
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}", parent=self.root)

        # Saving result to the user's file
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data:
            data.write("\n\nQuiz Results \n")
            data.write(f"Date: {date}\n")
            data.write(f"Quiz Area: {self.quiz_topic}\n")
            data.write(f"Level: {self.quiz_level}\n")
            data.write(f"Correct: {self.correct}\n")
            data.write(f"Wrong: {wrong_count}\n")
            data.write(f"Score: {score}%\n")

        self.root.destroy()

    def check_ans(self, q_no):
        """Check if the selected answer is correct."""
        return self.opt_selected.get() == self.quiz_data['answer'][q_no]

    def buttons(self):
        """Create important buttons for the quiz, like Next and Quit."""
        next_button = tk.Button(self.root, text="NEXT", command=self.next_btn,
                                bg="white", fg="black", width=7, height=1, 
                                font=("Helvetica", 16, "bold"))
        next_button.place(x=470, y=550)

        quit_button = tk.Button(self.root, text="EXIT", 
                                bg="white", width=7, height=1,
                                fg="black", command=self.check_exit,
                                font=("Helvetica", 16, "bold"))
        quit_button.place(x=920, y=95)

    def check_exit(self):
        """Confirm exit and handle quitting the quiz."""
        result = mb.askquestion("Exit", "Are you sure you want to exit the quiz now?", parent=self.root)
        if result == "yes":
            self.root.destroy()

    def display_options(self):
        """Display the options for the current question."""
        val = 0
        self.opt_selected.set(0)
        for option in self.quiz_data['options'][self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        """Display the current question."""
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label = tk.Label(self.root, text=self.quiz_data['question'][self.q_no],
                                width=100, font=('Helvetica', 20, 'bold'),
                                anchor='w', wraplength=900, justify='left',
                                bg="oldlace", fg="black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        """Display the title of the quiz."""
        title = tk.Label(self.root, text="Quiz",
                         width=50, bg="lightseagreen", fg="white", height=2,
                         font=("Helvetica", 26, "bold"))
        title.place(x=0, y=0)

    def radio_buttons(self):
        """Create radio buttons for each option."""
        q_list = []
        y_pos = 250
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(self.root, text=" ",
                                       variable=self.opt_selected,
                                       value=len(q_list) + 1,
                                       font=("Helvetica", 18),
                                       fg="black", bg="oldlace")
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 60
        return q_list

    def update_progress_bar(self, final=False):
        """Update the progress bar as the quiz progresses."""
        if final or self.q_no >= self.data_size:
            self.progress_var.set(100)
        else:
            self.progress_var.set((self.q_no/self.data_size) * 100)


class QuizSelect:
    """Code for the window where the user can choose what level and area quiz they want."""
    def __init__(self, parent, current_level):
        """Function for the window where the user can choose what level and area quiz they want."""
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Select Quiz Area")
        self.dialog.configure(bg="oldlace")
        self.dialog.resizable(False, False)
        self.level_number = current_level  # User's current level
        self.selected_quiz = None

        # Center the window on screen
        w_w, w_h = 400, 350
        screen_w = self.dialog.winfo_screenwidth()
        screen_h = self.dialog.winfo_screenheight()
        x = (screen_w - w_w) // 2
        y = (screen_h - w_h) // 4
        self.dialog.geometry(f"{w_w}x{w_h}+{x}+{y}")

    def display_variable(self):
        """Code for what is displayed in that window, the looks and text shown."""
        # Label to show current level
        level_label = tk.Label(self.dialog, 
                               text=f"Your current level: {self.level_number}",
                               font=("Helvetica", 15, "bold"), bg="oldlace")
        level_label.pack(pady=10)

        # Info label
        info_label = tk.Label(self.dialog,
                              text="You can keep this level or select a different one:",
                              font=("Helvetica", 12), bg="oldlace")
        info_label.pack(pady=5)

        # Dropdown to choose level
        levels = [1, 2, 3]
        self.level_var = tk.IntVar(value=self.level_number)
        level_dropdown = ttk.Combobox(self.dialog, values=levels, textvariable=self.level_var, state="readonly")
        level_dropdown.pack(pady=5)

        # Label for quiz type
        quiz_label = tk.Label(self.dialog,
                              text="Select the quiz area:",
                              font=("Helvetica", 14, "bold"), bg="oldlace")
        quiz_label.pack(pady=15)

        # Buttons for quiz types
        grammar_btn = tk.Button(self.dialog, text="Grammar", width=20, height=2,
                                command=self.select_grammar)
        grammar_btn.pack(pady=5)

        spelling_btn = tk.Button(self.dialog, text="Spelling", width=20, height=2,
                                 command=self.select_spelling)
        spelling_btn.pack(pady=5)

        vocab_btn = tk.Button(self.dialog, text="Vocabulary", width=20, height=2,
                              command=self.select_vocab)
        vocab_btn.pack(pady=5)

    def select_grammar(self):
        """The grammar quizzes - calls it."""
        chosen_level = self.level_var.get()
        self.selected_quiz = f"level{chosen_level}Grammar.json"
        self.dialog.destroy()

    def select_spelling(self):
        """The spelling quizzes - calls it.."""
        chosen_level = self.level_var.get()
        self.selected_quiz = f"level{chosen_level}Spelling.json"
        self.dialog.destroy()

    def select_vocab(self):
        """The vocab quizzes - calls it.."""
        chosen_level = self.level_var.get()
        self.selected_quiz = f"level{chosen_level}Vocabulary.json"
        self.dialog.destroy()

    def get_selected_quiz(self):
        return self.selected_quiz
    

# image slideshow (controlled) 2 code
class Slideshow:
    """The code that shows the slideshow pictures in the learn class / page."""
    def __init__(self, parent, image_dir):
        """Function to get the different images from the folder, and the looks."""
        self.top = tk.Toplevel(parent)
        self.top.title("Literacy Learning Slideshow")

        self.image_dir = image_dir
        self.images_by_level = {'1': [], '2': [], '3': []}

        # Load images from subdirectories: images/Level 1/, images/Level 2/, etc.
        level_dirs = {'1': 'Level 1', '2': 'Level 2', '3': 'Level 3'}
        for level, folder in level_dirs.items():
            level_path = os.path.join(self.image_dir, folder)
            if os.path.exists(level_path):
                for f in os.listdir(level_path):
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        self.images_by_level[level].append(os.path.join(level_path, f))

        self.level = '1'
        self.current_index = 0

        self.level_var = tk.StringVar(value='1')
        self.create_level_selector()

        self.canvas = tk.Canvas(self.top, width=600, height=600, bg="white")
        self.canvas.pack(pady=20)

        btn_frame = tk.Frame(self.top, bg="white")
        btn_frame.pack()

        self.prev_button = tk.Button(btn_frame, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(btn_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.display_image()

    def create_level_selector(self):
        """The looks and labels on the slideshow window."""
        level_frame = tk.Frame(self.top, bg="white")
        level_frame.pack(pady=10)

        tk.Label(level_frame, text="Select Level:", font=("Helvetica", 12, "bold"), bg="white").pack(side=tk.LEFT)
        for lvl in ['1', '2', '3']:
            rb = tk.Radiobutton(level_frame, text=f"Level {lvl}", variable=self.level_var, value=lvl,
                                command=self.change_level, bg="white", font=("Helvetica", 12))
            rb.pack(side=tk.LEFT, padx=5)

    def change_level(self):
        """Lets the user to change between the different levels."""
        self.level = self.level_var.get()
        self.current_index = 0
        self.display_image()

    def display_image(self):
        """To display the various pictures (sizing etc.) from the folder."""
        image_list = self.images_by_level.get(self.level, [])
        if not image_list:
            self.canvas.delete("all")
            self.canvas.create_text(400, 300, text="No images found for this level.",
                                    font=("Helvetica", 18), fill="red")
            return

        image_path = image_list[self.current_index % len(image_list)]
        image = Image.open(image_path)
        image = image.resize((601, 601), Image.Resampling.LANCZOS) # resizing and is aligned with the Pillow library
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def next_image(self):
        """To go to the next picture."""
        if self.images_by_level[self.level]:
            self.current_index = (self.current_index + 1) % len(self.images_by_level[self.level])
            self.display_image()

    def prev_image(self):
        """To go back to the last picture."""
        if self.images_by_level[self.level]:
            self.current_index = (self.current_index - 1) % len(self.images_by_level[self.level])
            self.display_image()


# All the code for the Main Home Page
class DashboardWindow:
    """Code for the window after user had logged in."""
    def __init__(self, master, user_info):
        """Basic functionality and display for the window."""
        self.master=master
        self.user_info=user_info
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

        title=tk.Label(self.dashboard_window, text="Page By Page", 
                       font=("Helvetica", 20, "bold"), fg="lightseagreen", 
                       bg="oldlace")
        title.pack(pady=20)

        # Sidebar and main area
        self.create_sidebar()
        self.create_main_area()

        exit_button=tk.Button(self.dashboard_window, text='EXIT', 
                              font=("Helvetica", 10, "bold"), width=10, 
                              height=2, fg="black", bg="white", 
                              command=self.check_exit)
        exit_button.place(x=1090, y=685)

        signout_button=tk.Button(self.dashboard_window, text='SIGN OUT', 
                                 font=("Helvetica", 10, "bold"), width=10, 
                                 height=2, fg="black", bg="white", 
                                 command=self.signout)
        signout_button.place(x=1090, y=620)

        profile_button=tk.Button(self.dashboard_window, text='PROFILE', 
                                 font=("Helvetica", 10, "bold"), width=10, 
                                 height=2, fg="lightseagreen", bg="white", 
                                 command=self.display_profile)
        profile_button.place(x=1090, y=50)

        self.display_home()

    def check_exit(self):
        """Verify if the user wants to exit."""
        result=mb.askquestion("Exit", "Are you sure you want to exit the "+
                              "program now?", parent=self.dashboard_window)
        if result=="yes":
            self.master.destroy()

    def signout(self):
        """Verify if the user wants to sign out."""
        result=mb.askquestion("Sign Out", "Are you sure you want to sign "+
                              "out of the program now?", 
                              parent=self.dashboard_window)
        if result=="yes":
            self.dashboard_window.destroy()

    # The buttons on the side - tabs - because they are all in the same
    # window.
    def create_sidebar(self):
        """The side bar buttons on the window."""
        buttons=[
            ("HOME", self.display_home),
            ("USER\nMANUAL", self.display_manual),
            ("QUIZ", self.display_quiz),
            ("LEARN", self.display_learn),
            ("ABOUT", self.display_about),
            ("HELP", self.display_help)
        ]

        for i, (text, command) in enumerate(buttons):
            btn=tk.Button(self.dashboard_window, text=text, width=11, 
                          height=2, font=("Helvetica", 10, "bold"), 
                          fg="lightseagreen", bg="white", command=command)
            btn.place(x=50, y=50+i*100)
    
    # The area that will be cleared to create the tab look. Where it 
    # will be on the same window but the display will change in the 
    # specified area.
    def create_main_area(self):
        """Specified area of the window that soon will be cleared 
        everytime another tab is pressed (sidebar buttons - tabs).
        """
        self.main_frame=tk.Frame(self.dashboard_window, bg="oldlace")
        self.main_frame.place(x=250, y=50, width=900, height=700)

    def clear_main_area(self):
        """Clearing the specified area for the tabs."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # The Home page of the Dashboard Window
    def display_home(self):
        """The home page of the window. The display of titles etc."""
        self.clear_main_area() # Specified part cleared for the new display                                        

        # Title label
        title_label=tk.Label(self.main_frame, text="Home Page", 
                             font=("Helvetica", 30), fg="black", 
                             bg="oldlace")
        title_label.place(x=240, y=5)

        label=tk.Label(self.main_frame, 
                       text="Welcome to the Home Page\nThis program is to "+
                       "teach and test you on your knowledge on specific \n"+
                       "areas of literacy like spelling, grammar, and "+
                       "vocabulary.\nClick the buttons on the side "+
                       "to navigate through the program.", 
                       font=("Helvetica", 14),
                       fg="lightseagreen", bg="oldlace")
        label.place(x=10, y=60)

        # Load and display image
        home_image_path="imagehome.jpg"
        home_image=Image.open(home_image_path)
        resize_image=home_image.resize((700, 530))
        self.home_img=ImageTk.PhotoImage(resize_image)

        home_image_label=tk.Label(self.main_frame, image=self.home_img)
        home_image_label.image=self.home_img  
        home_image_label.place(y=130, x=0)

    # The Home page of the Dashboard Window
    def display_manual(self):
        """The display of the user manual for the user - as a picture."""
        self.clear_main_area() # Specified part cleared for the new display 

        title2=tk.Label(self.main_frame, text="User Manual", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

        # Load and display image - of the user manual
        manual_image_path="manual.png"
        manual_image=Image.open(manual_image_path)
        resize_image=manual_image.resize((670, 600))
        self.manual_img=ImageTk.PhotoImage(resize_image)

        manual_image_label=tk.Label(self.main_frame, image=self.manual_img, 
                                      borderwidth=0, highlightthickness=0)
        manual_image_label.image=self.manual_img  
        manual_image_label.place(y=80, x=50)

    # The Quiz page of the Dashboard Window
    def display_quiz(self):
        """Displaying the quiz page where the user can choose between the
        grammar, spelling, or vocabulary quiz."""
        self.clear_main_area()  # Specified part cleared for the new display

        # Title label
        title_label = tk.Label(self.main_frame, text="Quiz Page", 
                               font=("Helvetica", 30), fg="black", 
                               bg="oldlace")
        title_label.place(x=249, y=5)

        label = tk.Label(self.main_frame, text="Welcome to the Quiz Page\nTo" +
                         " take the quiz, press the quiz button below.\n" +
                         "Then go onto the Learn tab to teach yourself " +
                         "more, to do better in the quiz, next time.",
                         font=("Helvetica", 15), fg="lightseagreen", bg="oldlace")
        label.place(x=0, y=80)

        # Load and display image
        image_path = "quizpageimage.jpg"
        image = Image.open(image_path)
        resize_image = image.resize((750, 350))
        img = ImageTk.PhotoImage(resize_image)

        image_label = tk.Label(self.main_frame, image=img)
        image_label.image = img  
        image_label.place(y=200, x=0)

        # Quiz button
        quiz_button = tk.Button(self.main_frame, text='QUIZ', width=10, 
                                height=2, font=("Helvetica", 10, "bold"), 
                                fg="lightseagreen", bg="white", 
                                command=self.open_quiz_window_message)
        quiz_button.place(x=300, y=635)

    def open_quiz_window_message(self):
        current_level = self.user_info.get("level", 1)  # default level 1
        quiz_dialog = QuizSelect(self.dashboard_window, current_level)
        quiz_dialog.display_variable()
        self.dashboard_window.wait_window(quiz_dialog.dialog)

        selected_quiz = quiz_dialog.get_selected_quiz()
        if selected_quiz:
            try:
                with open(selected_quiz) as f:
                    quiz_data = json.load(f)
                # Save the selected quiz file path so open_quiz_window can use it
                self.selected_quiz_path = selected_quiz  
                self.open_quiz_window(quiz_data)
            except FileNotFoundError:
                mb.showerror("Error", f"Quiz file {selected_quiz} not found.")
        else:
            mb.showwarning("No Selection", "No quiz selected. Please choose a quiz area.", parent=self.dashboard_window)


    def open_quiz_window(self, quiz_data):
        # Extract quiz_level and quiz_topic from the saved quiz file path
        import re
        quiz_level = "Unknown"
        quiz_topic = "Unknown"

        # Example filename format: "level1grammar.json" or "level2spelling.json"
        if hasattr(self, 'selected_quiz_path'):
            filename = self.selected_quiz_path.lower()
            match = re.search(r"level(\d)(grammar|spelling|vocab|vocabulary)", filename)
            if match:
                quiz_level = match.group(1)
                quiz_topic = match.group(2)
                # Normalize vocabulary naming if needed
                if quiz_topic == "vocabulary":
                    quiz_topic = "vocab"

        # Now open the quiz window
        quiz_window = tk.Toplevel(self.master)
        quiz_window.title("Quiz")
        quiz_window.configure(bg="oldlace")
        quiz_window.resizable(False, False)

        # Pass quiz_topic and quiz_level to MainQuiz
        MainQuiz(quiz_window, quiz_data, self.user_info, quiz_topic, quiz_level)

    
    def open_learn_slideshow(self):
        image_directory = "images"  # Update this if your folder is elsewhere
        Slideshow(self.main_frame, image_directory)

    # Display the learn page
    def display_learn(self):
        """Display the learn page."""
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="Learn", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

        # Load and display image
        image_path="learnpage.jpg"
        image=Image.open(image_path)
        resize_image=image.resize((700, 350))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img  
        image_label.place(x=30, y=320)

        text_for_button = tk.Label(self.main_frame, 
                                   text = "Click the button to learn in your chosen level and literacy area",
                                   font = ("Helvetica", 15), fg = "black", bg = "oldlace")
        text_for_button.place(x=200, y=100)

        slideshow_button = tk.Button(self.main_frame, text = "Click here",
                                     command = self.open_learn_slideshow)
        slideshow_button.place(x=290, y=150)

        # Add the Photos / Videos button
        photos_button=tk.Button(self.main_frame, text="MORE INFORMATION", 
                                bg="white", font=("Helvetica", 13, "bold"), 
                                command=self.open_photos_window)
        photos_button.place(x=240, y=200)

    def open_photos_window(self):
        """Window where there are videos and pictures that are eductational
        and fun for the topics. 
        """
        self.photos_window=tk.Toplevel(self.master)
        self.photos_window.title("Photo / Videos / Animations?")
        self.photos_window.configure(bg="oldlace")
        self.photos_window.resizable(False, False)

        # Calculate center position
        w_w=1000  # Window width
        w_h=600  # window height
        screen_width=self.photos_window.winfo_screenwidth()
        screen_height=self.photos_window.winfo_screenheight()

        x_place=(screen_width-w_w)//2
        y_place=(screen_height-w_h)//4

        # Set window geometry
        self.photos_window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

        title=tk.Label(self.photos_window, text="Page By Page", 
                         font=("Helvetica", 20, "bold"), fg="lightseagreen", 
                         bg="oldlace")
        title.pack(pady=20)

        # Video links and buttons
        def open_video1():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=r8OJuXRT9PE"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video For A Quick Quiz:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 1", fg = "lightseagreen",
                      font=("Helvetica", 12, 'bold'), command=open_video1)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video2():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=Qz0LWrJDfx0"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video About Syllables "+
                                 "And Words:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)

        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 2", fg = "lightseagreen",
                      font=("Helvetica", 12, 'bold'), command=open_video2)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video3():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=BsQj1Q6Q5PA"
            webbrowser.open(video_url)

        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text="Video To Exercise "+
                                 "Your Spelling:", 
                                 font=("Helvetica", 11, 'bold'), fg="black", 
                                 bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 3", fg = "lightseagreen",
                      font=("Helvetica", 12, 'bold'), command=open_video3)
        btn.pack(pady=7)

        # Video links and buttons
        def open_video4():
            """Opening the youtube link."""
            # URL of the YouTube video
            video_url="https://www.youtube.com/watch?v=Yav8BcHk2D4"
            webbrowser.open(video_url)
        
        # Label for video URL input
        video_url_label=tk.Label(self.photos_window, text=" Video About "+
                                  "Reading Sentences:",
                                  font=("Helvetica", 11, 'bold'), fg="black", 
                                  bg="oldlace")
        video_url_label.pack(pady=10)
        
        # Button to open the video
        btn=tk.Button(self.photos_window, text="Play Video 4", fg = "lightseagreen",
                      font=("Helvetica", 12, 'bold'), command=open_video4)
        btn.pack(pady=7)

        back=tk.Button(self.photos_window, text="EXIT",  
                       font=("Helvetica", 13, 'bold'), 
                       command=self.photos_window.destroy)
        back.pack(pady=30)

        # Load and display image 1
        image_path1="learnpic3.jpg"
        image1=Image.open(image_path1)
        resize_image1=image1.resize((250, 250))
        img1=ImageTk.PhotoImage(resize_image1)

        image_label1=tk.Label(self.photos_window, image=img1)
        image_label1.image=img1  
        image_label1.place(y=20, x=19)

        # Load and display image 2
        image_path2="learnpic2.jpg"
        image2=Image.open(image_path2)
        resize_image2=image2.resize((250, 250))
        img2=ImageTk.PhotoImage(resize_image2)

        image_label2=tk.Label(self.photos_window, image=img2)
        image_label2.image=img2  
        image_label2.place(y=20, x=730)

        # Load and display image 3
        image_path3="image1.jpg"
        image3=Image.open(image_path3)
        resize_image3=image3.resize((350, 250))
        img3=ImageTk.PhotoImage(resize_image3)

        image_label3=tk.Label(self.photos_window, image=img3)
        image_label3.image=img3  
        image_label3.place(y=330, x=630)

        # Load and display image 4
        image_path4="learnpic1.png"
        image4=Image.open(image_path4)
        resize_image4=image4.resize((350, 250))
        img4=ImageTk.PhotoImage(resize_image4)

        image_label4=tk.Label(self.photos_window, image=img4)
        image_label4.image=img4  
        image_label4.place(y=330, x=19)

    # The About page of the Dashboard Window
    def display_about(self):
        """Displaying the about info of the entire program and picture."""
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="About", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

        # Create a Text widget to display file contents
        self.configfile=Text(self.main_frame, wrap="word", bd=0, 
                             bg="oldlace", font=("Helvetica", 13))
        self.configfile.config(state='normal') 
        self.configfile.place(x=0, y=100, width=775, height=250)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 13, "bold"))

        # Open and read the file
        filename="aboutpagetext"
        try:
            with open(filename, 'r') as f:
                content=f.read()
                self.configfile.insert(INSERT, content)
                
                # Example of making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "5.0", "5.end")
                self.configfile.tag_add("bold", "6.0", "6.end")
                self.configfile.tag_add("bold", "9.0", "9.end")
                self.configfile.tag_add("bold", "12.0", "12.end")
                self.configfile.tag_add("bold", "15.0", "15.end")
                self.configfile.tag_add("bold", "19.0", "20.end")
                
                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' "+
                                   "not found.")
        
        self.configfile.config(state='disabled')  # Text widget read-only

        # Load and display image
        image_path="aboutus.png"
        image=Image.open(image_path)
        resize_image=image.resize((700, 300))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img  
        image_label.place(x=30, y=370)

    # The Home page of the Dashboard Window
    def display_help(self):
        """Displaying the help questions and answer of the program and 
        picture.
        """
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="Help", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

        # Create a Text widget to display file contents
        self.configfile=Text(self.main_frame, wrap="word", bd=0, 
                             bg="oldlace", font=("Helvetica", 13))
        self.configfile.config(state='normal')  
        self.configfile.place(x=0, y=100, width=775, height=250)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=self.configfile.yview)
        scrollbar.place(x=762, y=100, height=250)
        self.configfile.configure(yscrollcommand=scrollbar.set)

        # Define tags for the font color and bold text
        self.configfile.tag_configure("custom_color", foreground="black")
        self.configfile.tag_configure("bold", font=("Helvetica", 13, "bold"))

        # Open and read the file
        filename="helppagetext"
        try:
            with open(filename, 'r') as f:
                content=f.read()
                self.configfile.insert(INSERT, content)
                
                # Making specific text bold
                self.configfile.tag_add("bold", "1.0", "1.end")
                self.configfile.tag_add("bold", "2.0", "2.9")
                self.configfile.tag_add("bold", "3.0", "3.7")
                self.configfile.tag_add("bold", "5.0", "5.9")
                self.configfile.tag_add("bold", "6.0", "6.7")
                self.configfile.tag_add("bold", "8.0", "8.9")
                self.configfile.tag_add("bold", "9.0", "9.7")
                self.configfile.tag_add("bold", "11.0", "11.9")
                self.configfile.tag_add("bold", "12.0", "12.7")
                self.configfile.tag_add("bold", "14.0", "14.end")
                self.configfile.tag_add("bold", "15.0", "15.9")
                self.configfile.tag_add("bold", "16.0", "16.7")
                self.configfile.tag_add("bold", "18.0", "18.9")
                self.configfile.tag_add("bold", "19.0", "19.7")
                self.configfile.tag_add("bold", "21.0", "21.9")
                self.configfile.tag_add("bold", "22.0", "22.7")
                self.configfile.tag_add("bold", "24.0", "24.9")
                self.configfile.tag_add("bold", "25.0", "25.7")
                self.configfile.tag_add("bold", "27.0", "27.9")
                self.configfile.tag_add("bold", "28.0", "28.7")
                self.configfile.tag_add("bold", "30.0", "30.9")
                self.configfile.tag_add("bold", "31.0", "31.7")

                # Apply custom color to the entire content
                self.configfile.tag_add("custom_color", "1.0", "end")
        except FileNotFoundError:
            self.configfile.insert(INSERT, f"Error: File '{filename}' "+
                                   "not found.")
        
        self.configfile.config(state='disabled')  # text widget read-only

        # Load and display image
        image_path="helppagepic.jpg"
        image=Image.open(image_path)
        resize_image=image.resize((700, 300))
        img=ImageTk.PhotoImage(resize_image)

        image_label=tk.Label(self.main_frame, image=img)
        image_label.image=img 
        image_label.place(x=30, y=370)

    def display_profile(self):
        """Display the profile page with a dropdown for data selection."""
        self.clear_main_area()

        profile_frame = tk.Frame(self.main_frame, bg="oldlace")
        profile_frame.place(x=240, y=45)

        if 'first_name' in self.user_info:
            profile_frame=tk.Frame(self.main_frame, bg="oldlace")
            profile_frame.place(x=240, y=45)  

            title_label=tk.Label(profile_frame, text="Profile Information", 
                                 font=("Helvetica", 20, "bold"), 
                                 bg="oldlace", fg="black")
            title_label.grid(row=0, column=0, columnspan=2, pady=(5, 20))

            info_label=tk.Label(self.main_frame, text="Your profile details"+
                                " and all your quiz results.", 
                                font=("Helvetica", 15), fg="lightseagreen", 
                                bg="oldlace")
            info_label.place(x=155, y=10)

            labels=["First Name:", "Username:", 
                      "Date of Birth:", "Password:"]
            values=[self.user_info['first_name'], self.user_info['username'], 
                    self.user_info['date_of_birth'], 
                    self.user_info['password']]

            for i, (label_text, value_text) in enumerate(zip(labels, values)):
                label=tk.Label(profile_frame, text=label_text, 
                               font=("Helvetica", 15, "bold"), bg="oldlace", 
                               fg="black", anchor="w")
                label.grid(row=i+1, column=0, sticky="w", padx=(0, 20), pady=5)
                value=tk.Label(profile_frame, text=value_text, 
                               font=("Helvetica", 15), bg="oldlace", 
                               fg="black", anchor="w")
                value.grid(row=i+1, column=1, sticky="w", pady=5)
        else:
            label=tk.Label(self.main_frame, text="Profile information not"+
                           " available", font=("Helvetica", 16), fg="black", 
                           bg="oldlace")
            label.place(x=250, y=60)  

        # Dropdown to choose the data area to display
        self.data_selection = ttk.Combobox(self.main_frame, 
                                           width=20, 
                                           values=["Literacy Area", "Level Info", 
                                                   "Level Quiz Info", "Quiz Results"],
                                           state="readonly")
        self.data_selection.place(x=140, y=280)

        self.data_selection.current(0)  # Default value
        select_button = tk.Button(self.main_frame, text="Show Data", 
                                  command=self.show_selected_data)
        select_button.place(x=300, y=280)

        # Create a Text widget to display the selected file contents
        self.text_widget = tk.Text(self.main_frame, wrap="word", 
                                   font=("Helvetica", 13, "bold"), bg="oldlace", 
                                   bd=0, fg="black", width=60, height=17, highlightthickness=2,
                                   highlightbackground="black", relief="solid") # Creates a solid line border
        self.text_widget.place(x=140, y=320, width=485, height=280)

        # Add a scrollbar to the canvas
        scrollbar=ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, 
                                command=self.text_widget.yview)
        scrollbar.place(x=606, y=322, height=276)
        self.text_widget.configure(yscrollcommand=scrollbar.set)

        # Add a default message
        self.text_widget.insert(tk.END, "Choose what data you would like to see, by clicking on the dropdown above.")
        self.text_widget.config(state=tk.DISABLED)

    def show_selected_data(self):
        # Open the user's profile file
        file_path = f"{self.user_info['username']}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Default content to display if sections are missing
            content_to_display = "No specific data found for this section."

            # Print dropdown selection and file content
            print(f"User selected: {self.data_selection.get()}")  
            print("File content:\n", "".join(lines))  

            # Based on the selected dropdown option, find the correct lines to display
            if "Literacy Area" in self.data_selection.get():
                # Show lines 7 and 8 (index 6 and 7)
                areas_line = lines[7].strip()
                # Remove the square brackets and quotes from the list
                areas = areas_line.strip("[]").replace("'", "").split(", ")
                # Format the areas as a list of items
                formatted_areas = "\n".join(areas)
                content_to_display = f"Literacy Areas:\n{formatted_areas}"

            elif "Level Quiz Info" in self.data_selection.get():
                # Show lines 10 to 14 (index 9 to 13)
                content_to_display = ''.join(lines[9:14]).strip()

            elif "Level Info" in self.data_selection.get():
                # Show lines 16 and 17 (index 15 and 16)
                content_to_display = lines[15] + lines[16].strip()

            elif "Quiz Results" in self.data_selection.get():
                if "Quiz Results" == False:
                    content_to_display = "You have no quiz results to show at the moment."
                else:
                    # Show lines 19 onward (index 18 and onward)
                    content_to_display = ''.join(lines[18:]).strip()

            # Enable the Text widget for insertion
            self.text_widget.config(state=tk.NORMAL)

            # Clear previous content in the Text widget
            self.text_widget.delete(1.0, tk.END)

            # Insert the new content into the Text widget
            self.text_widget.insert(tk.END, content_to_display)

            # Can't editing again after inserting content
            self.text_widget.config(state=tk.DISABLED)

            # Ensure the widget is updated correctly
            self.text_widget.update_idletasks()

        else:
            # If the file doesn't exist, show an error message
            no_file_label = tk.Label(self.main_frame, text="Profile file not found", 
                                    font=("Helvetica", 16), fg="black", bg="oldlace")
            no_file_label.place(x=250, y=250)

    def clear_main_area(self):
        """Clearing the specified area for the tabs."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app=MainWindow(root)
    root.mainloop()