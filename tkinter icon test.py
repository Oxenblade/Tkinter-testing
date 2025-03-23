from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title("Yoshitha's New Project")
root.iconbitmap("C:/Users/Dell/Downloads/New folder (4)/python_104451.ico")

my_img = ImageTk.PhotoImage(Image.open("python.png"))
my_label = Label(image= my_img)

my_label.pack()




root.mainloop()
