import tkinter as tk
from PIL import Image, ImageTk
import os

class Slideshow:
    def __init__(self, root, image_dir):
        self.root = root
        self.root.title("Image Slideshow")
        self.image_dir = image_dir
        self.image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        self.current_index = 0

        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(root, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.display_image()

    def display_image(self):
        image_path = self.image_paths[self.current_index]
        image = Image.open(image_path)
        image = image.resize((800, 600))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.display_image()

    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_paths)
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    image_dir = "G:\My Drive\Yr 13\Digital Science\Main_Code\images"
    slideshow = Slideshow(root, image_dir)
    root.mainloop()
