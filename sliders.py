from tkinter import *
from PIL import ImageTk,Image

def slide ():
    mly_label=Label(root,text = horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
    
root = Tk()
root.title("Sliders")
root.iconbitmap('Coffee.ico')
root.geometry("400x400")

vertical=Scale(root,from_=0, to=200)
vertical.pack()
horizontal=Scale(root,from_=0, to=200, orient=HORIZONTAL )
#horizontal=Scale(root,from_=0, to=200, orient=HORIZONTAL , command =slide ) // def slide (bar):
horizontal.pack()

#mly_label=Label(root,text = horizontal.get()).pack()

my_btn=Button(root, text="click me" , command = slide).pack()

root.mainloop()
