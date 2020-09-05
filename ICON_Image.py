from tkinter import *
from PIL import ImageTk,Image


win=Tk()
#add icon to win
win.iconbitmap('Coffee.ico')

my_img=ImageTk.PhotoImage(Image.open("images.jpg"))
my_label=Label(image = my_img).pack()


button_quit=Button(win,text="Exit",command=win.quit)
button_quit.pack()
win.mainloop()
