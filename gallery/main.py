from tkinter import *
from PIL import Image, ImageTk
from tkinter import colorchooser

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

    image = image.resize((new_width, new_height), Image.LANCZOS)
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
    image = Image.open("Background.jpg")
    
    # Calculate the maximum dimensions for the preview window
    max_width, max_height = 480,300  # Adjust these values as needed

    # Maintain aspect ratio and fit within the preview window
    image_width, image_height = image.size
    ratio = min(max_width / image_width, max_height / image_height)
    new_width = int(image_width * ratio)
    new_height = int(image_height * ratio)

    image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Set the image as the background
    background_label = Label(bg_frame, image=photo)
    background_label.pack(fill=BOTH)
    
    #text
    Label(root, 
          text="थिमि भैल: २०८१ ताहाननी", 
          font=("Courier",26), 
          bg="#87bab5").pack(pady=12)

    #creating a frame for the icons
    icon_frame = Frame(root, bg="#87bab5")
    icon_frame.pack()

    #used small icons of the images to be displayed and binded the label using mouse click
    #for group photo
    gr_icon = Image.open("group.jpg")
    gr_p = gr_icon.resize((70,70), Image.LANCZOS)
    pGr = ImageTk.PhotoImage(gr_p)
    widthG, heightG = gr_icon.size
    grp_label = Label(icon_frame, image=pGr)
    grp_label.bind("<Button-1>", lambda event: preview(event, background_label, "group.jpg", widthG, heightG))
    grp_label.grid(row=0, column=0)

    #for bhaila photo
    b1_icon = Image.open("bhaila.jpg") #open images and resize them as small icons
    bh_p = b1_icon.resize((70,70), Image.LANCZOS)
    pBh = ImageTk.PhotoImage(bh_p)    # print(f"W: {width}, h: {height}")
    widthB, heightB = b1_icon.size      #obtain the real pixels of the pictures
    bhaila_label = Label(icon_frame, image=pBh)
    bhaila_label.bind("<Button-1>", lambda event: preview(event, background_label, "bhaila.jpg", widthB, heightB)) #binding the left mouse button click to opening the image
    bhaila_label.grid(row=0, column=1)
   
   #for daagi photo
    d1_icon = Image.open("daagi3.jpg") #open images and resize them as small icons
    dg_p = d1_icon.resize((70,70), Image.LANCZOS)
    pDg = ImageTk.PhotoImage(dg_p)
    widthD, heightD = d1_icon.size
    daagi_label = Label(icon_frame, image=pDg)
    daagi_label.bind("<Button-1>", lambda event: preview(event, background_label, "daagi3.jpg", widthD, heightD)) #binding the left mouse button click to opening the image
    daagi_label.grid(row=0, column=2)

    #for jyapugacha photo
    jPg_icon = Image.open("jyapugacha.jpg") #open images and resize them as small icons
    jPg_p = jPg_icon.resize((70,70), Image.LANCZOS)
    pJpg = ImageTk.PhotoImage(jPg_p)
    widthJ, heightJ = jPg_icon.size
    jyapugacha_label = Label(icon_frame, image=pJpg)
    jyapugacha_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha.jpg", widthJ, heightJ)) #binding the left mouse button click to opening the image
    jyapugacha_label.grid(row=0, column=3)

    #for IMG3
    img3_icon = Image.open("IMG3.jpg") #open images and resize them as small icons
    img3_p = img3_icon.resize((70,70), Image.LANCZOS)
    pImg3 = ImageTk.PhotoImage(img3_p)
    width3, height3 = img3_icon.size
    img3_label = Label(icon_frame, image=pImg3)
    img3_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG3.jpg", width3, height3)) #binding the left mouse button click to opening the image
    img3_label.grid(row=0, column=4)

    #for jyapugacha special photo
    jPgs_icon = Image.open("jyapugacha1.jpeg") #open images and resize them as small icons
    jPgs_p = jPgs_icon.resize((70,70), Image.LANCZOS)
    pJpgs = ImageTk.PhotoImage(jPgs_p)
    width_Js , height_Js = jPgs_icon.size
    jpg1_label = Label(icon_frame, image=pJpgs)
    jpg1_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha1.jpeg", width_Js, height_Js)) #binding the left mouse button click to opening the image
    jpg1_label.grid(row=1, column=0)

    #for jyapugacha and daagi photo
    jPgDg_icon = Image.open("jyapugacha_daagi.jpg") #open images and resize them as small icons
    jPgDg_p = jPgDg_icon.resize((70,70), Image.LANCZOS)
    pJpgDg = ImageTk.PhotoImage(jPgDg_p)
    width_Jd, height_Jd = jPgDg_icon.size
    jpgdg_label = Label(icon_frame, image=pJpgDg)
    jpgdg_label.bind("<Button-1>", lambda event: preview(event, background_label, "jyapugacha_daagi.jpg", width_Jd, height_Jd)) #binding the left mouse button click to opening the image
    jpgdg_label.grid(row=1, column=1)

    #for group dance photo
    Dance_icon = Image.open("group_dance.jpg") #open images and resize them as small icons
    Dance_p = Dance_icon.resize((70,70), Image.LANCZOS)
    pDance = ImageTk.PhotoImage(Dance_p)
    width_Gd, height_Gd = Dance_icon.size
    dance_label = Label(icon_frame, image=pDance)
    dance_label.bind("<Button-1>", lambda event: preview(event, background_label, "group_dance.jpg", width_Gd, height_Gd)) #binding the left mouse button click to opening the image
    dance_label.grid(row=1, column=2)

    #for IMG1
    img1_icon = Image.open("IMG1.jpg") #open images and resize them as small icons
    img1_p = img1_icon.resize((70,70), Image.LANCZOS)
    pImg1 = ImageTk.PhotoImage(img1_p)
    width1, height1 = img1_icon.size
    img1_label = Label(icon_frame, image=pImg1)
    img1_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG1.jpg", width1, height1)) #binding the left mouse button click to opening the image
    img1_label.grid(row=1, column=3)

    #for IMG2
    img2_icon = Image.open("IMG2.jpg") #open images and resize them as small icons
    img2_p = img2_icon.resize((70,70), Image.LANCZOS)
    pImg2 = ImageTk.PhotoImage(img2_p)
    width2, height2 = img2_icon.size
    img2_label = Label(icon_frame, image=pImg2)
    img2_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG2.jpg", width2, height2)) #binding the left mouse button click to opening the image
    img2_label.grid(row=1, column=4)

    #img3 is at row0,col4
    #for IMG4
    img4_icon = Image.open("IMG4.jpg") #open images and resize them as small icons
    img4_p = img4_icon.resize((70,70), Image.LANCZOS)
    pImg4 = ImageTk.PhotoImage(img4_p)
    width4, height4 = img4_icon.size
    img4_label = Label(icon_frame, image=pImg4)
    img4_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG4.jpg", width4, height4)) #binding the left mouse button click to opening the image
    img4_label.grid(row=0, column=5)

    #for IMG5
    img5_icon = Image.open("IMG5.jpg") #open images and resize them as small icons
    img5_p = img5_icon.resize((70,70), Image.LANCZOS)
    pImg5 = ImageTk.PhotoImage(img5_p)
    width5, height5 = img5_icon.size
    img5_label = Label(icon_frame, image=pImg5)
    img5_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG5.jpg", width5, height5)) #binding the left mouse button click to opening the image
    img5_label.grid(row=0, column=6)

    #for IMG6
    img6_icon = Image.open("IMG6.jpg") #open images and resize them as small icons
    img6_p = img6_icon.resize((70,70), Image.LANCZOS)
    pImg6 = ImageTk.PhotoImage(img6_p)
    width6, height6 = img6_icon.size
    img6_label = Label(icon_frame, image=pImg6)
    img6_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG6.jpg", width6, height6)) #binding the left mouse button click to opening the image
    img6_label.grid(row=0, column=7)

    #for IMG7
    img7_icon = Image.open("IMG7.jpg") #open images and resize them as small icons
    img7_p = img7_icon.resize((70,70), Image.LANCZOS)
    pImg7 = ImageTk.PhotoImage(img7_p)
    width7, height7 = img7_icon.size
    img7_label = Label(icon_frame, image=pImg7)
    img7_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG7.jpg", width7, height7)) #binding the left mouse button click to opening the image
    img7_label.grid(row=1, column=5)

    #for IMG8
    img8_icon = Image.open("IMG8.jpg") #open images and resize them as small icons
    img8_p = img8_icon.resize((70,70), Image.LANCZOS)
    pImg8 = ImageTk.PhotoImage(img8_p)
    width8, height8 = img8_icon.size
    img8_label = Label(icon_frame, image=pImg8)
    img8_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG8.jpg", width8, height8)) #binding the left mouse button click to opening the image
    img8_label.grid(row=1, column=6)

    #for IMG9
    img9_icon = Image.open("IMG9.jpg") #open images and resize them as small icons
    img9_p = img9_icon.resize((70,70), Image.LANCZOS)
    pImg9 = ImageTk.PhotoImage(img9_p)
    width9, height9 = img9_icon.size
    img9_label = Label(icon_frame, image=pImg9)
    img9_label.bind("<Button-1>", lambda event: preview(event, background_label, "IMG9.jpg", width9, height9)) #binding the left mouse button click to opening the image
    img9_label.grid(row=1, column=7)

    root.mainloop()

if __name__ == "__main__":
    main()