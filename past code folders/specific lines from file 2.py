import tkinter as tk
from tkinter import ttk, filedialog

window = tk.Tk()
window.title("Line Printer")

dropdown_options = ["Line 1", "Line 2", "Line 3", "Line 4"]
selected_line = tk.StringVar()
dropdown = ttk.Combobox(window, textvariable=selected_line, values=dropdown_options)
dropdown.pack(pady=10)

text_box = tk.Text(window, height=10, width=40)
text_box.pack(pady=10)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_path = "r.txt"
                lines = file.readlines()
                # Clear the text box
                text_box.delete("1.0", tk.END)
                # Insert the file content into the text box
                for line in lines:
                    text_box.insert(tk.END, line)
        except Exception as e:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, f"Error loading file: {e}")

def print_selected_line():
    line_number = dropdown_options.index(selected_line.get())
    try:
      lines = text_box.get("1.0", tk.END).splitlines()
      if 0 <= line_number < len(lines):
        print_text = lines[line_number]
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, print_text)
      else:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Invalid line number")
    except:
      text_box.delete("1.0", tk.END)
      text_box.insert(tk.END, "Error, please load a file first")

load_button = tk.Button(window, text="Load File", command=load_file)
load_button.pack(pady=5)
print_button = tk.Button(window, text="Print Line", command=print_selected_line)
print_button.pack(pady=5)

window.mainloop()