from tkinter import *

#showing a msg #window
win=Tk()

#input box
#e=Entry(win).pack()

#resize
#e=Entry(win,width=50,borderwidth=5).pack()

#color
#e=Entry(win,bg="blue",fg="white").pack()

#use input
def myClick():
    myLabel=Label(win,text="hi  "+e.get()).pack()
    
e=Entry(win)
e.pack()
#put dif text into the box 0
e.insert(0,"enter your text")
#button to show input text
myButton= Button(win,text="Click me !",command=myClick).pack()


win.mainloop()
