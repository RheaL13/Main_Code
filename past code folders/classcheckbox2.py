import tkinter as tk

class WordSelector:
    def __init__(self, master):
        self.master = master
        master.title("Word Selector")

        self.options = ["apple", "banana", "cherry", "date"]
        self.checkbox_vars = {}
        self.checkboxes = {}

        for option in self.options:
            self.checkbox_vars[option] = tk.BooleanVar()
            self.checkboxes[option] = tk.Checkbutton(master, text=option, variable=self.checkbox_vars[option])
            self.checkboxes[option].pack(anchor="w")

        self.select_button = tk.Button(master, text="Select Words", command=self.get_selected_words)
        self.select_button.pack()

        self.selected_words_label = tk.Label(master, text="Selected words: ")
        self.selected_words_label.pack()

    def get_selected_words(self):
        selected_words = [option for option, var in self.checkbox_vars.items() if var.get()]
        self.selected_words_label.config(text="Selected words: " + ", ".join(selected_words))

root = tk.Tk()
word_selector = WordSelector(root)
root.mainloop()