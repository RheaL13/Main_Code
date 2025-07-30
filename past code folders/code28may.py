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
data = {
    "question": [
        "Which word is spelled correctly?",
        "What is the plural of 'fox'?",
        "Which sentence is correct?",
        "What does the word 'tiny' mean?",
        "Choose the word that rhymes with 'cake'",
        "What is the opposite of 'happy'?",
        "What word fits best? 'The cat sat ___ the mat.'",
        "Which word is a noun?",
        "Which sentence uses capital letters correctly?",
        "Choose the correct past tense: 'What did she ___ yesterday?'",
        "Choose the correct spelling:",
        "Which word is an adjective?",
        "What does 'gigantic' mean?",
        "Which sentence is a question?",
        "Choose the correct version of 'they're'"
    ],
    "options": [
        ["a) frend", "b) fren", "✅ c) friend", "d) frand"],
        ["a) foxes", "b) foxs", "✅ c) foxes", "d) foxess"],
        ["a) She can goes fast.", "b) She going fast.", "✅ c) She goes fast.", "d) She go fast."],
        ["a) loud", "b) fast", "✅ c) very small", "d) very bright"],
        ["a) cook", "b) chalk", "✅ c) lake", "d) kick"],
        ["a) tired", "✅ b) sad", "c) excited", "d) angry"],
        ["a) on", "✅ b) on", "c) in", "d) under"],
        ["a) quickly", "✅ b) apple", "c) red", "d) run"],
        ["a) i like school.", "b) my name is jack.", "✅ c) My name is Jack.", "d) Today is monday."],
        ["a) go", "✅ b) do", "c) does", "d) doing"],
        ["a) becaus", "✅ b) because", "c) becuase", "d) becouse"],
        ["a) jump", "✅ b) tall", "c) run", "d) dog"],
        ["a) tricky", "b) bumpy", "✅ c) very big", "d) very fast"],
        ["a) I like ice cream", "b) She has a bike", "✅ c) Do you like ice cream?", "d) We saw a dog"],
        ["a) Their going to the beach.", "b) There going to the beach.", "✅ c) They’re going to the beach.", "d) They going to the beach."]
    ],
    "answer": [3, 3, 3, 3, 3, 2, 2, 2, 3, 2, 2, 2, 3, 3, 3]
}

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
                       text="Name\nLiteracy Quiz", 
                       font=("Helvetica", 28, "bold"), 
                       fg="green", bg="oldlace")
        label.pack(pady=40)

        description=tk.Label(self.firstwindow, text="Welcome!\nThis "+
                             "program is to teach and test you on "+
                             "your knowledge on \nyour literacy skills "+
                             "(spelling, grammar, and vocabulary). "+
                             "\nIf you are new here, please sign up, "+
                             "otherwise login.",font=("Helvetica", 15), 
                             fg="green", bg="oldlace")
        description.place(x=330, y=140)

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
        mb.showwarning("Warning", "Please login or sign up first.")

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
                              height=1, fg="green", bg="white", 
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
                                       width=7, height=1, fg="green", 
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
                              height=1, fg="green", bg="white", 
                              command=self.signup)
        next_button.pack(pady=20)

        # Button that changes between the sign up and login windows
        def change2():
            """Changing between the sign up and login window."""
            LoginWindow(parent)
            self.signup_window.destroy()

        login_change_button=tk.Button(self.signup_window, text="LOGIN", 
                                      font=("Helvetica", 15, "bold"),
                                      width=7, height=1, fg="green", 
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
        first_name=self.first_name.get().strip()
        username=self.username.get().strip()
        password=self.password.get().strip()
        confirm_password=self.confirm_password.get().strip()
        date_of_birth=self.date_of_birth.get().strip()

        if (first_name=="First Name" or username=="Username" or 
            password=="Password" or confirm_password=="Confirm Password" or 
            date_of_birth=="Date of Birth (DD/MM/YYYY)"):
            mb.showwarning("Incomplete Fields", "Please fill out all "+
                           "the fields.", parent=self.signup_window)
            return False
        
        if len(first_name)>10 or len(username)>10 or len(password)>10:
            mb.showwarning("Invalid Input", "First name, username, and"+
                           " password must be 10 characters or less.", 
                           parent=self.signup_window)
            return False

        if not first_name.isalpha():
            mb.showwarning("Invalid First Name", "First name can only "+
                           "contain letters.", 
                           parent=self.signup_window)
            return False

        if not re.match("^[A-Za-z0-9]+$", username):
            mb.showwarning("Invalid Username", "Username can only "+
                           "contain letters and numbers without "+
                           "spaces.", parent=self.signup_window)
            return False

        if password!=confirm_password:
            mb.showerror("Error", "Passwords do not match.", 
                         parent=self.signup_window)
            return False

        birthdate=self.validate_date_of_birth(date_of_birth)
        if not birthdate:
            mb.showerror("Invalid Date Of Birth", "Please enter a valid "+
                         "date of birth. Remember to include the ' / '.", 
                         parent=self.signup_window)
            return False

        age=(datetime.today()-birthdate).days//365
        if age<0 or age>90:
            mb.showerror("Invalid Date Of Birth", "Invalid date of birth. "+
                         "Remember to include the ' / '.", 
                         parent=self.signup_window)
            return False
        elif age<18 or age>30:
            if age<10:
                age_maybe=mb.askquestion("Age Notice", "Are you sure"+
                                         "that is the correct age?", 
                                         parent=self.signup_window)
                if age_maybe=="no":
                    return False
            else:
                mb.showwarning("Age Notice", "This program is "+
                               "designed for ages 5-15. However you are still"+
                               " able to use the program.", 
                               parent=self.signup_window)
        else:
            mb.showwarning("Age Notice", "This program is designed for"+
                           " ages 18-30.", parent=self.signup_window)
                
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


# All the code for the literacy area question                                         # here
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
                                fg="green", command=self.finish)
        self.check_button.pack()

        title1=tk.Label(self.window, text="\nThere will be a short quiz that will see what "+ 
                                    "level you are at, when\n you click next. Try "+ 
                                    "your best :)", 
                                font=("Helvetica", 12, "bold"), 
                                fg="black", bg="oldlace")
        title1.pack(pady=1)                                                        # to here

    def open_dashboard(self):
        """Open the dashboard window when all completed."""
        self.dashboard=DashboardWindow(self.parent.master, 
                                         self.parent.pending_user_info)
        
    def open_level_quiz(self):                                                        # here!!!!!!!!!
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

    def finish(self):                                                                       # here!!!!!!!!!
        checked_words = [word for word, var in self.word_vars.items() if var.get()]
        
        # Saving result to the user's file
        username = self.user_info.get("username", "user")
        with open(f"{username}.txt", 'a') as data:
            data.write("\nHelp in Literacy Area(s): \n")
            data.write(f"Areas: {checked_words}\n")
        
        print("Checked words:", checked_words)

        # Close both SignUpWindow and QuestionWindow
        self.signup_window.destroy()
        self.window.destroy()

        # Open Dashboard
        self.open_dashboard()  # This will now call the open_dashboard() method of MainWindow
        # Open Level Quiz
        self.open_level_quiz()  # Now it can access user_info correctly


# All the code for the level quiz
class LevelQuiz:
    """Code for the window of the level quiz."""
    def __init__(self, root, user_info):
        self.root = root
        self.root.configure(bg="oldlace")
        self.q_no = 0
        self.correct = 0
        self.user_info = user_info
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(data['question'])

        # Progress bar
        style=ttk.Style()
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", 
                        thickness=30, 
                        troughcolor='black', 
                        background='green')
        self.progress_var=tk.DoubleVar()
        self.progress_bar=ttk.Progressbar(self.root, maximum=100, length=300, 
                                          variable=self.progress_var, 
                                          style="green.Horizontal."+
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

    # def open_dashboard(self):
    #     """Open the dashboard window when all completed."""
    #     self.dashboard=DashboardWindow(self.root, self.root.user_info)           # fix!!!!

    def display_result(self):
        """Displaying the correct, wrong, and overall score of the quiz."""
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        if self.correct < 6:
            level = "You have been put into Level 1"
            levelnumber = "1"
        elif self.correct > 6 and self.correct < 12:
            level = "You have been put into Level 2"
            levelnumber = "2"
        else:
            level = "You have been put into Level 3"
            levelnumber = "3"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}\n{level}", parent=self.root)

        self.root.destroy()

        # Open Dashboard
        #self.open_dashboard()  # This will now call the open_dashboard() method of MainWindow

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
        return self.opt_selected.get() == data['answer'][q_no]

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
        for option in data['options'][self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        """Displaying the questions for the quiz."""
        if hasattr(self, 'q_label'):
            self.q_label.destroy()  # Destroy previous question label
        self.q_label = tk.Label(self.root, text=data['question'][self.q_no],
                                width=100, font=('Helvetica', 20, 'bold'),
                                anchor='w', wraplength=900, justify='left',
                                bg="oldlace", fg="black")
        self.q_label.place(x=50, y=150)

    def display_title(self):
        """Title of the quiz."""
        title = tk.Label(self.root, text="Level Quiz",
                         width=50, bg="green", fg="white", height=2,
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

        title=tk.Label(self.dashboard_window, text="EcoSmart", 
                       font=("Helvetica", 20, "bold"), fg="green", 
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
                                 height=2, fg="green", bg="white", 
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
                          fg="green", bg="white", command=command)
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
                       fg="green", bg="oldlace")
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

    # The Home page of the Dashboard Window
    def display_quiz(self):
        """Displaying the quiz page where the user can choose between the 
        normal or shuffled quiz order. 
        """
        self.clear_main_area() # Specified part cleared for the new display

        title2=tk.Label(self.main_frame, text="Quiz", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

    # Display the learn page
    def display_learn(self):
        """Display the learn page."""
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="Learn", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

    # The About page of the Dashboard Window
    def display_about(self):
        """Displaying the help questions and answer of the program and 
        picture.
        """
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="About", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

    # The Home page of the Dashboard Window
    def display_help(self):
        """Displaying the help questions and answer of the program and 
        picture.
        """
        self.clear_main_area()

        title2=tk.Label(self.main_frame, text="Help", 
                          font=("Helvetica", 30), fg="black", bg="oldlace")
        title2.place(x=230, y=5)

    # The profile page from the Dashboard Window
    def display_profile(self):
        """Display the profile page."""
        self.clear_main_area()

        # label = tk.Label(self.main_frame, text=f"Profile: {self.user_info['first_name']}", font=("Helvetica", 16), fg="black", bg="oldlace")
        # label.pack(pady=20)

        if 'first_name' in self.user_info:
            profile_frame=tk.Frame(self.main_frame, bg="oldlace")
            profile_frame.place(x=240, y=45)  

            title_label=tk.Label(profile_frame, text="Profile Information", 
                                 font=("Helvetica", 20, "bold"), 
                                 bg="oldlace", fg="black")
            title_label.grid(row=0, column=0, columnspan=2, pady=(5, 20))

            info_label=tk.Label(self.main_frame, text="Your profile details"+
                                " and all your quiz results.", 
                                font=("Helvetica", 15), fg="green", 
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


if __name__ == "__main__":
    root = tk.Tk()
    app=MainWindow(root)
    root.mainloop()