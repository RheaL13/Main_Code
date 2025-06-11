from tkinter import *  

# root = Tk()  
# root.geometry("200x200")  

# def show():  
#     label.config(text=opt.get()) 
#     if option == "Literacy Area":
#         label.config(text=opt.get()) 
#     elif option == "Level Info":
#         label.config(text=opt.get()) 
#     elif option == "Level Quiz Info":
#         label.config(text=opt.get()) 
#     elif option == "Quiz Results":
#         label.config(text=opt.get())  

# # Dropdown options  
# option = ["Literacy Area", "Level Info", "Level Quiz Info", "Quiz Results"]  

# # Selected option variable  
# opt = StringVar(value="Select an option")  

# # Dropdown menu  
# OptionMenu(root, opt, *option).pack()  

# # Button to update label  
# Button(root, text="Submit", command=show).pack()  

# label = Label(root, text=" ")  
# label.pack()  

# root.mainloop()

#-----------------------------------------------------------------------------------------------------

# from tkinter import messagebox, ttk
# import tkinter as tk

# # def display_selection():
# #     # Get the selected value.
# #     selection = combo.get()
# #     messagebox.showinfo(
# #         message=f"The selected value is: {selection}",
# #         title="Selection"
# #     )

# def display():
#     if combo == "Literacy Area":
#         selection = combo.get()
#         label1 = tk.Label(selection)
#         label1.place(x=50, y=140)
#         label=tk.Label(main_window, text="Profile information not"+
#                            " available", font=("Helvetica", 13), fg="black")
#         label.place(x=50, y=140)  
#     elif combo == "Level Info":
#         label=tk.Label(main_window, text="Profile information not"+
#                            " available", font=("Helvetica", 13), fg="black")
#         label.place(x=50, y=140) 
#     elif combo == "Level Quiz Info":
#         label=tk.Label(main_window, text="Profile information not"+
#                            " available", font=("Helvetica", 13), fg="black")
#         label.place(x=50, y=140) 
#     elif combo == "Quiz Results":
#         label=tk.Label(main_window, text="Profile information not"+
#                             " available", font=("Helvetica", 13), fg="black")
#         label.place(x=50, y=140)   

# main_window = tk.Tk()
# main_window.config(width=300, height=200)
# main_window.title("Combobox")
# combo = ttk.Combobox(
#     state="readonly",
#     values=["Literacy Area", "Level Info", "Level Quiz Info", "Quiz Results"]
# )
# combo.place(x=50, y=50)
# button = ttk.Button(text="Display selection", command=display)
# button.place(x=50, y=100)
# main_window.mainloop()

#------------------------------------------------------------------------------------

# import tkinter as tk
# from tkinter import ttk

# def read_file_lines(file_path):
#     with open(file_path, 'r') as f:
#         lines = [line.strip() for line in f]
#     return lines

# def create_dropdown(root, options):
#     selected_option = tk.StringVar(root)
#     selected_option.set(options[0] if options else "")
#     dropdown = ttk.OptionMenu(root, selected_option, *options)
#     return dropdown, selected_option

# def main():
#     file_path="r.txt"
#     options = read_file_lines(file_path)

#     root = tk.Tk()
#     dropdown, selected = create_dropdown(root, options)
#     dropdown.pack()

#     # Example of getting the selected value
#     def print_selection():
#         print("Selected:", selected.get())

#     button = tk.Button(root, text="Print Selection", command=print_selection)
#     button.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk()
root.title("File Text Printer")

# Dropdown options  
option = ["Literacy Area", "Level Info", "Level Quiz Info", "Quiz Results"]  

# Selected option variable  
opt = StringVar(value="Select an option")  

# Dropdown menu  
OptionMenu(root, opt, *option).pack()  

def print_file_text(event):
    selected_file = "r.txt"
    if selected_file:
        try:
            with open(selected_file, 'r') as file:
                file_content = file.read()
                text_area.delete(1.0, tk.END)  # Clear previous text
                text_area.insert(tk.END, file_content)
        except FileNotFoundError:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, "File not found.")
        except Exception as e:
             text_area.delete(1.0, tk.END)
             text_area.insert(tk.END, f"Error reading file: {e}")

def open_file_dialog():
#     file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#     if file_path:
#         file_var.set(file_path)
#         print_file_text(None)  # Call print_file_text to display content
    print_file_text
    
file_var = tk.StringVar()
file_var.set("Select a file")  # Initial text in the dropdown

file_button = tk.Button(root, text="Select File", command=open_file_dialog)
file_button.pack(pady=10)

text_area = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(pady=10)

root.mainloop()