import tkinter as tk

def open_modal_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Modal Dialog")
    dialog.geometry("200x100")

    # ... add widgets to the dialog ...
    tk.Label(dialog, text="This is a modal dialog.").pack(pady=20)
    tk.Button(dialog, text="Close", command=dialog.destroy).pack()

    # Make the dialog modal
    dialog.transient(root)  # Ensures dialog appears on top of the root
    dialog.grab_set()      # Prevents interaction with other windows
    root.wait_window(dialog) # Pauses execution of the root window until dialog closes
    print("Modal dialog closed.")

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

tk.Button(root, text="Open Modal Dialog", command=open_modal_dialog).pack(pady=50)

root.mainloop()