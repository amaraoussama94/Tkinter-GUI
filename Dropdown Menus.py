from tkinter import *
from PIL import ImageTk,Image


def show ():
    my_label= Label (root ,text=clicked.get()).pack()
root = Tk()
root.title("D_M")
root.iconbitmap('Coffee.ico')

option = ["M",
          "S",
          "X"]
clicked=StringVar()
clicked.set(option [0])

drop= OptionMenu(root, clicked,*option)
drop.pack()

my_button= Button(root,text="show" ,command =show).pack()
root.mainloop()
