from tkinter import *
import tkinter.messagebox as tmgs 

root = Tk()
root.geometry("443x350")
root.title("Slider")

def getdollar():
    tmgs.showinfo('Amount credited ',f"You got {myslider.get()} dollars")

Label(text="How much dollars you want?",font='lucido 19 bold').pack()
myslider = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=10)
myslider.set(10)
myslider.pack(fill='x')

Button(text="Get dollar!",command=getdollar).pack(pady=20)

root.mainloop()