from tkinter import *
from PIL import ImageTk,Image

def open():
    global my_image
    top= Toplevel()
    top.title("N_W*")
    top.iconbitmap('Coffee.ico')
    #lbl=Label(top,text="hello world").pack()
    my_image=ImageTk.PhotoImage(Image.open("images.jpg"))
    my_label=Label(top,image=my_image).pack()    
    btn2=Button(top,text="close windo",command= top.destroy).pack()



root = Tk()
root.title("N_W")
root.iconbitmap('Coffee.ico')

btn=Button(root,text="open new  windo",command=open).pack()



root.mainloop()
