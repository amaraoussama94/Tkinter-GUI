from tkinter import *

#showing a msg #window
win=Tk()
#---------------------------Sol1-----------------------#

#creat label widget
#myLabel=Label(win,text="hello world")
#myLabel2=Label(win,text="My name is Oussama")

#P1
#showing  it into screen
#myLabel.pack() #size win=size  mg

#P2
#pos txt uing gring coord #fix coord
#myLabel.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)

#----------------------------------Sol2----------------------#
myLabel=Label(win,text="hello world").grid(row=0,column=0)
myLabel2=Label(win,text="My name is Oussama").grid(row=1,column=0)


win.mainloop()
