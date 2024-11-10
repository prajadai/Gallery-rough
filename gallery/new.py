from tkinter import *
from PIL import Image, ImageTk

root = Tk()
image = Image.open("group.jpg")
photo = ImageTk.PhotoImage(image)
width, height = photo.width(), photo.height()
    # Set the image as the background
image = image.resize((480, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
background_label = Label(root, image=photo, bg="#87bab5")
background_label.pack(fill=BOTH)
print(f"Width: {width} Height: {height}")


root,mainloop()