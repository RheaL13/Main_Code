import tkinter as tk

class QuestionWindow:
    def __init__(self, window, word_list):
        self.window = window
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

        self.word_vars = {}
        for word in word_list:
            self.word_vars[word] = tk.BooleanVar()
            cb = tk.Checkbutton(window, text=word, variable=self.word_vars[word], bg="oldlace", font=("Helvetica", 11, "bold"))
            cb.pack(anchor="c")

        self.check_button = tk.Button(window, text="Next", bg="white", width=7, 
                                font=("Helvetica", 13, "bold"), 
                                fg="green", command=self.print_checked_words)
        self.check_button.pack()

        title1=tk.Label(window, text="\nThere will be a short quiz that will see what "+
                                    "level you are at, when\n you click next. Try "+
                                    "your best :)", 
                                font=("Helvetica", 12, "bold"), 
                                fg="black", bg="oldlace")
        title1.pack(pady=1)

    def print_checked_words(self):
        checked_words = [word for word, var in self.word_vars.items() if var.get()]
        print("Checked words:", checked_words)

if __name__ == "__main__":
    root = tk.Tk()
    word_list = ["Grammar", "Spelling", "Vocabulary"]
    my_gui = QuestionWindow(root, word_list)
    root.mainloop()