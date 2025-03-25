from tkinter import *

root = Tk()
root.title("project 01")
root.iconbitmap("C:/Users/hp/Downloads/New folder (4)/python_104451.ico")
root.geometry("500x500")

class elder:
    #root
    def clicker(self):
        print("look at you.. you clicked a button!")
        
    def __init__(self, master):
        myframe = Frame(master)
        myframe.pack()

        self.mybutton = Button( master, text="Click", command = self.clicker)
        self.mybutton.pack(pady=20)

  


        
e = elder(root)



root.mainloop()
