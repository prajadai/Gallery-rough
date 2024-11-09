from tkinter import *
from PIL import Image, ImageTk
from tkinter import colorchooser

def Group(event):
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

def bhaila(event):
    bhaila_root = Toplevel()
    bhaila_root.geometry("1080x720")
    bhaila_root.title("Bhaila")

    try:
        image = Image.open("bhaila.jpg")  # Replace with your image path
        image = image.resize((455, 650), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(bhaila_root, image=photo)
        background_label.pack(fill="both", expand=True)

        bhaila_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def daagi(event):
    daagi_root = Toplevel()
    daagi_root.geometry("1080x720")
    daagi_root.title("Daagi")

    try:
        image = Image.open("daagi3.jpg")  # Replace with your image path
        image = image.resize((1080, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(daagi_root, image=photo)
        background_label.pack(fill="both", expand=True)

        daagi_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def jyapugacha(event):
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

def jpu_special(event):
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

def jp_dg(event):
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

def dance(event):
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

def Img1(event):
    Img1_root = Toplevel()
    Img1_root.geometry("1080x720")
    Img1_root.title("Img1")

    try:
        image = Image.open("IMG1.jpg")  # Replace with your image path
        image = image.resize((480, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img1_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img1_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img2(event):
    Img2_root = Toplevel()
    Img2_root.geometry("1080x720")
    Img2_root.title("Img2")

    try:
        image = Image.open("IMG2.jpg")  # Replace with your image path
        image = image.resize((480, 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img2_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img2_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img3(event):
    Img3_root = Toplevel()
    Img3_root.geometry("1080x720")
    Img3_root.title("Img3")

    try:
        image = Image.open("IMG3.jpg")  # Replace with your image path
        image = image.resize((1080, 810), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img3_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img3_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img4(event):
    Img4_root = Toplevel()
    Img4_root.geometry("1080x720")
    Img4_root.title("Img4")

    try:
        image = Image.open("IMG4.jpg")  # Replace with your image path
        image = image.resize((1080, 810), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img4_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img4_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img5(event):
    Img5_root = Toplevel()
    Img5_root.geometry("1080x720")
    Img5_root.title("Img5")

    try:
        image = Image.open("IMG5.jpg")  # Replace with your image path
        image = image.resize((1080, 810), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img5_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img5_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img6(event):
    Img6_root = Toplevel()
    Img6_root.geometry("1080x720")
    Img6_root.title("Img6")

    try:
        image = Image.open("IMG6.jpg")  # Replace with your image path
        image = image.resize((1080, 810), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img6_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img6_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img7(event):
    Img7_root = Toplevel()
    Img7_root.geometry("1080x720")
    Img7_root.title("Img7")

    try:
        image = Image.open("IMG7.jpg")  # Replace with your image path
        image = image.resize((1080, 810), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img7_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img7_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img8(event):
    Img8_root = Toplevel()
    Img8_root.geometry("1080x720")
    Img8_root.title("Img8")

    try:
        image = Image.open("IMG8.jpg")  # Replace with your image path
        image = image.resize((540 , 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img8_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img8_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def Img9(event):
    Img9_root = Toplevel()
    Img9_root.geometry("1080x720")
    Img9_root.title("Img9")

    try:
        image = Image.open("IMG9.jpg")  # Replace with your image path
        image = image.resize((540 , 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(Img9_root, image=photo)
        background_label.pack(fill="both", expand=True)

        Img9_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    root.geometry("1080x720")
    root.title("Bhaila Gallery")
    root.wm_iconbitmap("apple.ico")
    # print(colorchooser.askcolor())
    root.config(bg="#87bab5")

    # Load and resize the image
    image = Image.open("group.jpg")
    image = image.resize((480, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the image as the background
    background_label = Label(root, image=photo, bg="#87bab5")
    background_label.pack(pady=20, fill=BOTH)
    
    #text
    Label(root, text="Album:", font=("Courier",20), bg="#87bab5").pack()

    #creating a frame for the icons
    icon_frame = Frame(root, bg="#87bab5")
    icon_frame.pack()

    #used small icons of the images to be displayed and binded the label using mouse click
    #for group photo
    gr_icon = Image.open("group.jpg")
    gr_p = gr_icon.resize((70,70), Image.LANCZOS)
    pGr = ImageTk.PhotoImage(gr_p)
    grp_label = Label(icon_frame, image=pGr)
    grp_label.bind("<Button-1>", Group)
    grp_label.grid(row=0, column=0)

    #for bhaila photo
    b1_icon = Image.open("bhaila.jpg") #open images and resize them as small icons
    bh_p = b1_icon.resize((70,70), Image.LANCZOS)
    pBh = ImageTk.PhotoImage(bh_p)
    bhaila_label = Label(icon_frame, image=pBh)
    bhaila_label.bind("<Button-1>", bhaila) #binding the left mouse button click to opening the image
    bhaila_label.grid(row=0, column=1)
   
   #for daagi photo
    d1_icon = Image.open("daagi3.jpg") #open images and resize them as small icons
    dg_p = d1_icon.resize((70,70), Image.LANCZOS)
    pDg = ImageTk.PhotoImage(dg_p)
    daagi_label = Label(icon_frame, image=pDg)
    daagi_label.bind("<Button-1>", daagi) #binding the left mouse button click to opening the image
    daagi_label.grid(row=0, column=2)

    #for jyapugacha photo
    jPg_icon = Image.open("jyapugacha.jpg") #open images and resize them as small icons
    jPg_p = jPg_icon.resize((70,70), Image.LANCZOS)
    pJpg = ImageTk.PhotoImage(jPg_p)
    jyapugacha_label = Label(icon_frame, image=pJpg)
    jyapugacha_label.bind("<Button-1>", jyapugacha) #binding the left mouse button click to opening the image
    jyapugacha_label.grid(row=0, column=3)

    #for IMG3
    img3_icon = Image.open("IMG3.jpg") #open images and resize them as small icons
    img3_p = img3_icon.resize((70,70), Image.LANCZOS)
    pImg3 = ImageTk.PhotoImage(img3_p)
    img3_label = Label(icon_frame, image=pImg3)
    img3_label.bind("<Button-1>", Img3) #binding the left mouse button click to opening the image
    img3_label.grid(row=0, column=4)

    #for jyapugacha special photo
    jPgs_icon = Image.open("jyapugacha1.jpeg") #open images and resize them as small icons
    jPgs_p = jPgs_icon.resize((70,70), Image.LANCZOS)
    pJpgs = ImageTk.PhotoImage(jPgs_p)
    jpg1_label = Label(icon_frame, image=pJpgs)
    jpg1_label.bind("<Button-1>", jpu_special) #binding the left mouse button click to opening the image
    jpg1_label.grid(row=1, column=0)

    #for jyapugacha and daagi photo
    jPgDg_icon = Image.open("jyapugacha_daagi.jpg") #open images and resize them as small icons
    jPgDg_p = jPgDg_icon.resize((70,70), Image.LANCZOS)
    pJpgDg = ImageTk.PhotoImage(jPgDg_p)
    jpgdg_label = Label(icon_frame, image=pJpgDg)
    jpgdg_label.bind("<Button-1>", jp_dg) #binding the left mouse button click to opening the image
    jpgdg_label.grid(row=1, column=1)

    #for jdance photo
    Dance_icon = Image.open("group_dance.jpg") #open images and resize them as small icons
    Dance_p = Dance_icon.resize((70,70), Image.LANCZOS)
    pDance = ImageTk.PhotoImage(Dance_p)
    dance_label = Label(icon_frame, image=pDance)
    dance_label.bind("<Button-1>", dance) #binding the left mouse button click to opening the image
    dance_label.grid(row=1, column=2)

    #for IMG1
    img1_icon = Image.open("IMG1.jpg") #open images and resize them as small icons
    img1_p = img1_icon.resize((70,70), Image.LANCZOS)
    pImg1 = ImageTk.PhotoImage(img1_p)
    img1_label = Label(icon_frame, image=pImg1)
    img1_label.bind("<Button-1>", Img1) #binding the left mouse button click to opening the image
    img1_label.grid(row=1, column=3)

    #for IMG2
    img2_icon = Image.open("IMG2.jpg") #open images and resize them as small icons
    img2_p = img2_icon.resize((70,70), Image.LANCZOS)
    pImg2 = ImageTk.PhotoImage(img2_p)
    img2_label = Label(icon_frame, image=pImg2)
    img2_label.bind("<Button-1>", Img2) #binding the left mouse button click to opening the image
    img2_label.grid(row=1, column=4)

    #img3 is at row0,col4
    #for IMG4
    img4_icon = Image.open("IMG4.jpg") #open images and resize them as small icons
    img4_p = img4_icon.resize((70,70), Image.LANCZOS)
    pImg4 = ImageTk.PhotoImage(img4_p)
    img4_label = Label(icon_frame, image=pImg4)
    img4_label.bind("<Button-1>", Img4) #binding the left mouse button click to opening the image
    img4_label.grid(row=2, column=0)

    #for IMG5
    img5_icon = Image.open("IMG5.jpg") #open images and resize them as small icons
    img5_p = img5_icon.resize((70,70), Image.LANCZOS)
    pImg5 = ImageTk.PhotoImage(img5_p)
    img5_label = Label(icon_frame, image=pImg5)
    img5_label.bind("<Button-1>", Img5) #binding the left mouse button click to opening the image
    img5_label.grid(row=2, column=1)

    #for IMG6
    img6_icon = Image.open("IMG6.jpg") #open images and resize them as small icons
    img6_p = img6_icon.resize((70,70), Image.LANCZOS)
    pImg6 = ImageTk.PhotoImage(img6_p)
    img6_label = Label(icon_frame, image=pImg6)
    img6_label.bind("<Button-1>", Img6) #binding the left mouse button click to opening the image
    img6_label.grid(row=2, column=2)

    #for IMG7
    img7_icon = Image.open("IMG7.jpg") #open images and resize them as small icons
    img7_p = img7_icon.resize((70,70), Image.LANCZOS)
    pImg7 = ImageTk.PhotoImage(img7_p)
    img7_label = Label(icon_frame, image=pImg7)
    img7_label.bind("<Button-1>", Img7) #binding the left mouse button click to opening the image
    img7_label.grid(row=2, column=3)

    #for IMG8
    img8_icon = Image.open("IMG8.jpg") #open images and resize them as small icons
    img8_p = img8_icon.resize((70,70), Image.LANCZOS)
    # img8_p = Image.rotate(90, expand=TRUE)
    pImg8 = ImageTk.PhotoImage(img8_p)
    img8_label = Label(icon_frame, image=pImg8)
    img8_label.bind("<Button-1>", Img8) #binding the left mouse button click to opening the image
    img8_label.grid(row=2, column=4)

    #for IMG9
    img9_icon = Image.open("IMG9.jpg") #open images and resize them as small icons
    img9_p = img9_icon.resize((70,70), Image.LANCZOS)
    pImg9 = ImageTk.PhotoImage(img9_p)
    img9_label = Label(icon_frame, image=pImg9)
    img9_label.bind("<Button-1>", Img9) #binding the left mouse button click to opening the image
    img9_label.grid(row=3, column=2)

    root.mainloop()