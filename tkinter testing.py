from tkinter import *

# label creating
'''root = Tk()

mylabel = Label(root, text= "Hello World")

mylabel.pack()

root.mainloop()'''

#button and label creating 
'''root = Tk()


def my_Click():
    my_label = Label(root, text = " Hey Yo ! I clicked a button !", fg = "Brown", bg = "Light Green")
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()'''

#input fields

'''root = Tk()

e = Entry(root, width=50, borderwidth=15)
e.pack()
e.insert(0, "Enter your name: ")

def my_Click():
    Hello = "Hello" + e.get()
    my_label = Label(root, text= Hello)
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()'''


'''root = Tk()

e = Entry(root, width=50, borderwidth=15)
e.pack()
e.insert(0, "Enter your name: ")

def my_Click():
    Hello = "Hello" + e.get()
    my_label = Label(root, text= Hello)
    my_label.pack()


my_button = Button(root, text= "Click Me Dammit! ", command =my_Click, fg= "Red", bg ="Yellow")
my_button.pack()

root.mainloop()'''


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width =35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    e.delete(0, END)
    e.insert(0,number)
    
button_1 = Button(root, text="1", padx=40, pady=20, command=Lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=Lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=Lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=Lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=Lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=Lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=Lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=Lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=Lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=Lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=Lambda: button_click())
button_equal = Button(root, text="=", padx=91, pady=20, command=Lambda: button_click())
button_clear = Button(root, text="clear", padx=79, pady=20, command=Lambda: button_click())
#put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)


root.mainloop()


















