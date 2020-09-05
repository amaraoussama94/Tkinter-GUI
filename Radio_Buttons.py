from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('Coffee.ico')

#option-1
def clicked(value):
    mylabel=Label(root,text= value)
    mylabel.pack()

#r= IntVar()

#r.set("2")# set to option 2
    
#Radiobutton(root,text="option 1",variable=r ,value=1 , command= lambda : clicked(r.get())).pack()
#Radiobutton(root,text="option 2",variable=r ,value=2 , command= lambda : clicked(r.get())).pack()

#option2
#(txt,val)
MODES=[
    ("Pepperoni","1"),
    ("cheese","2"),
    ("Mushroom","3"),
    ("Onion","4"), 
    ]


pizza= StringVar()
pizza.set("1")

for text ,mode in MODES :
    Radiobutton(root,text=text ,variable=pizza , value = mode).pack(anchor=W)

    
mylabel=Label(root,text=pizza.get())
mylabel.pack()

mybutton=Button(root,text="hi",command= lambda : clicked(pizza.get()))
mybutton.pack()

                
                
root.mainloop()
