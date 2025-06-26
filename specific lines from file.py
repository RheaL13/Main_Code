import tkinter as tk
from tkinter import ttk

def read_file_lines(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        return None

def display_lines(lines, line_numbers):
    text_area.config(state='normal')
    text_area.delete('1.0', tk.END)
    for line_number in line_numbers:
        if 0 < line_number <= len(lines):
            line = lines[line_number - 1]
            text_area.insert(tk.END, line)
    text_area.config(state='disabled')

window = tk.Tk()
window.title("Line Display")
text_area = tk.Text(window, wrap='word', state='disabled', height=10, width=50)
text_area.pack(padx=10, pady=10)

dropdown_options = ["Literacy Area", "Level Info", "Level Quiz Info", "Quiz Results"]
selected_line = tk.StringVar()
dropdown = ttk.Combobox(window, textvariable=selected_line, values=dropdown_options)
dropdown.pack(pady=10)

def load_and_display():
    filepath = "r.txt"
    lines = read_file_lines(filepath)
    if "Literacy Area" in selected_line.get():
        if lines:
            display_lines(lines, [7, 8])  # Example line numbers to display
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, "File not found!")
            text_area.config(state='disabled')
    elif "Level Info" in selected_line.get():
        if lines:
            display_lines(lines, [16, 17])  # Example line numbers to display
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, "File not found!!")
            text_area.config(state='disabled')
    elif "Level Quiz Info" in selected_line.get():
        if lines:
            display_lines(lines, [10, 11, 12, 13, 14])  # Example line numbers to display
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, "File not found!!!")
            text_area.config(state='disabled')
    elif "Quiz Results" in selected_line.get():
        if lines:
            display_lines(lines, [19])  # Example line numbers to display
        else:
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, "File not found!!!!")
            text_area.config(state='disabled')
    else:
        text_area.config(state='normal')
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, "File not found!!!!!")
        text_area.config(state='disabled')


button = ttk.Button(window, text="Display Lines", command=load_and_display)
button.pack(pady=10)

window.mainloop()
