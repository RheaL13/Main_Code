# # # imports
# # import tkinter as tk
# # from tkinter import ttk

# # # Read values from file
# # creatures = []
# # with open('r.txt') as inFile:
# #     creatures = [line for line in inFile]


# # # Create instance
# # win = tk.Tk()   

# # # Add a title       
# # win.title("Combo Test")


# # # Creature Drop Down
# # ttk.Label(win, text="Select Creature").grid(column=1, row=3)
# # creature_box = tk.StringVar()
# # creature_chosen = ttk.Combobox(win, width=20, state='readonly')
# # creature_chosen['values'] = tuple(creatures)
# # creature_chosen.grid(column=2, row=3)
# # creature_chosen.current(0)

# # # Start GUI
# # win.mainloop()

# #-------------------------

# # # python program demonstrating
# # # Combobox widget using tkinter


# # Importing all the modules for the program
# """Provides functions for creating and removing a directory / folder."""
import os
# """Allows intergers / values to be manipulated randomly."""
# import random
# """For using regular expressions."""
# import re
# """The ability to open websites on web browser."""
# import webbrowser
# """Allows the current date and time to be imported."""
# from datetime import datetime

# """Imports tkinter library."""
import tkinter as tk
# """Allows access to the Tk themed widget set."""
# from tkinter import ttk
# """Holds integer data where we can set integer data and can retrieve it"""
# from tkinter import IntVar
# """Importing the tkinter text style."""
# from tkinter import Text
# """Allowing the text to be inserted in a canvas."""
# from tkinter import INSERT
# """Import the specific font style from the tkinter library."""
# from tkinter import font
# """Allows the tkinter style of message box that pops up."""
# from tkinter import messagebox as mb
# """Imports the tkinter style of image that are saved to display and modify."""
# from PIL import Image
# """Imports the tkinter style of image that are saved to display and modify.."""
# from PIL import ImageTk
# """import json to use json file for data"""
# import json


# # import tkinter as tk
# # from tkinter import ttk

# # # Creating tkinter window
# # window = tk.Tk()
# # window.title('Combobox')
# # window.geometry('1000x1000')

# # # label text for title
# # ttk.Label(window, text = "GFG Combobox Widget", 
# #           background = 'green', foreground ="white", 
# #           font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# # # label
# # ttk.Label(window, text = "Select the Month :",
# #           font = ("Times New Roman", 10)).grid(column = 0,
# #           row = 5, padx = 10, pady = 25)

# # # Combobox creation
# # n = tk.StringVar()
# # monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# # # Adding combobox drop down list
# # monthchoosen['values'] = (' January', 
# #                           ' February',
# #                           ' March',
# #                           ' April',
# #                           ' May',
# #                           ' June',
# #                           ' July',
# #                           ' August',
# #                           ' September',
# #                           ' October',
# #                           ' November',
# #                           ' December')

# # # Create a Text widget to display file contents
# # text_widget=tk.Text(window, wrap="word", 
# #                     font=("Helvetica", 13, "bold"), bg="oldlace", 
# #                     bd=0, fg="black", width=60, height=17)
# # text_widget.place(x=140, y=320, width=485, height=280)

# # if monthchoosen == " January":
# #     file_path="r.txt"
# #     if os.path.exists(file_path):
# #         with open(file_path, 'r') as file:
# #             lines=file.readlines()
# #             if len(lines)>5:
# #                 content=''.join(lines[5:])  # Skip the first 5 lines
# #                 text_widget.insert(tk.END, content)
# #                 text_widget.tag_configure('bold', 
# #                                             font=("Helvetica", 13, "bold"))


# # monthchoosen.grid(column = 1, row = 5)
# # monthchoosen.current()
# # window.mainloop()







# #------------------------------------------


from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk
import os
import tkinter as tk



root = Tk()

root.geometry("400x400")
#^ width - heghit window :D


cmb = ttk.Combobox(root, width="10", values=("Literacy Area","Level Info","Level Quiz Info","Quiz Results"))
#cmb = Combobox

class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = tk.StringVar() # create variable for table
        ttk.Combobox.__init__(self, parent)#  init widget
        self.config(textvariable = self.current_table, state = "readonly", values = ["Customers", "Pets", "Invoices", "Prices"])
        self.current(0) # index of values for current table
        self.place(x = 50, y = 50, anchor = "w") # place drop down box 

def open_file():
    # Create a Text widget to display file contents
    text_widget=tk.Text(root, wrap="word", 
                        font=("Helvetica", 13, "bold"), bg="oldlace", 
                        bd=0, fg="black", width=60, height=17)
    text_widget.place(x=140, y=320, width=485, height=280)

    # Add the code to show the file content below the profile information
    file_path="r.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines=file.readlines()
            if len(lines)>5:
                content=''.join(lines[5:])  # Skip the first 5 lines
                text_widget.insert(tk.END, content)
                text_widget.tag_configure('bold', 
                                            font=("Helvetica", 13, "bold"))

            #     # Apply the bold tag to "Select an option:"
            #     start_idx=1.0
            #     while True:
            #         start_idx=text_widget.search("Select an option:", 
            #                                         start_idx, tk.END)
            #         if not start_idx:
            #             break
            #         end_idx=f"{start_idx}+{len('Select an option:')}c"
            #         text_widget.tag_add('bold', start_idx, end_idx)
            #         start_idx=end_idx
            # else:
            #     text_widget.insert(tk.END, "There is no data found.")

def checkcmbo():

    if cmb.get() == "Literacy Area":
        messagebox.showinfo("What user choose", "you choose Literacy Area")
        open_file

    elif cmb.get() == "Level Info":
        messagebox.showinfo("What user choose", "you choose Level Info")
        open_file

    elif cmb.get() == "Level Quiz Info":
        messagebox.showinfo("What user choose", "you choose Level Quiz Info")
        open_file

    elif cmb.get() == "Quiz Results":
        messagebox.showinfo("What user choose", "you choose Quiz Results")
        open_file

    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "you have to be choose something")


cmb.place(relx="0.1",rely="0.1")

btn = tk.Button(root, text="Get Value",command=checkcmbo)
btn.place(relx="0.5",rely="0.1")

root.mainloop()


#---------------------------------------------------

# import ttkbootstrap

# def click_bind(e):
#     print(my_combo.get())

# root = ttkbootstrap.Window(themename = 'darkly')

# root.title('Hello World') 
# root.geometry('400x400') # width x height

# options = ['1200','2400','4800','9600']


# my_combo = ttkbootstrap.Combobox(value = options)

# my_combo.pack(pady = 50)

# my_combo.bind('<<ComboboxSelected>>',click_bind)


# root.mainloop()