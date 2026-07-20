from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# list of image paths
image_paths = [
    r"D:\nanital trip\image\IMG_20260123_102957.jpg",
    r"D:\nanital trip\image\IMG_20260123_093611.jpg",
    r"D:\nanital trip\image\IMG_20260123_101031.jpg",
    r"D:\nanital trip\image\IMG_20260123_114302.jpg",
    r"D:\nanital trip\image\IMG_20260123_151500.jpg",
]

# resize the images to 1080 x 1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    photo_image = next(slideshow)
    label.config(image=photo_image)
    root.after(3000, update_image)

play_button = tk.Button(root, text='Play SlideShow', command=update_image)
play_button.pack()

root.mainloop()
