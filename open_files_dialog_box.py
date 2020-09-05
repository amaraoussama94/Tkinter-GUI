from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

def open ():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/tkinter", title="Select a file",filetypes=(("jpg files","*.jpg"),("all files","*.*") ))
    #my_label=Label(root, text= root.filename).pack()

    my_img=ImageTk.PhotoImage(Image.open(root.filename))
    my_label=Label(image = my_img).pack()


root = Tk()
root.title("O_D")
root.iconbitmap('Coffee.ico')


btn= Button(root, text= "open file" , command = open).pack()
root.mainloop()
