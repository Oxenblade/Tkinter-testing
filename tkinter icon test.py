from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title("Yoshitha's New Project")
root.iconbitmap("C:/Users/hp/Downloads/New folder (4)/python_104451.ico")

my_img_1 = ImageTk.PhotoImage(Image.open("images/demon1.JPG"))
my_img_2 = ImageTk.PhotoImage(Image.open("images/demon2.JPG"))
my_img_3 = ImageTk.PhotoImage(Image.open("images/demon3.JPG"))
my_img_4 = ImageTk.PhotoImage(Image.open("images/demon4.JPG"))
my_img_5 = ImageTk.PhotoImage(Image.open("images/demon5.JPG"))
my_img_6 = ImageTk.PhotoImage(Image.open("images/abraham.JPG"))

image_list = [ my_img_1, my_img_2, my_img_3, my_img_4, my_img_5, my_img_6]

my_label = Label(image= my_img_1)
my_label.grid(row=3, column=0, columnspan =3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image= image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command = lambda:back(image_number-1))
    
    if image_number == 6:
        button_forward = Button(root, text=">>", state= DISABLED)
    
    my_label.grid(row=3, column=0, columnspan =3)
    button_forward.grid(row=2, column=2)
    button_back.grid(row =2, column = 0)
    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image= image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command = lambda:back(image_number-1))
    
    my_label.grid(row=3, column=0, columnspan =3)
    button_forward.grid(row=2, column=2)
    button_back.grid(row =2, column = 0)

    if image_number == 1:
        button_back = Button(root, text="<<", state= DISABLED)
        
button_back = Button(root, text="<<", command=back, state =DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))


button_back.grid(row =2, column = 0)
button_exit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)

root.mainloop()
