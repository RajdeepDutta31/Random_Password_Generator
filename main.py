#Random Password Generator
#Author - Rajdeep Dutta

import random
import pyperclip
from tkinter import *
my_root = Tk()
my_root.title("Random Password Generator")
my_root.geometry("300x300")
my_root.config(bg="Black")

l1 = Label(text = "Password Generator", bg = "Black", fg= "Yellow", relief = SUNKEN, borderwidth = 3)
l1.config(font=("Arial",20,"bold"))
l1.pack(pady= 15)

l2 = Label(text = "Enter the no of character", bg = "Black", fg= "Yellow")
l2.config(font=("Arial",10,"bold italic"))
l2.pack()

e1 = Entry()
e1.pack()

def copy2board(x):
    pyperclip.copy(x)          #Copy to Clipboard

def gen_pass():
    password = ""
    n_el = int(e1.get())
    for i in range(n_el):
        if i==int(n_el/2):
            password += "@"
        else:
            password = password + chr(random.randrange(50,122))

    l3 = Label(text = str(password) , bg = "Black", fg= "Yellow")
    l3.config(font=("Arial",10,"bold italic"))
    l3.pack(pady = 10)

    b2 = Button(text = "Copy",command = copy2board(password), fg ="Black", bg= "Yellow")
    b2.config(width=5)
    b2.pack(side = BOTTOM)
    

b1 = Button(text = "Generate Password",command =gen_pass, fg ="Black", bg= "Yellow")
b1.pack(side = BOTTOM, pady = 20)

my_root.mainloop()
