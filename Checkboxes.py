from tkinter import *
from PIL import ImageTk,Image

def show ():
    my_label= Label(root , text= var.get()).pack()
    my_label2= Label(root , text= var2.get()).pack()
    
    
root = Tk()
root.title("C_B")
root.iconbitmap('Coffee.ico')

#var= IntVar()
var= StringVar()
#c= Checkbutton(root,text="check  box",variable= var)
c= Checkbutton(root,text="check  box",variable= var,onvalue="on" , offvalue="off")
c.deselect()
c.pack()

var2= StringVar()
#d= Checkbutton(root,text="check  box",variable= var2)
d= Checkbutton(root,text="check  box",variable= var2,onvalue="pizza" , offvalue="hum")
d.deselect()
d.pack()

#my_label= Label(root , text= var.get()).pack()
my_btn= Button( root, text="click", command= show ).pack()

root.mainloop()
