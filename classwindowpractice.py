import tkinter as tk
import tkinter.messagebox as msgbox

class MyWindow:
    def __init__(self, title="My GUI"):
        self.window = tk.Tk()
        self.window.title(title)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Enter your name:")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.greet_button = tk.Button(self.window, text="Greet", command=self.greet)
        self.greet_button.pack()

    def greet(self):
        name = self.entry.get()
        if name:
            msgbox.showinfo("Greeting", f"Hello, {name}!")
        else:
            msgbox.showwarning("Warning", "Please enter your name.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MyWindow("My Application")
    app.run()