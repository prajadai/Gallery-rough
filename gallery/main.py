from tkinter import *
from PIL import Image, ImageTk

def Group():
    tush_root = Toplevel()
    tush_root.geometry("1080x720")
    tush_root.title("Group Photo")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\group.jpg")  # Replace with your image path
        image = image.resize((1080 , 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(tush_root, image=photo)
        background_label.pack(fill="both", expand=True)

        tush_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def bhaila():
    bhaila_root = Toplevel()
    bhaila_root.geometry("1080x720")
    bhaila_root.title("Bhaila")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\bhaila.jpg")  # Replace with your image path
        image = image.resize((455, 650), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(bhaila_root, image=photo)
        background_label.pack(fill="both", expand=True)

        bhaila_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def jyapugacha():
    jpg_root = Toplevel()
    jpg_root.geometry("1080x720")
    jpg_root.title("Tushar's Window")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\jyapugacha.jpg")  # Replace with your image path
        image = image.resize((1080, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(jpg_root, image=photo)
        background_label.pack(fill="both", expand=True)

        jpg_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def jpu_special():
    jp_root = Toplevel()
    jp_root.geometry("1080x720")
    jp_root.title("Tushar Special")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\jyapugacha1.jpeg")  # Replace with your image path
        image = image.resize((420, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(jp_root, image=photo)
        background_label.pack(fill="both", expand=True)

        jp_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def daagi():
    daagi_root = Toplevel()
    daagi_root.geometry("1080x720")
    daagi_root.title("Daagi")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\daagi3.jpg")  # Replace with your image path
        image = image.resize((1080, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(daagi_root, image=photo)
        background_label.pack(fill="both", expand=True)

        daagi_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def dance():
    d_root = Toplevel()
    d_root.geometry("1080x720")
    d_root.title("Dance")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\group_dance.jpg")  # Replace with your image path
        image = image.resize((1080, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(d_root, image=photo)
        background_label.pack(fill="both", expand=True)

        d_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def jp_dg():
    jd_root = Toplevel()
    jd_root.geometry("1080x720")
    jd_root.title("Jyapugacha x Daagi")

    try:
        image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\jyapugacha_daagi.jpg")  # Replace with your image path
        image = image.resize((1080, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(jd_root, image=photo)
        background_label.pack(fill="both", expand=True)

        jd_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    root.geometry("1080x720")
    root.title("Bhaila Gallery")
    root.wm_iconbitmap("apple.ico")

    # Load and resize the image
    image = Image.open("C:\\Users\\User\\coding1py\\tkinty\\gallery\\jyapugacha.jpg")
    image = image.resize((720 , 480), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the image as the background
    background_label = Label(root, image=photo)
    background_label.pack(fill=BOTH)
    
    #text
    Label(root, text="Album:", font=("Courier",20)).pack()

    #creating a frame for the buttons
    button_frame = Frame(root)
    button_frame.pack()

    #button creation and management
    bhaila_button = Button(button_frame, text="Bhaila", command=bhaila, relief=GROOVE)
    bhaila_button.grid(row=0,column=0)
    daagi_button = Button(button_frame, text="Daagi", command=daagi, relief=GROOVE)
    daagi_button.grid(row=0,column=1)
    jp_button = Button(button_frame, text="Jyapugacha", command=jyapugacha, relief=GROOVE)
    jp_button.grid(row=0,column=2)
    group_button = Button(button_frame, text="Group", command=Group, relief=GROOVE)
    group_button.grid(row=0,column=3)
    dance_button = Button(button_frame, text="Dance", command=dance, relief=GROOVE)
    dance_button.grid(row=0,column=4)
    jp1_button = Button(button_frame, text="Jyapugacha Special", command=jpu_special, relief=GROOVE)
    jp1_button.grid(row=1, column=0, columnspan=2)
    jpdg_button = Button(button_frame, text="Jyapugacha & Daagi", command=jp_dg, relief=GROOVE)
    jpdg_button.grid(row=1, column=3, columnspan=2)

    root.mainloop()