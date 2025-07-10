import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Image Slideshow")

image_folder = "/Users/rheaschool/Library/CloudStorage/GoogleDrive-lalr@stu.otc.school.nz/My Drive/Yr 13/Digital Science/Main_Code/images"#G:\My Drive\Yr 13\Digital Science\Main_Code\images"  # Replace with your image folder
image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((600, 400), Image.Resampling.LANCZOS)  # Resize images if needed
    photo_img = ImageTk.PhotoImage(img)
    images.append(photo_img)

image_label = tk.Label(root)
image_label.pack()

current_image_index = 0

def show_image():
    global current_image_index
    image_label.config(image=images[current_image_index])
    current_image_index = (current_image_index + 1) % len(images)  # Loop through images
    root.after(3000, show_image) # Change image every 3 seconds

show_image()

root.mainloop()