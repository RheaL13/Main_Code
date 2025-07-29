import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Slideshow:
    def __init__(self, root, base_dir):
        self.root = root
        self.root.title("Page By Page - Learn Space")
        self.base_dir = base_dir
        self.level_var = tk.StringVar(value="1")

        # Level Selection Dropdown
        level_frame = tk.Frame(root)
        level_frame.pack(pady=10)
        tk.Label(level_frame, text="Select Level:").pack(side=tk.LEFT)
        level_menu = tk.OptionMenu(level_frame, self.level_var, "1", "2", "3", command=self.change_level)
        level_menu.pack(side=tk.LEFT)

        # Current level display label
        self.level_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.level_label.pack(pady=5)

        # Image Display Canvas
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Navigation Buttons
        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)
        self.prev_button = tk.Button(nav_frame, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=20)
        self.next_button = tk.Button(nav_frame, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT, padx=20)

        # Load default level
        self.image_paths = []
        self.current_index = 0
        self.change_level("1")

    def change_level(self, level):
        level_folder = os.path.join(self.base_dir, f"Level {level}")
        if not os.path.exists(level_folder):
            messagebox.showerror("Error", f"Folder not found: {level_folder}")
            return
        self.image_paths = [
            os.path.join(level_folder, f)
            for f in os.listdir(level_folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
        ]
        if not self.image_paths:
            messagebox.showinfo("No Images", f"No images found in Level {level}.")
            self.canvas.delete("all")
            self.level_label.config(text=f"Level {level} - No content available")
            return

        self.current_index = 0
        self.level_label.config(text=f"Now Learning: Level {level}")
        self.display_image()

    def display_image(self):
        image_path = self.image_paths[self.current_index]
        image = Image.open(image_path)
        image = image.resize((800, 600))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")  # Clear previous image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def next_image(self):
        if not self.image_paths:
            return
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.display_image()

    def prev_image(self):
        if not self.image_paths:
            return
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.display_image()


if __name__ == "__main__":
    root = tk.Tk()
    image_base_dir = "/Users/rheaschool/Library/CloudStorage/GoogleDrive-lalr@stu.otc.school.nz/My Drive/Yr 13/Digital Science/Main_Code/images"
    app = Slideshow(root, image_base_dir)
    root.mainloop()
