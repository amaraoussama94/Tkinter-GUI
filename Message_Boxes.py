from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("M_B")
root.iconbitmap('Coffee.ico')
def popup():
    #messagebox.showinfo("info","hello")
    #messagebox.showwarning("info","hello")
    #messagebox.showerror("info","hello")
    #messagebox.askquestion("info","hello")
    #messagebox.askokcancel("info","hello")
    response=messagebox.askyesno("info","hello")
    Label(root,text=response).pack()
    if response==1 :
        Label(root,text="you clicked  yes!").pack()
    else:
        Label(root,text="you clicked  no!").pack()

Button(root,text="Popup",command= popup).pack()

                
root.mainloop()
