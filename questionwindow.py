import tkinter as tk

class QuestionWindow:
    def show_selections(self):
        selected_options = [option for option, var in self.option_vars.items() if var.get()]
        print("Selected options:", selected_options)

    def __init__(self, parent):
        self.parent=parent

    # Create the main window
    window = tk.Tk()

    # Set the title of the window
    window.title("Question Window")
    window.configure(bg="oldlace")
    window.resizable(False, False)

    # Calculate center position
    w_w=600  # Window width
    w_h=330  # Window height
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()

    x_place=(screen_width-w_w)//2
    y_place=(screen_height-w_h)//4

    # Set window geometry
    window.geometry(f"{w_w}x{w_h}+{x_place}+{y_place}")

    # Headings for the different entries
    label=tk.Label(window, text="Question", 
                    font=("Helvetica", 20, "bold"), 
                    fg="black", bg="oldlace")
    label.pack(pady=20)

    title=tk.Label(window, text="What areas do you need help with?", 
                            font=("Helvetica", 12, "bold"), 
                            fg="black", bg="oldlace")
    title.pack(pady=2)

    options = ["Spelling", "Grammar", "Vocabulary"]
    option_vars = {}

    for option in options:
        var = tk.BooleanVar()
        option_vars[option] = var
        check_button = tk.Checkbutton(window, text=option, variable=var, 
                                    bg="oldlace", font=("Helvetica", 11, "bold"))
        check_button.pack(pady=2)

    select_button = tk.Button(window, text="Next", bg="white", width=7, 
                            font=("Helvetica", 13, "bold"), 
                            fg="green", command=show_selections)
    select_button.pack(pady=5)

    title1=tk.Label(window, text="\nThere will be a short quiz that will see what "+
                                "level you are at, when\n you click next. Try "+
                                "your best :)", 
                            font=("Helvetica", 12, "bold"), 
                            fg="black", bg="oldlace")
    title1.pack(pady=1)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = QuestionWindow("My Application")
    app.run()