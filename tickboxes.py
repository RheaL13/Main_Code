import tkinter as tk

def show_selections():
    selected_options = [option for option, var in option_vars.items() if var.get()]
    print("Selected options:", selected_options)

window = tk.Tk()
window.title("Tick Box Example")

options = ["Option 1", "Option 2", "Option 3"]
option_vars = {}

for option in options:
    var = tk.BooleanVar()
    option_vars[option] = var
    check_button = tk.Checkbutton(window, text=option, variable=var)
    check_button.pack()

select_button = tk.Button(window, text="Show Selections", command=show_selections)
select_button.pack()

window.mainloop()

#------------------------------------------------------------------------------

# import tkinter as tk

# def show_selections():
#     selected_options = [option for option, var in option_vars.items() if var.get()]
#     print("Selected options:", selected_options)

# window = tk.Tk()
# window.title("Tick Box Example")

# options = ["Option 1", "Option 2", "Option 3"]
# option_vars = {}

# for option in options:
#     var = tk.BooleanVar()
#     option_vars[option] = var
#     check_button = tk.Radiobutton(window, text=option, variable=var)
#     check_button.pack()

# select_button = tk.Button(window, text="Show Selections", command=show_selections)
# select_button.pack()

# window.mainloop()