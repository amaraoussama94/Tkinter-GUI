from tkinter import *

#showing a msg #window
win=Tk()

def myClick():
    myLabel=Label(win,text="Hi").pack()

#create button
#myButton= Button(win,text="Click me !",padx=20).pack()

#Diable the button
#myButton= Button(win,text="Click me !",state =DISABLED).pack()

#resize the button
#myButton= Button(win,text="Click me !",padx=20,pady=30).pack()

#showing something after click the button
#myButton= Button(win,text="Click me !",command=myClick).pack()

#change the Text color fg an background color bg
myButton= Button(win,text="Click me !",command=myClick,fg="blue",bg= "red").pack()

win.mainloop()
