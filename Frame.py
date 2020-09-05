from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frame")
root.iconbitmap("Coffee.ico")


frame = LabelFrame(root,text=" this is my frame", padx = 5,pady = 5)
frame.pack(padx = 10,pady = 10)

#just ex
b= Button(frame,text="click me")
b.pack()

root.mainloop()
