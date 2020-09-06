from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root=Tk()
root.title("W_A")
root.iconbitmap('Coffee.ico')
root.geometry("400x40")

def graph():
    house_price =np.random.normal(200000,25000,5000)
    plt.hist(house_price,50 )
    plt.show()


my_button=Button(root,text= "graphic", command = graph).pack()
           
root.mainloop()


