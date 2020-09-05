from tkinter import *

win=Tk()
#change title
win.title("Calculator")

def button_add():
    first_number=e.get()
    global f_num
    global math
    math= "addition"
    f_num=int(first_number)
    e.delete(0,END)
    print("hi+")
    
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math= "multiplication"
    f_num=int(first_number)
    e.delete(0,END)
    
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math= "division"
    f_num=int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math= "subtraction"
    f_num=int(first_number)
    e.delete(0,END)


def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0,f_num+int(second_number))
    if math =="subtraction":
        e.insert(0,f_num-int(second_number))
    if math =="division":
        e.insert(0,f_num/int(second_number))
    if math =="multiplication":
        e.insert(0,f_num*int(second_number))
   

def button_clear():
    e.delete(0,END)
    
def button_click(number):  
    current=e.get()
    e.delete(0,END)#clear the box
    e.insert(0,str(current) + str(number))

e=Entry(win,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#define buttons

Button_0=Button(win,text="0",padx=40,pady=20,command=lambda :button_click(0))
Button_1=Button(win,text="1",padx=40,pady=20,command=lambda :button_click(1))
Button_2=Button(win,text="2",padx=40,pady=20,command=lambda :button_click(2))
Button_3=Button(win,text="3",padx=40,pady=20,command=lambda :button_click(3))
Button_4=Button(win,text="4",padx=40,pady=20,command=lambda :button_click(4))
Button_5=Button(win,text="5",padx=40,pady=20,command=lambda :button_click(5))
Button_6=Button(win,text="6",padx=40,pady=20,command=lambda :button_click(6))
Button_7=Button(win,text="7",padx=40,pady=20,command=lambda :button_click(7))
Button_8=Button(win,text="8",padx=40,pady=20,command=lambda :button_click(8))
Button_9=Button(win,text="9",padx=40,pady=20,command=lambda :button_click(9))

button_add=Button(win,text="+",padx=39,pady=20,command=button_add)
button_subtract=Button(win,text="-",padx=40,pady=20,command=button_subtract)
button_multiply=Button(win,text="*",padx=39,pady=20,command=button_multiply)
button_divide=Button(win,text="/",padx=40,pady=20,command=button_divide)
button_equal=Button(win,text="=",padx=86,pady=20,command=button_equal)
button_clear=Button(win,text="Clear",padx=77,pady=20,command=button_clear)
#put the buttons on the screen

Button_0.grid(row=4,column=0)
Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)
Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)
Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

button_add.grid(row=5,column=0)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

win.mainloop()
