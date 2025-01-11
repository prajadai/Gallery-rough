from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import random

def preview(event, background_label, path, width, height):
    #preview of the image
    image = Image.open(path)

    # Calculate the maximum dimensions for the preview window
    max_width, max_height = 480, 300  # Adjust these values as needed

    # Maintain aspect ratio and fit within the preview window
    image_width, image_height = image.size
    ratio = min(max_width / image_width, max_height / image_height)
    new_width = int(image_width * ratio)
    new_height = int(image_height * ratio)

    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    background_label.config(image=photo)
    background_label.image = photo # Keep a reference to prevent garbage collection
    background_label.bind("<Button-1>", lambda event: display_img(event, path, width, height))

def display_img(event, path, width, height):
    dis_root = Toplevel()
    dis_root.geometry("1080x720")

    try:
        image = Image.open(path)  # Replace with your image path

        # Calculate the maximum dimensions for the preview window
        max_width, max_height = 1080, 720  # Adjust these values as needed

        # Maintain aspect ratio and fit within the preview window
        image_width, image_height = image.size
        ratio = min(max_width / image_width, max_height / image_height)
        new_width = int(image_width * ratio)
        new_height = int(image_height * ratio)

        image = image.resize((new_width , new_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(dis_root, image=photo)
        background_label.pack(fill="both", expand=True)

        dis_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def open_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
            ("All Files", "*.*")
        ]
    )
    if file_path:  # If a file is selected
        display_from_location( file_path)

def display_from_location(file_path):
    dis_root = Toplevel()
    dis_root.geometry("1080x720")

    background_label = Label(dis_root)
    background_label.pack()
    try:
        img = Image.open(file_path)

        # Calculate the maximum dimensions for the preview window
        max_width, max_height = 1080, 720  # Adjust these values as needed

        # Maintain aspect ratio and fit within the preview window
        image_width, image_height = img.size
        ratio = min(max_width / image_width, max_height / image_height)
        new_width = int(image_width * ratio)
        new_height = int(image_height * ratio)

        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
    
        background_label.config(image=img_tk)
        background_label.image = img_tk
        background_label.pack()
    except Exception as e:
        print(f"Error opening image: {e}")

def main():
    root = Tk()
    root.geometry("1080x720")
    root.title("Bhaila Gallery")
    root.wm_iconbitmap("apple.ico")
    root.config(bg="#87bab5")

    #create a frame to display the preview image
    global bg_frame
    bg_frame = Frame(root)
    bg_frame.pack(pady=20)

    img_list = ['Background.jpg', 'bhaila.jpg', 'daagi3.jpg', 'group_dance.jpg',
                'group.jpg', 'IMG1.jpg', 'IMG2.jpg', 'IMG3.jpg', 'IMG4.jpg', 'IMG5.jpg',
                'IMG6.jpg', 'IMG7.jpg', 'IMG8.jpg', 'IMG9.jpg', 'jyapugacha_daagi.jpg',
                'jyapugacha.jpg']
    
    # Load and resize the image
    choice = random.choice(img_list)
    image = Image.open(choice)
    
    # Calculate the maximum dimensions for the preview window
    max_width, max_height = 480,300  # Adjust these values as needed

    # Maintain aspect ratio and fit within the preview window
    image_width, image_height = image.size
    ratio = min(max_width / image_width, max_height / image_height)
    new_width = int(image_width * ratio)
    new_height = int(image_height * ratio)

    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the image as the background
    background_label = Label(bg_frame, image=photo)
    background_label.pack(fill=BOTH)
    
    #text
    Label(root, text="थिमि भैल: २०८१ ताहाननी", 
          font=("Courier",26), bg="#87bab5").pack(pady=12)
    Label(root, text="Photos:", font=("Courier", 16, UNDERLINE), bg="#87bab5").pack()

    # Create a scrollable frame for the icons
    canvas = Canvas(root, bg="#87bab5", width=665, height=195)
    canvas.pack(pady=6)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    #creating a frame for the icons
    icon_frame = Frame(canvas, bg="#87bab5", padx=4, pady=4)
    canvas.create_window((0,0), window=icon_frame)

     # Configure grid layout to center-align icons
    icon_frame.grid_columnconfigure(tuple(range(8)), weight=1)  # 8 columns, expanding
    icon_frame.grid_rowconfigure(0, weight=1)  # Allow row to expand for centering


    #used small icons of the images to be displayed and binded the label using mouse click
    for i, path in enumerate(img_list):
        try:
            icon = Image.open(path)

            # Calculate the maximum dimensions for the preview window
            max_width, max_height = 70,70  # Adjust these values as needed

            # Maintain aspect ratio and fit within the preview window
            image_width, image_height = icon.size
            ratio = min(max_width / image_width, max_height / image_height)
            new_width = int(image_width * ratio)
            new_height = int(image_height * ratio)

            icon_p = icon.resize((new_width, new_height), Image.Resampling.LANCZOS)
            pIcon = ImageTk.PhotoImage(icon_p)

            label = Label(icon_frame, image=pIcon, bg="#87bab5")
            label.grid(row=i // 8, column=i % 8, padx=5, pady=5, sticky="nsew")
            label.image = pIcon

            # Get the original image dimensions
            original_width, original_height = icon.size

            label.bind("<Button-1>", lambda event, p=path, w=original_width, h=original_height: preview(event, background_label, p, w, h))
            
        except FileNotFoundError:
            print("Image file not found:", path)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Update the canvas scroll region
    icon_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Button to open image
    open_button = Button(root, text="Open Image", command=open_image)
    open_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()