from tkinter import *
from PIL import Image, ImageTk
from tkinter import colorchooser

def preview(event, background_label, path):
    #preview of the image
    image = Image.open(path)
    image = image.resize((480, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    background_label.config(image=photo)
    background_label.image = photo # Keep a reference to prevent garbage collection
    background_label.bind("<Button-1>", lambda event: display_img(event, path))

def display_img(event, path):
    dis_root = Toplevel()
    dis_root.geometry("1080x720")

    try:
        image = Image.open(path)  # Replace with your image path
        image = image.resize((1080 , 720), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        background_label = Label(dis_root, image=photo)
        background_label.pack(fill="both", expand=True)

        dis_root.mainloop()
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

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

    # Load and resize the image
    image = Image.open("group.jpg")
    image = image.resize((480, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the image as the background
    background_label = Label(bg_frame, image=photo, bg="#87bab5")
    background_label.pack(fill=BOTH)
    
    #text
    Label(root, text="Album:", font=("Courier",20), bg="#87bab5").pack(anchor=CENTER)

    #creating a frame for the icons
    icon_frame = Frame(root, bg="#87bab5")
    icon_frame.pack()

    #used small icons of the images to be displayed and binded the label using mouse click
    #for group photo
    gr_icon = Image.open("group.jpg")
    gr_p = gr_icon.resize((70,70), Image.LANCZOS)
    pGr = ImageTk.PhotoImage(gr_p)
    grp_label = Label(icon_frame, image=pGr)
    grp_label.bind("<Button-1>", lambda event: preview(event, background_label, "group.jpg"))
    grp_label.grid(row=0, column=0)

    #for bhaila photo
    b1_icon = Image.open("bhaila.jpg") #open images and resize them as small icons
    bh_p = b1_icon.resize((70,70), Image.LANCZOS)
    pBh = ImageTk.PhotoImage(bh_p)
    bhaila_label = Label(icon_frame, image=pBh)
    bhaila_label.bind("<Button-1>", lambda event: preview(event, background_label, "bhaila.jpg")) #binding the left mouse button click to opening the image
    bhaila_label.grid(row=0, column=1)
   
   #for daagi photo
    d1_icon = Image.open("daagi3.jpg") #open images and resize them as small icons
    dg_p = d1_icon.resize((70,70), Image.LANCZOS)
    pDg = ImageTk.PhotoImage(dg_p)
    daagi_label = Label(icon_frame, image=pDg)
    daagi_label.bind("<Button-1>", lambda event: preview(event, background_label, "daagi3.jpg")) #binding the left mouse button click to opening the image
    daagi_label.grid(row=0, column=2)

    #for jyapugacha photo
    jPg_icon = Image.open("jyapugacha.jpg") #open images and resize them as small icons
    jPg_p = jPg_icon.resize((70,70), Image.LANCZOS)
    pJpg = ImageTk.PhotoImage(jPg_p)
    jyapugacha_label = Label(icon_frame, image=pJpg)
    jyapugacha_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha.jpg")) #binding the left mouse button click to opening the image
    jyapugacha_label.grid(row=0, column=3)

    #for IMG3
    img3_icon = Image.open("IMG3.jpg") #open images and resize them as small icons
    img3_p = img3_icon.resize((70,70), Image.LANCZOS)
    pImg3 = ImageTk.PhotoImage(img3_p)
    img3_label = Label(icon_frame, image=pImg3)
    img3_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG3.jpg")) #binding the left mouse button click to opening the image
    img3_label.grid(row=0, column=4)

    #for jyapugacha special photo
    jPgs_icon = Image.open("jyapugacha1.jpeg") #open images and resize them as small icons
    jPgs_p = jPgs_icon.resize((70,70), Image.LANCZOS)
    pJpgs = ImageTk.PhotoImage(jPgs_p)
    jpg1_label = Label(icon_frame, image=pJpgs)
    jpg1_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha1.jpeg")) #binding the left mouse button click to opening the image
    jpg1_label.grid(row=1, column=0)

    #for jyapugacha and daagi photo
    jPgDg_icon = Image.open("jyapugacha_daagi.jpg") #open images and resize them as small icons
    jPgDg_p = jPgDg_icon.resize((70,70), Image.LANCZOS)
    pJpgDg = ImageTk.PhotoImage(jPgDg_p)
    jpgdg_label = Label(icon_frame, image=pJpgDg)
    jpgdg_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha_daagi.jpg")) #binding the left mouse button click to opening the image
    jpgdg_label.grid(row=1, column=1)

    #for jdance photo
    Dance_icon = Image.open("group_dance.jpg") #open images and resize them as small icons
    Dance_p = Dance_icon.resize((70,70), Image.LANCZOS)
    pDance = ImageTk.PhotoImage(Dance_p)
    dance_label = Label(icon_frame, image=pDance)
    dance_label.bind("<Button-1>", lambda event: preview(event, background_label, "group_dance.jpg")) #binding the left mouse button click to opening the image
    dance_label.grid(row=1, column=2)

    #for IMG1
    img1_icon = Image.open("IMG1.jpg") #open images and resize them as small icons
    img1_p = img1_icon.resize((70,70), Image.LANCZOS)
    pImg1 = ImageTk.PhotoImage(img1_p)
    img1_label = Label(icon_frame, image=pImg1)
    img1_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG1.jpg")) #binding the left mouse button click to opening the image
    img1_label.grid(row=1, column=3)

    #for IMG2
    img2_icon = Image.open("IMG2.jpg") #open images and resize them as small icons
    img2_p = img2_icon.resize((70,70), Image.LANCZOS)
    pImg2 = ImageTk.PhotoImage(img2_p)
    img2_label = Label(icon_frame, image=pImg2)
    img2_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG2.jpg")) #binding the left mouse button click to opening the image
    img2_label.grid(row=1, column=4)

    #img3 is at row0,col4
    #for IMG4
    img4_icon = Image.open("IMG4.jpg") #open images and resize them as small icons
    img4_p = img4_icon.resize((70,70), Image.LANCZOS)
    pImg4 = ImageTk.PhotoImage(img4_p)
    img4_label = Label(icon_frame, image=pImg4)
    img4_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG4.jpg")) #binding the left mouse button click to opening the image
    img4_label.grid(row=0, column=5)

    #for IMG5
    img5_icon = Image.open("IMG5.jpg") #open images and resize them as small icons
    img5_p = img5_icon.resize((70,70), Image.LANCZOS)
    pImg5 = ImageTk.PhotoImage(img5_p)
    img5_label = Label(icon_frame, image=pImg5)
    img5_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG5.jpg")) #binding the left mouse button click to opening the image
    img5_label.grid(row=0, column=6)

    #for IMG6
    img6_icon = Image.open("IMG6.jpg") #open images and resize them as small icons
    img6_p = img6_icon.resize((70,70), Image.LANCZOS)
    pImg6 = ImageTk.PhotoImage(img6_p)
    img6_label = Label(icon_frame, image=pImg6)
    img6_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG6.jpg")) #binding the left mouse button click to opening the image
    img6_label.grid(row=0, column=7)

    #for IMG7
    img7_icon = Image.open("IMG7.jpg") #open images and resize them as small icons
    img7_p = img7_icon.resize((70,70), Image.LANCZOS)
    pImg7 = ImageTk.PhotoImage(img7_p)
    img7_label = Label(icon_frame, image=pImg7)
    img7_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG7.jpg")) #binding the left mouse button click to opening the image
    img7_label.grid(row=1, column=5)

    #for IMG8
    img8_icon = Image.open("IMG8.jpg") #open images and resize them as small icons
    img8_p = img8_icon.resize((70,70), Image.LANCZOS)
    # img8_p = Image.rotate(90, expand=TRUE)
    pImg8 = ImageTk.PhotoImage(img8_p)
    img8_label = Label(icon_frame, image=pImg8)
    img8_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG8.jpg")) #binding the left mouse button click to opening the image
    img8_label.grid(row=1, column=6)

    #for IMG9
    img9_icon = Image.open("IMG9.jpg") #open images and resize them as small icons
    img9_p = img9_icon.resize((70,70), Image.LANCZOS)
    pImg9 = ImageTk.PhotoImage(img9_p)
    img9_label = Label(icon_frame, image=pImg9)
    img9_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG9.jpg")) #binding the left mouse button click to opening the image
    img9_label.grid(row=1, column=7)

    root.mainloop()

if __name__ == "__main__":
    main()